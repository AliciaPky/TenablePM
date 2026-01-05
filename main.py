from api.tenable_client import get_tenable_client
from collectors.scanner_collector import collect_scanner_health
from collectors.plugin_collector import collect_plugin_health
from collectors.scan_collector import collect_scan_health
from storage.json_writer import save_to_json

def main():
    print("[*] Connecting to Tenable...")
    tio = get_tenable_client()

    print("[*] Collecting scanner health...")
    scanners = collect_scanner_health(tio)

    print("[*] Collecting plugin health...")
    plugins = collect_plugin_health(tio)

    print("[*] Collecting scan health...")
    scans = collect_scan_health(tio)

    data = {
        "scanners": scanners,
        "plugins": plugins,
        "scans": scans
    }

    print("[*] Saving data to JSON...")
    save_to_json(data)

if __name__ == "__main__":
    main()
