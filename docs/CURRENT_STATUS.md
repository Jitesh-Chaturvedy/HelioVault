# HelioVault — Current Status

## Current Branch

develop

---

# Current Focus

UI refinement and architecture stabilization.

Current priority:

* make implementation visually match design mockups
* improve visual consistency
* reduce Qt-native appearance

---

# Current Completed Systems

## Search Page

Working:

* date dropdown
* mission dropdown
* instrument dropdown
* parameter dropdown
* mock search
* result generation
* download selection

Needs improvement:

* search results styling
* row/card redesign
* icons
* spacing refinement

---

## Downloads Page

Working:

* stats cards
* filter tabs
* structured download rows
* progress bars
* ETA
* pause/resume toggle
* cancel action
* scrolling layout

Needs improvement:

* SVG icons
* typography polish
* exact mockup parity
* completed/failed states
* actual download backend

---

# Known Issues

* Qt stylesheet inheritance occasionally creates unwanted boxed labels
* UI still partially resembles default Qt layouts
* icon system not implemented yet
* no persistent data storage

---

# Immediate Next Tasks

1. Refine search results UI
2. Add SVG icon system
3. Improve downloads row fidelity
4. Connect real metadata
5. Implement threaded downloads
6. Integrate first real data source (likely GOES)

---

# Git Workflow

Recommended:

* commit before major rewrites
* keep develop branch stable
* use feature branches for experiments

---

# Notes

The project prioritizes:

* UX quality
* workflow simplicity
* visual consistency

before scientific complexity.
