# Police scanner

The documented scanner cycle covers Books 0–19: one book per sweep, then wraps to book0. The published pointer currently records {"next":10}.

## State and provenance

- pointer.json records the next book index.
- scan.log records published sweep entries; the entries currently present end on 2026-10-26.
- This README and the published log do not establish whether an external scheduled job is currently enabled, disabled, or successfully running.
- Confirm the scheduler configuration and recent execution history before describing the scanner as active or stopped.

A log ending on a particular date is not proof that a cron job was disabled. Likewise, a pointer value alone does not establish that a scheduled run completed successfully.

## Scope and safety

The documented cycle is Books 0–19. Do not infer that Books 20–24 are scanned by this cycle unless the scanner configuration and implementation are explicitly extended and verified.

Published logs should distinguish review, proposed edits, completed repository writes, and pointer advancement. A planned or attempted change must not be described as committed unless the repository confirms it.
