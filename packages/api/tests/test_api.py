# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Chris <goabonga@pm.me>

from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_version_endpoint() -> None:
    r = client.get("/version")
    assert r.status_code == 200
    assert "version" in r.json()


def test_healthz_endpoint() -> None:
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"ok": True}
