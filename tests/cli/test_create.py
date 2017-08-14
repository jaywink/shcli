from unittest.mock import patch

from click.testing import CliRunner
from shcli.cli import shcli


@patch("shcli.cli.api.create")
def test_create_is_called(mock_create):
    runner = CliRunner()
    runner.invoke(shcli, ["create", "domain.tld", "token", "-t", "foobar", "-v", "self"])
    mock_create.assert_called_once_with("domain.tld", "token", text="foobar", visibility="self")


def test_create_requires_text_or_text_from_file():
    runner = CliRunner()
    response = runner.invoke(shcli, ["create", "domain.tld", "token", "-v", "self"])
    assert response.exit_code == 2


def test_create_requires_visibility():
    runner = CliRunner()
    response = runner.invoke(shcli, ["create", "domain.tld", "token", "-t", "foobar"])
    assert response.exit_code == 2
