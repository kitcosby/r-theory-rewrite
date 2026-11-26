# R Theory Codex Pipeline

## Purpose

This directory defines how Codex Desktop monitors and fills the R Theory research pipeline. It adds an operational layer to the existing repository; it does not replace the site's publishing process, validation scripts, research ledgers, external control framework, or mathematical source material.

The canonical repository remains `kitcosby/r-theory-rewrite` on `main`. All work must follow the root `AGENTS.md` and the existing `WORKFLOW.md`.

## Operating model

Codex is the pipeline operator:

1. **Observe** — inspect repository state, recent commits, open and closed issues and pull requests, research notes, validation coverage, bibliography records, and existing automation.
2. **Triage** — identify new, stale, blocked, duplicated, or unowned work.
3. **Discover** — identify specific proof obligations, counterexample opportunities, missing validation, and relevant literature.
4. **Populate** — create GitHub issues for distinct, actionable, evidence-backed work, with explicit deduplication and closure criteria.
5. **Execute** — perform bounded repository tasks on an isolated branch/worktree; implement tests or documentation only within the stated authorization.
6. **Verify** — run relevant checks and record exact evidence without upgrading mathematical status beyond what the checks establish.
7. **Report** — provide a dated operational report, link issues actually created, summarize deduplication, and identify blockers and the next highest-value task.

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

Important: the architecture document describes a static site plus audit tooling, not an already-established general-purpose CI/research scheduler. The existing daily `rewrite-polish-scanner` is a separate process. Do not claim Codex has inherited or replaced it.

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
- Record exact theorem/equation/page/section locations and whether a source supports, contextualizes, competes with, or contradicts the claim.
- Follow the schema and editorial rules in `works-cited/index.html`. Pending leads remain pending.

### C. Pipeline health
- Review open and closed GitHub issues and PRs, stale or blocked tasks, validation coverage, recent commits, unresolved entries in `ISSUE_LOG.md`, and existing automation.
- Detect duplicates before creating new work.
- Give each new issue a specific investigation, affected target, evidence, dependencies, assumptions, priority rationale, and measurable closure criterion.
- Do not manufacture backlog volume.

## Run procedure

1. Check for and use the connected GitHub integration when available. Do not assume a local clone is the only access route.
2. Confirm repository identity, current branch, remote, working-tree status, and latest canonical `main`; preserve uncommitted local work.
3. Inspect recent commits, open and closed issues, open PRs, research and validation records, literature references, and existing automation.
4. Read relevant source records and confirm whether the apparent gap is already addressed elsewhere.
5. Choose worthwhile work based on impact, dependency centrality, and evidence quality.
6. Create GitHub issues for actionable, non-duplicate tasks. Issue creation is authorized without per-issue approval. If an existing record already tracks the work, report it and recommend updating that record instead.
7. Perform only bounded implementation/validation work permitted by `AGENTS.md` and `policy.yml`; use task branches/worktrees and prepare PRs where appropriate.
8. Run relevant checks and record actual outputs, or state why a check could not run.
9. Report actual issue URLs, evidence and classifications, deduplication checks, blockers, inconclusive work, and the next recommended investigation.

## Cadence

Recommended Codex Desktop Automation: **one daily run**, using `prompts/daily-monitor.md`. The prompt defines the run; this repository file does not schedule it. If Codex Automations are unavailable in the installed app, run the same workflow manually. Do not substitute a ChatGPT Scheduled Task or Lampy cron and claim that it is a Codex Desktop Automation.

## Current rollout and authorization

- **Authorized now:** repository monitoring, evidence-based issue creation, deduplication, operational reporting, and bounded task-branch/PR preparation.
- **Not authorized:** direct writes to `main`, PR merges, force-pushes, branch deletion, theorem-status changes, mathematical-source edits, external control-document edits, expensive Lampy computation without explicit authorization and a verified route, or new scheduled services/GitHub Actions/cron.
- **Still requires setup in Codex Desktop:** create the daily Automation using `prompts/daily-monitor.md`. This specification does not create or activate an Automation.
- **Setup scope:** scheduling is per user and workspace in the target Codex Desktop installation; verify the Automation in that exact installation. A ChatGPT Scheduled Task or Lampy cron is a separate scheduler and does not satisfy this Codex Desktop setup step.

## Definition of a useful pipeline item

A useful issue must include:

- a precise question or defect;
- source paths and/or stable external references;
- affected theorem, claim, page, or component;
- existing evidence;
- dependencies and assumptions;
- a proposed investigation;
- a measurable closure criterion;
- an evidence/status classification;
- a duplicate check against issues, PRs, ledgers, research notes, and scanner tasks.

## Report location

Use `templates/run-report.md` for each run. For the first rollout, reports may remain in Codex task output or be attached to a related issue/PR. Do not commit a new daily report for every run; commit durable findings only when they change the project's knowledge state.
