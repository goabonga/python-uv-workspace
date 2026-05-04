# python-uv-workspace

A uv workspace shipping three independent Python packages — an HTTP
api, a click CLI, and a polling worker — each versioned and released
on its own cadence by [`multicz`](https://github.com/goabonga/multicz).

```
.
├── pyproject.toml          uv workspace root (pytest + ruff + dev deps)
├── multicz.toml            three components, three tag streams
└── packages/
    ├── api/                FastAPI — /version, /healthz
    ├── cli/                click CLI — version, greet, ping
    └── worker/             polling worker — tick every interval_s
```

## Setup

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
git clone https://github.com/goabonga/python-uv-workspace
cd python-uv-workspace
uv sync                      # installs every workspace member + dev deps
uv run pytest                # runs all 9 tests across the 3 packages
```

## Run each package

```bash
uv run --package api    api       # FastAPI on :8000
uv run --package cli    cli greet --name Alice
uv run --package worker worker    # ticks until interrupted
```

## Independent versions, independent tags

```toml
# multicz.toml
[components.api]
paths      = ["packages/api/**"]
bump_files = [{ file = "packages/api/pyproject.toml", key = "project.version" }]
changelog  = "packages/api/CHANGELOG.md"
post_bump  = ["uv lock"]
# ... idem for cli and worker
```

`feat(api): ...` bumps `api` and tags `api-vX.Y.Z`. A scope-less
`feat: ...` bumps every component whose paths see the change (default
`bump_policy = "as-commit"`).

```bash
uv run multicz status              # plan in a table
uv run multicz changed             # CI matrix gating
uv run multicz bump --commit --tag # write versions, commit, tag
```

## Release flow

`.github/workflows/release.yml` runs after the `ci` workflow finishes
green on `main`:

1. `multicz plan` — exit cleanly if nothing pending
2. `multicz bump --commit --tag --push` — writes the bumped versions,
   regenerates `uv.lock` (`post_bump`), commits, tags, pushes
3. `multicz release-notes --all` — markdown notes per component
4. `gh release create <tag>` per bumped tag

CI itself uses `multicz changed --output json` to drive a per-package
matrix so PR builds only test what actually moved.

## License

[MIT](LICENSE).
