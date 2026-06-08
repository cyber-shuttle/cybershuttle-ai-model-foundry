# Security policy

## Supported versions

The Cybershuttle AI Model Foundry is currently in early development. Security fixes
are applied to the `main` branch only.

| Version | Supported |
| ------- | --------- |
| main    | ✅ Yes    |

## Reporting a vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Please report security concerns privately by emailing the core maintainers listed
in [MAINTAINERS.md](MAINTAINERS.md). Include:

- a description of the vulnerability and its potential impact
- steps to reproduce or a proof-of-concept (if available)
- any suggested mitigations you are aware of

You will receive an acknowledgement within 5 business days. We will work with you
to understand and address the issue before any public disclosure.

## Scope

This policy covers:

- schema definitions and generated JSON Schema files in `schemas/`
- the `foundry` CLI and tooling in `tools/`
- GitHub Actions workflows in `.github/workflows/`
- registry content that could be used to supply malicious container references
  or execution recipes

Registry metadata (YAML files in `registry/`) that references external resources
(containers, datasets, model weights) is community-contributed. Users are
responsible for verifying the integrity of external resources before use.

## Deployment disclaimer

Registry entries and execution recipes are provided as reference and are not
guaranteed to be secure in all deployment environments. When running models on
production cyberinfrastructure, review container sources, validate checksums,
and follow your institution's security policies.
