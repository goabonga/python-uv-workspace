# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Chris <goabonga@pm.me>

import click
import httpx

from . import __version__


@click.group()
def main() -> None:
    """Workspace demo CLI."""


@main.command()
def version() -> None:
    """Print the CLI's version."""
    click.echo(__version__)


@main.command()
@click.option("--name", default="world", show_default=True)
def greet(name: str) -> None:
    """Print a friendly greeting."""
    click.echo(f"Hello, {name}!")


@main.command()
@click.argument("url")
@click.option("--timeout", default=5.0, show_default=True, type=float)
def ping(url: str, timeout: float) -> None:
    """GET a URL and print the response status."""
    try:
        r = httpx.get(url, timeout=timeout)
    except httpx.HTTPError as exc:
        raise click.ClickException(f"request failed: {exc}") from exc
    click.echo(f"{r.status_code} {r.reason_phrase}")


if __name__ == "__main__":
    main()
