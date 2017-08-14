from unittest.mock import patch

import pytest

import shcli


def test_create_validates_visibility():
    with pytest.raises(ValueError):
        shcli.create("domain.tld", "token", "text", "visibility")
    shcli.create("domain.tld", "token", "text", "public")
    shcli.create("domain.tld", "token", "text", "limited")
    shcli.create("domain.tld", "token", "text", "site")
    shcli.create("domain.tld", "token", "text", "self")


@patch("shcli.api.requests.post")
def test_create_returns_does_correct_post(mock_post):
    shcli.create("domain.tld", "token", "text", "public")
    mock_post.assert_called_once_with(
        "https://domain.tld/api/content/",
        headers={"Authorization": "Token token"},
        data={
            "text": "text",
            "visibility": "public",
        }
    )
