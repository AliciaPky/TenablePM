from collectors.scan_collector import format_myt

def derive_scanner_health(scanner):
    issues = []

    # Scanner availability
    if scanner.get("status") != "on":
        issues.append("Scanner offline")

    # Health classification
    if not issues:
        health = "healthy"
    elif len(issues) <= 2:
        health = "warning"
    else:
        health = "critical"

    return health, issues

def collect_scanner_health(tio):
    results = []

    for s in tio.scanners.list():
        details = tio.scanners.details(s["id"])
        health, issues = derive_scanner_health(details)

        results.append({
            "scanner_id": details.get("id"),
            "scanner_name": details.get("name"),
            "status": details.get("status"),
            "health": health,
            "creation_date": format_myt(details.get("creation_date")),
            "last_modification_date": format_myt(details.get("last_modification_date")),
            "plugin_set": details.get("loaded_plugin_set"),
            "issues": issues,
            "ip_address": details.get("ips"),
        })

    return results
