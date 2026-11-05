# Police scanner

The scanner documentation describes a one-book-per-sweep cycle over `book0` through `book19`, then wraps to `book0`. This documented cycle does not establish coverage of Books 20–24.

## Recorded state

- Pointer file: `pointer.json` (currently records `{"next": 10}`).
- Historical log: `scan.log` (latest entry in the inspected file is dated 2026-10-26).
- The log records historical sweeps and review notes; it is not a live scheduler heartbeat.

## Scheduler status

The README previously stated that a daily `rewrite-polish-scanner` cron runs automatically, fixes polish-level issues, pushes changes, and advances the pointer. The repository files inspected for this documentation update do not independently establish whether that scheduler is currently enabled, healthy, or still authorized to push.

**Do not infer that the scanner is active or inactive from the pointer or log alone.** Before relying on automation, verify the scheduler configuration and its latest execution result, then reconcile that result with `pointer.json` and `scan.log`.

## Scope and safety

The documented scanner cycle is limited to Books 0–19. Its historical notes distinguish polish-only edits from mathematical or status changes, which require explicit review. A clean scan or a passing validation script is not a claim that every mathematical statement in a book is correct.
