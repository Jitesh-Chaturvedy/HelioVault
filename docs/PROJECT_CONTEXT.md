# HelioVault — Project Context

## Overview

HelioVault is a modern desktop application for unified solar data acquisition, browsing, downloading, and later analysis.

The primary goal of the project is to simplify the fragmented ecosystem of solar physics data tools, websites, and satellite archives into a single cohesive user experience.

Current tools in the solar data ecosystem often require:

* multiple websites
* inconsistent UI structures
* different APIs
* custom scripts
* SunPy/Astropy knowledge
* manual FITS handling
* repetitive workflows

HelioVault aims to unify these workflows into a modern, intuitive desktop application.

---

# Core Philosophy

HelioVault prioritizes:

* simplicity
* visual clarity
* cohesive workflows
* modern UI/UX
* minimal technical friction
* discoverability of solar missions/instruments
* fast data acquisition

The project intentionally avoids classic scientific-software aesthetics and instead follows a modern product-oriented design language.

---

# Initial Scope (V1)

Version 1 focuses primarily on:

## Solar Data Acquisition

Features:

* date-based search
* mission selection
* instrument/product selection
* parameter filtering
* search results browsing
* bulk selection
* download queue management
* download monitoring

NOT included yet:

* advanced analysis
* FITS visualization
* flare detection
* image processing
* scientific plotting
* AI analysis

These will come later.

---

# Long-Term Vision

Future versions may include:

* FITS preview
* ROI cropping
* flare analysis
* magnetic field analysis
* image alignment
* animation generation
* integrated SunPy workflows
* metadata inspection
* batch processing
* scripting support
* plugin system

---

# Technology Stack

## Frontend

* Python
* PySide6 (Qt for Python)

## Backend

* Python
* SunPy
* Astropy

## Initial OS Target

* Windows

Future:

* Linux
* macOS

---

# Current Architecture

## Main Application Structure

Pages:

* SearchPage
* DownloadsPage
* LibraryPage (placeholder)
* SettingsPage (placeholder)

Main layout:

* sidebar navigation
* stacked page system

---

# Search Workflow

Current workflow:

1. Select Date
2. Select Mission
3. Select Instrument/Product
4. Optional Parameters appear dynamically
5. Search
6. Select Results
7. Download Selected

---

# Current Supported Missions (Mock Data)

Currently mocked:

* GOES
* SDO
* Hinode
* IRIS
* SOHO
* Solar Orbiter
* Parker Solar Probe
* STEREO

Mission/instrument relationships are dynamically linked.

---

# Current UI Philosophy

The UI language is extremely important.

HelioVault follows:

* rounded corners
* soft modern UI
* compact spacing
* subtle borders
* clean typography
* minimal clutter
* Bootstrap-inspired density
* modern desktop-app aesthetics

The UI should NOT resemble:

* traditional Qt desktop apps
* old scientific software
* spreadsheet-heavy interfaces

---

# Search Results Philosophy

Search results should visually behave more like:

* modern file managers
* cloud dashboards
* browser downloads

NOT:

* spreadsheet applications

---

# Downloads Page Philosophy

Downloads page should:

* show active download state clearly
* remain compact and readable
* include:

  * progress
  * ETA
  * mission/instrument
  * file size
  * actions

Action model:

* Pause ↔ Resume
* Cancel
* Open Folder

Inspired by browser download managers.

---

# Current Development State

Implemented:

* sidebar navigation
* page switching
* dynamic mission/instrument dropdowns
* parameter dropdowns
* mock search results
* download queue
* compact downloads layout
* pause/resume UI logic
* download statistics cards
* filter tabs
* custom styling
* Git version control workflow

Not implemented yet:

* real API integration
* actual downloads
* threading
* file persistence
* FITS handling
* metadata extraction
* dark mode
* SVG icon system

---

# Development Workflow

The project uses:

* Git
* feature iteration
* checkpoint commits
* branch-based experimentation

Recommended workflow:

* commit before major UI rewrites
* test AI-generated code incrementally
* maintain UI consistency
* avoid uncontrolled architecture rewrites

---

# Role Structure

Project direction:

* Human-led product vision

AI roles:

* architecture assistance
* UI implementation
* debugging
* styling refinement
* refactoring support

The human remains the final authority for:

* product direction
* UI consistency
* workflow decisions
* feature prioritization
