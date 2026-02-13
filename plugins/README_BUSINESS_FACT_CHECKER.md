# Business Fact-Checker Skill

A specialized Claude skill designed for rigorous verification of business assertions, financial metrics, valuations, and market intelligence. It moves beyond passive information retrieval to active "due diligence" mode.

## Overview

This skill equips Claude with a structured framework for validating business claims. It uses a tiered evidence system (prioritizing SEC filings over news articles) and includes specific checklists for detecting financial engineering, statistical manipulation, and "growth hacking" distortions.

## Capabilities

*   **Financial Verification**: Distinguishes between GAAP metrics (Revenue, Net Income) and non-standard marketing metrics (Bookings, Adjusted EBITDA).
*   **Source Hierarchy**: Automatically weighs evidence based on reliability (Regulatory > Institutional > Trade > Social).
*   **Red Flag Detection**: Identifies common manipulation tactics like "community adjusted" numbers, misleading chart axes, and circular sourcing.
*   **Market Reality Checks**: Validates TAM/SAM/SOM claims against reputable analyst data.

## File Structure

```text
business-fact-checker/
├── SKILL.md                          # Core logic, trigger definitions, and output templates
└── references/
    ├── reliability-tiers.md          # Hierarchy of evidence (SEC vs. Blogs)
    ├── verification-checklists.md    # Step-by-step guides for Revenue, Valuations, etc.
    └── red-flags.md                  # Indicators of misleading data or fraud