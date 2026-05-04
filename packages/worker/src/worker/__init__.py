# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Chris <goabonga@pm.me>

from importlib.metadata import PackageNotFoundError, version


def _resolve_version() -> str:
    try:
        return version("worker")
    except PackageNotFoundError:
        return "0.0.0"


__version__ = _resolve_version()
