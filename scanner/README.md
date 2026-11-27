# Police scanner

One book per sweep, book0 -> book19, then wraps to book0.
State: pointer.json {"next": N}. Log: scan.log (one line per sweep).
Runs via the `rewrite-polish-scanner` daily cron; each run reviews bookN only,
fixes polish-level issues, pushes under the standing approval, and advances the pointer.


## Branch state and provenance (observed 2026-11-27)

The repository records do not identify which checkout/branch the
`rewrite-polish-scanner` cron uses or where it pushes. Do not treat either
branch's pointer as authoritative until that scheduler configuration is
checked.

At this observation:

- `site-dist/scanner/pointer.json` is `{"next": 2}`; its log ends with a
  clean book1 sweep on 2026-11-27, with the book1 verification and embed
  checks recorded as passing and no fixes pushed.
- `main/scanner/pointer.json` is `{"next": 6}`; its log ends with the
  book5 sweep on 2026-11-11.
- `WORKFLOW.md` specifies a daily sweep but does not name its checkout branch
  or push target. `docs/architecture.md` describes site-dist as a manual
  mirror/snapshot and reports no sync script in this repository tree.

These observations establish that site-dist contains the newer scanner log
snapshot; they do not establish the cron's configured branch, the canonical
state-of-record branch, or the intended synchronization cadence. Resolve
those questions from the registered cron/task definition and its execution
workspace: record the checkout repository and branch, working directory,
remote/push target, and the run's source revision. Until then, report the
branch authority and sync cadence as **unverified**. No scanner behavior or
schedule is changed by this note.
