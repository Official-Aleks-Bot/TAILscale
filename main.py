import http.client
import json
import argparse

def main(api_key, tailnet):
    # Establish a connection to the Tailscale API
    conn = http.client.HTTPSConnection("api.tailscale.com")

    # Your API key for authorization
    headers = {
        'Authorization': f"Bearer {api_key}",
        'Content-Type': "application/json"
    }

    # Construct the URL with the provided tailnet
    devices_url = f"/api/v2/tailnet/{tailnet}/devices"

    # First, get the list of devices
    conn.request("GET", devices_url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    devices_info = json.loads(data.decode("utf-8"))

    # Iterate through each device and update its enabled routes if it's a Linux device
    for i, device in enumerate(devices_info['devices'], start=1):
        os_type = device.get('os', '').lower()

        if os_type == 'linux':
            print(f"Device {i} (Linux): {device['hostname']}")

            # Prepare the payload to set the enabled routes
            payload = json.dumps({
                "routes": ["0.0.0.0/0", "::/0"]
            })

            # Make a POST request to set the enabled routes for the current device
            conn.request("POST", f"/api/v2/device/{device['id']}/routes", payload, headers)
            res = conn.getresponse()
            data = res.read()

            # Print the response to check if the operation was successful
            print(data.decode("utf-8"))
        else:
            print(f"Device {i} (Not Linux): {device['hostname']} - Skipping")

    # Close the connection
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update routes for Linux devices via the Tailscale API.")
    parser.add_argument("api_key", help="Your Tailscale API key")
    parser.add_argument("tailnet", help="Your Tailscale tailnet domain (e.g., taild9b7a6.ts.net)")
    args = parser.parse_args()

    main(args.api_key, args.tailnet)
