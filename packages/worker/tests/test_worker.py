# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Chris <goabonga@pm.me>

from worker.main import loop, tick


def test_tick_format_includes_counter_and_version() -> None:
    line = tick(7)
    assert line.startswith("[worker ")
    assert "tick #7" in line


def test_loop_emits_n_ticks_when_capped() -> None:
    seen: list[str] = []
    sleeps: list[float] = []
    n = loop(
        interval_s=0.0,
        iterations=3,
        sleep=lambda s: sleeps.append(s),
        emit=seen.append,
    )
    assert n == 3
    assert seen == [tick(1), tick(2), tick(3)]
    # Every iteration should have called sleep with the configured
    # interval, even when it's zero.
    assert sleeps == [0.0, 0.0, 0.0]
