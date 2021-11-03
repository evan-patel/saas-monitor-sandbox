SLACK_STATUS = (
    ("ok", "ok"),
    ("active", "active"),
    ("resolved", "resolved"),
    ("scheduled", "scheduled"),
    ("completed", "completed"),
    ("cancelled", "cancelled")
)
SLACK_INCIDENTS_TYPE = (
    ("incident", "incident"),
    ("notice", "notice"),
    ("outage", "outage")
)

SLACK_SERVICES = (
    ("Login/SSO", "Login/SSO"),
    ("Messaging", "Messaging"),
    ("Posts/Files", "Posts/Files"),
    ("Calls", "Calls"),
    ("Apps/Integrations/APIs", "Apps/Integrations/APIs"),
    ("Connections", "Connections"),
    ("Link Previews", "Link Previews"),
    ("Notifications", "Notifications"),
    ("Search", "Search"),
    ("Workspace/Org Administration", "Workspace/Org Administration")
)

INDICATORS = (
    ('major', 'major'),
    ('minor', 'minor'),
    ('none', 'none'),
    ('critical', 'critical')
)
