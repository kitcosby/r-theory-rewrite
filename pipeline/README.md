# R Theory Codex Pipeline

## Purpose

This directory defines how Codex Desktop monitors and fills the R Theory research pipeline. It adds an operational layer to the existing repository; it does not replace the site's publishing process, validation scripts, research ledgers, external control framework, or mathematical source material.

The canonical repository remains `kitcosby/r-theory-rewrite` on `main`. All work must follow the root `AGENTS.md` and the existing `WORKFLOW.md`.

## Operating model

Codex is the pipeline operator:

1. **Observe** — inspect repository state, recent commits, open issues and pull requests, research notes, validation coverage, and bibliography records.
2. **Triage** — identify new, stale, blocked, duplicated, or unowned work.
3. **Discover** — identify specific proof obligations, counterexample opportunities, missing validation, and relevant literature.
4. **Populate** — create or update a backlog issue only when the item is distinct, actionable, evidence-backed, and has a closure criterion.
5. **Execute** — perform bounded repository tasks on an isolated branch/worktree; implement tests or documentation where authorized.
6. **Verify** — run relevant checks and record exact evidence without upgrading mathematical status beyond what the checks establish.
7. **Report** — leave a dated operational report and identify the next highest-value task.

## Responsibilities and boundaries

| System | Responsibility |
|---|---|
| Codex Desktop | Repository monitoring, intake, triage, bounded implementation, tests, branch/PR preparation, operational reporting |
| GitHub | Canonical code/document history, issues, pull requests, review trail |
| Lampy (WSL2) | Persistent computational environment, only when connectivity and authorization are verified |
| Existing validation scripts | Claim-level executable checks and structural tests already defined by the project |
| ChatGPT / human review | Mathematical scrutiny, interpretation, prioritization, and review of consequential claims or changes |

Codex must not describe itself as an independent mathematical verifier merely because it authored or ran code. Software correctness, reproducibility, computational evidence, and mathematical proof are distinct.

## Repository-specific sources

Read these before making pipeline decisions:

- `README.md` — current site and repository scope.
- `WORKFLOW.md` — mathematical honesty, source boundaries, audit and publishing rules.
- `docs/architecture.md` — observed architecture and known limitations.
- `ISSUE_LOG.md` — dated repository findings and closure criteria.
- `validation/README.md` — documented validation coverage and its boundary.
- `works-cited/index.html` — bibliography structure and literature-review policy.
- `scanner/README.md` — existing polish scanner; do not duplicate or silently repurpose it.

Important: the repository's architecture document describes a static site plus audit tooling, not an already-established general-purpose CI/research scheduler. The existing daily `rewrite-polish-scanner` is a separate process. Do not claim that Codex has inherited or replaced it.

## Work lanes

Rotate according to evidence and current bottlenecks; do not force a lane when there is no worthwhile work.

### A. Verification
- Identify claims with missing assumptions, incomplete proofs, or untested edge cases.
- Locate the exact source statement and its dependencies.
- Propose minimal decisive counterexample searches or executable checks.
- Preserve CP/SC/NC/ST/MA/AX/IN/IC labels and their existing definitions.
- Record timeouts and failures as incomplete/failed evidence.

### B. Literature
- Search for primary papers, authoritative standards, datasets, and original documentation relevant to an identified claim.
- Verify metadata and inspect the underlying source, not only search snippets or AI summaries.
- Record exact locators and whether a source supports, contextualizes, competes with, or contradicts the claim.
- Follow the schema and editorial rules in `works-cited/index.html`. Pending leads remain pending.

### C. Pipeline health
- Review open GitHub issues and PRs, stale or blocked tasks, validation coverage, recent commits, and unresolved entries in `ISSUE_LOG.md`.
- Detect duplicates before creating new work.
- Give each new task a specific owner/next action where possible, evidence, priority rationale, dependencies, and closure criterion.
- Do not manufacture backlog volume.

## Run procedure

1. Confirm repository identity, branch, remote, and working-tree status.
2. Fetch/inspect current `origin/main`; do not overwrite local work.
3. Inspect open issues and PRs and changes since the last recorded run.
4. Read relevant source records and confirm whether the apparent gap is already addressed elsewhere.
5. Choose the highest-value lane based on impact, dependency centrality, and evidence quality.
6. Either:
   - record a finding in the operational report;
   - create/update one or more justified GitHub issues;
   - or implement a bounded change on a task branch and prepare a PR.
7. Run relevant tests and record actual outputs.
8. Leave a report using `templates/run-report.md`.

## Cadence

Recommended initial Codex Desktop Automation: **one daily run**, with the prompt in `prompts/daily-monitor.md`. Start in monitor-and-propose mode. After several successful runs and review of false positives, selectively enable issue creation and low-risk branch/PR work.

If Codex Automations are unavailable in the installed app, run the same prompt manually. Do not substitute a ChatGPT Scheduled Task or a Lampy cron and claim that it is a Codex Desktop Automation.

## Current rollout phases

1. **Phase 1 — Instructions and read-only discovery:** root `AGENTS.md`, this runbook, and a daily monitor prompt.
2. **Phase 2 — Controlled intake:** create evidence-backed issues and maintain deduplication.
3. **Phase 3 — Bounded execution:** task branches/worktrees, reproducible tests, and draft PRs.
4. **Phase 4 — Verified external computation:** only after a secure, documented Codex-to-Lampy route is tested.
5. **Phase 5 — Expanded automation:** only after reviewing reports, permissions, failure handling, and resource limits.

No GitHub Actions workflow, Lampy service, database integration, or external scheduler is installed by this specification.

## Definition of a useful pipeline item

A useful item must include:

- a precise question or defect;
- source paths and/or stable external references;
- affected theorem, claim, page, or component;
- evidence already available;
- dependencies and assumptions;
- a proposed next action;
- a closure criterion;
- a status/evidence classification;
- duplicate check against issues, PRs, ledgers, and research notes.

## Report location

For the first rollout, place reports in Codex's task output or attach them to the related GitHub issue/PR. Do not commit a new daily report for every run: that creates repository noise. Commit durable findings only when they change the project's knowledge state.
