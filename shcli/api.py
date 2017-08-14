import requests

VISIBILITIES = ("public", "site", "limited", "self")


def validate_visibility(visibility):
    if visibility not in VISIBILITIES:
        raise ValueError("Visibility must be one of: %s" % (VISIBILITIES, ))


def create(domain, token, text, visibility):
    validate_visibility(visibility)
    response = requests.post(
        "https://%s/api/content/" % domain,
        headers={"Authorization": "Token %s" % token},
        data={
            "text": text,
            "visibility": visibility,
        }
    )
    return response.json()
