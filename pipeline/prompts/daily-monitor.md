# Codex Desktop Automation — Daily R Theory Pipeline Monitor

Run the R Theory pipeline monitor for the repository `kitcosby/r-theory-rewrite`.

Follow root `AGENTS.md`, `WORKFLOW.md`, and `pipeline/README.md`. Treat this run as monitor-and-propose unless Kit has explicitly enabled a later rollout phase.

## Objectives

1. Inspect the current repository identity, branch, remote, working-tree state, and latest `origin/main`. Preserve any local work; never reset or overwrite it.
2. Review commits since the previous report, open issues, open pull requests, and relevant changes in `research/`, `validation/`, `works-cited/`, and `ISSUE_LOG.md`.
3. Check the existing research and validation records before identifying a gap. Specifically avoid duplicating existing issues, RES-* entries, audit ledgers, scanner tasks, or the existing daily polish scanner.
4. Identify the single most valuable next item across these lanes:
   - verification/proof obligations/counterexamples;
   - primary literature discovery and Works Cited;
   - pipeline health, stalled tasks, and missing coverage.
5. For each candidate, record its source, exact affected claim/page/component, evidence class, dependencies, next action, and closure criterion.
6. Keep literature leads pending until the original source and its relevance have been checked.
7. Do not run expensive computations or contact Lampy unless a verified route and authorization are already documented and available.
8. Do not change theorem statuses, merge PRs, write to main, edit external control documents, or create a scheduled GitHub Action/cron.

## Initial mode

During the initial rollout, do not create issues or modify repository files automatically. Return proposed issues as ready-to-copy drafts and identify any existing issue/PR that should be updated instead. After Kit reviews several reports, the operating policy may be expanded to permit evidence-backed issue creation and task-branch PRs.

## Output

Use `pipeline/templates/run-report.md`. Include:
- run timestamp and commit inspected;
- changes/issues/PRs inspected;
- findings grouped by lane;
- duplicate checks;
- proposed backlog additions or existing records to update;
- blockers and unverified access;
- one recommended next action.

If no worthwhile new work is found, report that plainly. Do not invent work to fill the queue.
