# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Chris <goabonga@pm.me>

from click.testing import CliRunner

from cli.__main__ import main


def test_version_command() -> None:
    result = CliRunner().invoke(main, ["version"])
    assert result.exit_code == 0
    # Just check it printed something looking like a version, not the
    # exact value (importlib.metadata returns the installed version,
    # which differs between dev and packaged builds).
    assert result.output.strip()


def test_greet_default() -> None:
    result = CliRunner().invoke(main, ["greet"])
    assert result.exit_code == 0
    assert result.output.strip() == "Hello, world!"


def test_greet_named() -> None:
    result = CliRunner().invoke(main, ["greet", "--name", "Alice"])
    assert result.exit_code == 0
    assert result.output.strip() == "Hello, Alice!"
