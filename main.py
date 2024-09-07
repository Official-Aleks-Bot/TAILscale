import http.client
import json
import argparse

def main(api_key, tailnet):
    conn = http.client.HTTPSConnection("api.tailscale.com")

    headers = {
        'Authorization': f"Bearer {api_key}",
        'Content-Type': "application/json"
    }

    devices_url = f"/api/v2/tailnet/{tailnet}/devices"

    conn.request("GET", devices_url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    devices_info = json.loads(data.decode("utf-8"))

    for i, device in enumerate(devices_info['devices'], start=1):
        os_type = device.get('os', '').lower()

        if os_type == 'linux':

            payload = json.dumps({
                "routes": ["0.0.0.0/0", "::/0"]
            })

            conn.request("POST", f"/api/v2/device/{device['id']}/routes", payload, headers)
            res = conn.getresponse()
            data = res.read()

        else:
            print("Skipping")

    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update routes for Linux devices via the Tailscale API.")
    parser.add_argument("api_key", help="Your Tailscale API key")
    parser.add_argument("tailnet", help="Your Tailscale tailnet domain (e.g., taild9b7a6.ts.net)")
    args = parser.parse_args()

    main(args.api_key, args.tailnet)
