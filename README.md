# Route Window Lab

A Python transit-reporting project for testing API Guardian on a real package upgrade. Given an ordered list of stops, the CLI counts contiguous paths and reports loops. The library also reports travel times, passenger loads and fare-zone crossings.

The initial commit deliberately pins `more-itertools==5.0.0`. The application calls **10 public functions** from that distribution. One of those functions, `substrings`, drops its optional `join_func` argument by version 11.2.1. Four modules each pass the retired argument at six different call sites, for **24 independently tested migration issues**. The other nine functions supply the route overview. API Guardian V1 prepares a PR for one analyzed dependency and one breaking change per run.

## Run the application

Use Python 3.11 or newer. From this repository:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -e . pytest
route-window A B A
python -m pytest -q
```

The example produces six contiguous paths and one loop, A → B → A.

| Condition | Expected test result |
|---|---|
| Original pin, original source | 26 pass |
| Upgrade to 11.2.1 with the old calls intact | 24 fail on the obsolete argument, 2 pass |
| Upgrade and repair every affected call | 26 pass |

The 24 cases have separate pytest IDs. A patch that skips even one report leaves a corresponding failure. The two overview tests cover the unaffected operations.

## Upload your test repository

From this checkout, push its baseline commit to a new repository under your GitHub account. For example, with an authenticated GitHub CLI:

```sh
gh repo create Route-Window-Lab --private --source=. --remote=origin --push
git remote get-url origin
```

The baseline includes the hidden `.api-guardian/` directory. Uploading that directory with the project lets Core resolve both provider versions from a GitHub checkout.

## Run API Guardian against GitHub

Run these commands in an environment where the API Guardian CLI is installed. Replace the account name with yours.

```sh
REPO_URL=https://github.com/YOUR_ACCOUNT/Route-Window-Lab.git
api-guardian repair --repo "$REPO_URL" --github-token-env GITHUB_TOKEN
```

For a private repository, export `GITHUB_TOKEN` locally with access to that repository. For a public read-only preflight you can omit the token flag. An analysis run should report one removed parameter and 24 affected locations across stops, timing, demand and zones.

To test model-generated repair and draft PR publication, run the following from the **API Guardian Core checkout**. The CLI uses `OPENAI_API_KEY` and `GITHUB_TOKEN` from your environment. Choose a model available to your account that supports the Core planner’s Chat Completions JSON request. The GitHub token needs repository contents and pull-request write permissions. The host needs a running local Docker daemon.

```sh
docker build -t api-guardian-validator:local - < benchmark/Dockerfile.validation
api-guardian repair --repo "$REPO_URL" \
  --model "${MODEL:?set MODEL to your repair model}" --model-token-env OPENAI_API_KEY \
  --validation-image api-guardian-validator:local \
  --github-token-env GITHUB_TOKEN --publish \
  --output-dir /tmp/route-window-runs
```

A successful publication returns a draft PR URL. Review the version pin, all four production modules and the test result. Core checks PyPI for the current latest stable release before preparing a candidate. If PyPI has moved past 11.2.1, the offline comparison still works; a verified declaration and provider for the new target will be needed for a live repair.

## Release evidence

The registry uses a small Git bundle so both provider snapshots travel with this repository. It contains the original, digest-verified Python runtime sources and upstream license, plus locally authored setuptools descriptors and declarations covering the ten functions used here. The tags inside the bundle identify these fixture snapshots. The old release requires six; the target has no runtime dependency. Source archive URLs, SHA-256 hashes, declaration source lines, local commit IDs and the PyPI lookup time are in the [provenance record](.api-guardian/provenance.json).
