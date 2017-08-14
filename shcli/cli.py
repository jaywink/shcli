import click

from shcli import api


@click.group()
def shcli():
    pass


@shcli.command()
@click.argument("domain")  # TODO validate domain?
@click.argument("token")
@click.option("--text", "-t")
@click.option("--text-from-file", "-f", type=click.File())
@click.option("--visibility", "-v", type=click.Choice(api.VISIBILITIES))
def create(domain, token, **kwargs):
    # Collect data and validate
    if kwargs.get("text"):
        text = kwargs.get("text")
    elif kwargs.get("text_from_file"):
        text = kwargs.get("text_from_file").read()
    else:
        raise click.UsageError("Must give either 'text' or 'text-from-file'.")
    if not kwargs.get("visibility"):
        raise click.UsageError("Must give 'visibility'.")

    # Create
    response = api.create(domain, token, text=text, visibility=kwargs.get("visibility"))
    click.echo(response)


if __name__ == "__main__":
    shcli()
