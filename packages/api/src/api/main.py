# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Chris <goabonga@pm.me>

from fastapi import FastAPI

from . import __version__

app = FastAPI(title="api")


@app.get("/version")
def get_version() -> dict[str, str]:
    return {"version": __version__}


@app.get("/healthz")
def healthz() -> dict[str, bool]:
    return {"ok": True}


def run() -> None:
    """Console entry point. Defers `uvicorn` import so it only becomes
    a runtime requirement when the binary is actually invoked."""
    import uvicorn

    uvicorn.run("api.main:app", host="0.0.0.0", port=8000)
