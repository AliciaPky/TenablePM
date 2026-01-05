from datetime import datetime, timezone, timedelta

MYT = timezone(timedelta(hours=8))


def format_myt(timestamp):
    # Convert Unix timestamp to readable MYT time
    return datetime.fromtimestamp(timestamp, tz=MYT).strftime(
        "%Y-%m-%d %H:%M:%S MYT"
    )

def derive_scan_health(scan):
    issues = []

    if scan.get("enabled") is False:
            issues.append("Scan is disabled")

    status = scan.get("status")

    if status in ["error"]:
        return "critical", ["Scan failed"]
    
    if status in ["canceled"]:
        return "critical", ["Scan was canceled"]

    if status == "running":
        issues.append("Scan currently running")

    last_modified = scan.get("last_modification_date")
    if last_modified:
        hours_since_update = (
            datetime.now(timezone.utc).timestamp() - last_modified
        ) / 3600

        if hours_since_update > 1440: # 60 days
            issues.append("Scan has not been updated in over 2 months")

    if not issues:
        return "healthy", []
    return "warning", issues

def collect_scan_health(tio):
    results = []

    for s in tio.scans.list():
        health, issues = derive_scan_health(s)

        last_mod = s.get("last_modification_date")
        last_mod_myt = format_myt(last_mod) if last_mod else None

        results.append({
            "scan_id": s.get("id"),
            "scan_name": s.get("name"),
            "status": s.get("status"),
            "enabled": s.get("enabled"),
            "health": health,
            "last_modification_date": last_mod_myt,
            "issues": issues,
        })

    return results
