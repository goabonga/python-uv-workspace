# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Chris <goabonga@pm.me>

"""Polling worker stub.

A real worker would dequeue jobs from Redis / RabbitMQ / a database
table; this minimal version just emits one tick per `interval_s`
seconds with a monotonic counter, which is plenty to demonstrate the
multi-component versioning and release pipeline.
"""

from __future__ import annotations

import time
from collections.abc import Callable

from . import __version__


def tick(counter: int) -> str:
    """Render a single tick line. Pure function for ease of testing."""
    return f"[worker {__version__}] tick #{counter}"


def loop(
    *,
    interval_s: float = 5.0,
    iterations: int | None = None,
    sleep: Callable[[float], None] = time.sleep,
    emit: Callable[[str], None] = print,
) -> int:
    """Run the worker loop, emitting one tick line per iteration.

    `iterations` caps the loop for tests / dry-runs. `sleep` and `emit`
    are dependency-injected to keep the test fully synchronous and
    silent.
    """
    counter = 0
    while iterations is None or counter < iterations:
        counter += 1
        emit(tick(counter))
        sleep(interval_s)
    return counter


def run() -> None:  # pragma: no cover
    """Console entry point. Runs forever."""
    loop()
