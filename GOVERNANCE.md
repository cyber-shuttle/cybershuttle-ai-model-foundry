# Governance

The Cybershuttle AI Model Foundry is a community-governed project. This document describes how decisions are made, how maintainers are selected, and how the project is organized.

[Principles](#principles) · [Roles](#roles) · [Decision making](#decision-making) · [Working groups](#working-groups) · [Maintainer responsibilities](#maintainer-responsibilities) · [Becoming a maintainer](#becoming-a-maintainer) · [Stepping down](#stepping-down) · [Conflict resolution](#conflict-resolution) · [Amendments](#amendments)

---

## Principles

The Foundry is built on three commitments:

**Vendor neutrality.** NVIDIA, Google, and other partners are helping to contribute optimization profiles, containers, workflows, and benchmark records. Common schemas and interoperability requirements apply to all contributions equally.

**Scientific openness.** The registry exists to serve researchers across all scientific domains. Curation decisions prioritize broad utility, reproducibility, and scientific validity over novelty or vendor preference.

**Community ownership.** Governance, roadmap, and technical direction are determined by active contributors, not by any single organization. Decisions are made in the open, in this repository.

---

## Roles

### Contributor

Anyone who opens an issue, submits a PR, or participates in discussions. No formal process required.

### Reviewer

A contributor who has been granted the ability to review and approve pull requests in one or more areas of the repository. Reviewers are recognized for sustained, high-quality contributions within a specific domain or component.

Reviewers can:
- approve PRs within their area
- request changes and block merges on quality grounds
- participate in technical discussions with elevated weight

Reviewers cannot merge PRs directly, that requires a maintainer.

### Maintainer

Maintainers have merge access and are responsible for the overall health of the project. They review and merge PRs, triage issues, make architectural decisions, and uphold the governance process.

Maintainers are organized into two tiers:

**Domain maintainers** are responsible for a specific registry domain (e.g., biology, chemistry, climate) or infrastructure area (e.g., schemas, workflows, benchmarks). They have merge access scoped to their area.

**Core maintainers** have repository-wide merge access and are responsible for cross-cutting concerns: schema design, the CLI and tooling, governance, and release management. Core maintainers make decisions when domain maintainers cannot reach consensus.

The current maintainer list is kept in [`MAINTAINERS.md`](MAINTAINERS.md).

---

## Decision making

Most decisions happen in pull requests and issues through lazy consensus: if a PR has been open for a reasonable review period (at least 48 hours for minor changes, 5 business days for significant changes) with no substantive objection from a maintainer, it can be merged.

**Minor changes** (documentation fixes, new model entries at `candidate` status, adding benchmark results, fixing typos) require one maintainer approval.

**Significant changes** (new domains, schema modifications, new tooling features, changes to the readiness lifecycle, optimization profile additions from new vendors) require two maintainer approvals and a 5-day review window.

**Major decisions** (changes to governance, changes to the core schema architecture, adding or removing maintainers, significant changes to project scope) require a documented proposal in an issue, a 14-day comment period, and consensus among core maintainers. If consensus cannot be reached, a simple majority vote among core maintainers decides.

Decisions are made in public. Private discussions among maintainers should be reserved for conduct matters.

---

## Working groups

The Foundry may organize working groups around specific domains or technical areas. Working groups are lightweight: they have a stated scope, a named lead, and a place for coordination (typically a GitHub Discussion or issue thread). They do not have separate governance; their output flows through the normal PR and review process.

Current working groups, if any, are listed in [`docs/working-groups.md`](docs/working-groups.md).

Any contributor can propose a working group by opening an issue. Core maintainers approve new working groups.

---

## Maintainer responsibilities

Maintainers are expected to:

- respond to issues and PRs in their area within a reasonable timeframe (aim for 5 business days)
- uphold the quality and consistency standards described in [CONTRIBUTING.md](CONTRIBUTING.md)
- enforce the code of conduct fairly and consistently
- participate in governance discussions
- keep their contact information current in `MAINTAINERS.md`
- give adequate notice before stepping down

Maintainers who are inactive for 3 months without notice may be moved to emeritus status.

---

## Becoming a maintainer

Maintainers are selected from contributors who have demonstrated sustained engagement, good judgment, and familiarity with the relevant part of the codebase or registry.

To nominate someone (including yourself), open an issue tagged `governance` describing the nominee's contributions and proposed scope. Any current maintainer can second the nomination. After a 5-day comment period, core maintainers vote. A simple majority approves.

There is no minimum contribution count. Quality, consistency, and judgment matter more than volume.

---

## Stepping down

Maintainers stepping down should open an issue or contact the core maintainers with reasonable notice so that responsibilities can be transitioned. Emeritus status is recorded in `MAINTAINERS.md` in recognition of past contributions.

---

## Conflict resolution

Technical disagreements should be resolved through discussion in the relevant issue or PR. If a discussion is not converging, any participant can request that core maintainers make a binding decision by commenting and tagging `@core-maintainers`.

Conduct issues should be reported privately to the maintainers listed in `MAINTAINERS.md`. If the issue involves a maintainer, contact a different maintainer or open a confidential report through the mechanism described in the Code of Conduct.

---

## Amendments

Changes to this governance document follow the major decisions process: a documented proposal, a 14-day comment period, and consensus among core maintainers. The rationale for significant changes should be recorded in the commit message or a linked issue for future reference.
