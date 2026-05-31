# Contributing to the Cybershuttle AI Model Foundry

Thank you for helping build this resource. Contributions of all kinds are welcome — model requests, execution recipes, resource profiles, optimization profiles, benchmark results, schema changes, documentation, and bug reports.

[Ways to contribute](#ways-to-contribute) · [Before you start](#before-you-start) · [Model requests](#model-requests) · [Registry contributions](#registry-contributions) · [Schema changes](#schema-changes) · [Code and tooling](#code-and-tooling) · [Benchmarks](#benchmarks) · [Documentation](#documentation) · [Pull request process](#pull-request-process) · [Code of conduct](#code-of-conduct)

---

## Ways to contribute

| Type | How |
|---|---|
| Suggest a model | Open an issue using the **Add AI4Science Model** template |
| Add a model entry | Submit a PR adding a `model.yaml` under `registry/models/<domain>/` |
| Add an execution recipe | Submit a PR adding a recipe under the relevant model directory |
| Add a resource profile | Submit a PR under `resource-profiles/` |
| Add an optimization profile | Submit a PR under `optimization-profiles/` |
| Submit benchmark results | Submit a PR under `benchmarks/results/` |
| Change a schema | Edit Pydantic models in `tools/schemas/`, regenerate, submit a PR |
| Fix documentation | Submit a PR editing any `.md` file |
| Report a bug or gap | Open an issue describing the problem |

You don't need to complete an entire model entry to contribute. A partial `model.yaml` with `registry_status: candidate` is a valid and useful starting point.

---

## Before you start

**Check existing issues and PRs first.** Someone may already be working on the model or profile you have in mind. Search open issues before opening a new one.

**For significant changes, open an issue first.** If you're planning a new domain, a schema change, or a major workflow addition, discuss it in an issue before writing code. This saves effort and avoids conflicts.

**Fork and branch.** Work on a feature branch in your fork. Branch names should be descriptive: `add-esm2-biology`, `recipe-molformer-finetune`, `resource-profile-nexus-b200`.

---

## Model requests

The simplest contribution is opening an issue to request a model. Use the **Add AI4Science Model** issue template and include as much as you can:

- model name and scientific domain
- link to the paper, GitHub repo, Hugging Face page, or NGC entry
- intended use: training, fine-tuning, inference, evaluation, or deployment
- expected input datasets
- current hardware and any known bottlenecks
- whether you want to collaborate on developing an optimized workflow

A partial request is still useful. You don't need to know every detail before filing.

---

## Registry contributions

### Adding a model entry

Create a directory under the appropriate domain:

```
registry/models/<domain>/<model-id>/
├── model.yaml
└── recipes/          # optional — add recipes as they are developed
```

The `model.yaml` must validate against the model schema. Include the `$schema` header:

```yaml
# yaml-language-server: $schema=../../../schemas/model.schema.json
id: esm2
name: ESM-2
...
```

Run validation before submitting:

```bash
foundry validate registry/models/biology/esm2/model.yaml
```

Set `registry_status: candidate` if the entry is incomplete. Reviewers will help advance it through the readiness lifecycle.

### Adding an execution recipe

Recipes live alongside the model they belong to:

```
registry/models/<domain>/<model-id>/recipes/<task-name>.yaml
```

Each recipe must specify the task type (inference, fine-tuning, training, evaluation, or deployment), expected inputs and outputs, software dependencies, and compatible resource profiles. Reference the recipe schema:

```yaml
# yaml-language-server: $schema=../../../../schemas/execution_recipe.schema.json
```

### Adding a resource or optimization profile

Resource profiles go under `resource-profiles/<system>/`. Optimization profiles go under `optimization-profiles/<vendor-or-portable>/`. Both must reference their respective schemas and include enough detail for the workflow generator to use them.

---

## Schema changes

Schemas are defined as Pydantic models in `tools/schemas/`. The JSON Schema files in `schemas/` are generated — never edit them directly.

To make a schema change:

```bash
# 1. Edit the relevant Pydantic model in tools/schemas/
# 2. Regenerate
python tools/generate_schemas.py

# 3. Validate that existing registry entries still pass
foundry validate --all

# 4. Update any affected example files
# 5. Submit the PR
```

Schema changes that break existing entries require a migration plan described in the PR. Breaking changes to stable schemas (any entry at `registered` or beyond) need maintainer approval.

---

## Code and tooling

The `tools/` directory contains the `foundry` CLI, schema generation, and workflow utilities. Contributions here follow standard Python conventions:

- Python 3.11 or later
- Type annotations throughout
- Tests under `tools/tests/` using `pytest`
- Formatting with `ruff` and `black`

Run the test suite before submitting:

```bash
cd tools
pip install -e ".[dev]"
pytest
```

---

## Benchmarks

Benchmark results go under `benchmarks/results/`. Each result file must reference the benchmark schema and include at minimum: model ID, resource profile, date, runtime, and peak memory. Science-specific metrics, throughput, cost estimates, and energy estimates are encouraged.

Results should be reproducible. Include enough detail (software versions, batch size, precision, data sample) that someone else could re-run the benchmark and get a comparable result.

---

## Documentation

Documentation lives in `docs/` and in the `README.md` files throughout the repository. Improvements to clarity, accuracy, and coverage are always welcome.

For tutorials and worked examples, follow the structure in `docs/tutorials/`. Each tutorial should be self-contained and runnable.

---

## Pull request process

1. Open a PR against the `main` branch with a clear title and description.
2. Reference any related issues with `Closes #N` or `Related to #N`.
3. Ensure `foundry validate` passes on any modified registry entries.
4. Ensure the test suite passes if you've changed tooling.
5. At least one maintainer review is required before merging.
6. For schema changes or new domains, two maintainer reviews are required.

PRs that add new model entries at `candidate` status can be merged with a single review. More advanced readiness levels require the relevant validation evidence (benchmark records, container references, workflow tests) to be present.

---

## Code of conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you agree to uphold it.

Be respectful and constructive in issues, PRs, and discussions. Disagreements about technical direction are welcome; personal attacks are not.

Report conduct concerns to the maintainers listed in [GOVERNANCE.md](GOVERNANCE.md).
