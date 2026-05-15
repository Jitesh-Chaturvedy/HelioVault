# HelioVault — AI Task Coordination

# Active Tasks

## UI Refinement

Status:
IN PROGRESS

Tasks:

* refine downloads page visual parity
* redesign search results rows
* integrate SVG icons
* reduce Qt-native appearance

Files:

* ui/downloads_page.py
* ui/search_page.py

---

## Download Backend

Status:
PLANNED

Tasks:

* threaded downloads
* pause/resume logic
* queue persistence
* ETA calculation

Files:

* backend/download_manager.py

---

## Data Integration

Status:
PLANNED

Tasks:

* GOES API integration
* SDO integration
* SunPy fetch system

Files:

* backend/data_fetcher.py

---

# Recently Completed

## Dynamic Mission/Instrument System

Completed:

* mission-aware instrument dropdowns
* parameter dropdown generation

Files:

* ui/search_page.py

---

## Download Queue

Completed:

* queue system
* download page integration
* pause/resume UI

Files:

* ui/downloads_page.py
* ui/search_page.py

---

# AI Collaboration Rules

1. Do not rewrite entire architecture without approval.
2. Preserve existing UI philosophy.
3. Avoid default Qt-native appearance.
4. Maintain compact modern design.
5. Commit before major rewrites.
6. Prefer incremental improvements.
7. Respect PROJECT_CONTEXT.md and UI_GUIDELINES.md.

---

# Current Highest Priority

1. Search results redesign
2. SVG icon system
3. Real download backend
4. Metadata integration
