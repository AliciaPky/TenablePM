from datetime import datetime, timezone


def derive_plugin_health(props):
    plugin_updated = props.get("plugin_updated")

    if not plugin_updated:
        return "critical", ["Plugin feed has never been updated"]

    hours_since = (
        datetime.now(timezone.utc).timestamp() - plugin_updated
    ) / 3600

    # Air-gapped or rarely updated systems
    if hours_since > 72:
        return "warning", ["Plugin feed older than 3 days"]

    return "healthy", []


def collect_plugin_health(tio):
    props = tio.server.properties()
    health, issues = derive_plugin_health(props)

    return {
        "health": health,
        "health_issues": issues,
        "plugin_set": props.get("plugin_set"),
        "plugin_updated": props.get("plugin_updated"),
        "feed": props.get("feed"),
    }
