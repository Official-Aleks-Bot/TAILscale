import http.client
import json
import argparse
from datetime import datetime, timedelta

def main(api_key, tailnet):
    conn = http.client.HTTPSConnection("api.tailscale.com")

    headers = {
        'Authorization': f"Bearer {api_key}",
        'Content-Type': "application/json"
    }

    offline_threshold = timedelta(seconds=1)
    current_time = datetime.utcnow()

    conn.request("GET", f"/api/v2/tailnet/{tailnet}/devices", headers=headers)
    res = conn.getresponse()
    data = res.read()
    devices_info = json.loads(data.decode("utf-8"))

    for i, device in enumerate(devices_info['devices'], start=1):
        os_type = device.get('os', '').lower()
        last_seen_str = device.get('lastSeen')

        if os_type == 'linux' and last_seen_str:
            last_seen_time = datetime.strptime(last_seen_str, "%Y-%m-%dT%H:%M:%SZ")
            time_diff = current_time - last_seen_time

            if time_diff >= offline_threshold:
                print("Removing")

                conn.request("DELETE", f"/api/v2/device/{device['id']}", headers=headers)
                res = conn.getresponse()
                data = res.read()
                response_data = data.decode("utf-8")

                if response_data.strip():
                    print(" ")
                else:
                    print("Device removal resulted in null response, skipping removal.")
            else:
                print("Device (Linux & Online) - Keeping")
        else:
            print("Device (Not Linux or Missing Last Seen)")

    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove offline Linux devices via the Tailscale API.")
    parser.add_argument("api_key", help="Your Tailscale API key")
    parser.add_argument("tailnet", help="Your Tailscale tailnet domain (e.g., taild9b7a6.ts.net)")
    args = parser.parse_args()

    main(args.api_key, args.tailnet)
