# Visual Design Library & Diagrams

Use these ASCII and Mermaid diagrams to illustrate concepts to the user during design critiques or explanations.

## 1. The Core Philosophy
Use this to explain the shift from subjective feelings to objective systems.

```text
SUBJECTIVE (Avoid)           OBJECTIVE (Goal)
"Feels right"                "Measured System"

o                        +-------+-------+
o   o                    |       |       |
  o                      |   A   |   B   |
                         |       |       |
o     o                  +-------+-------+
o                        |       |       |
(Chaos/Vibe)             (Grid/Structure)

## 2. Social Media: Mobile Safe Zones (9:16)

Use this when resizing for Reels, TikTok, or Stories.
code Text

+---------------------------+
|      [System Status]      |
+---------------------------+
| ///////////////////////// | <- Obscured by Top UI
| //                     // |
| //   +-------------+   // |
| //   |  SAFE ZONE  |   // | <- Place "Single Message" Here
| //   +-------------+   // |
| //                     // |
| //           [Like] -> (♥)| <- Obscured by Interaction UI
| ///////////////////////// |
+---------------------------+

## 3. Visual Hierarchy vs. Distance

Use this for Print, Billboard, or Poster design requests.
code Text

VISUAL HIERARCHY / DISTANCE
Dist.   Element size     User Perception

10ft    [ HEADLINE ]     "What is this?" (Hook)
|
5ft     [ Subhead  ]     "Why should I care?"
|
1ft     [ Details  ]     "Where do I go?"

## 4. Strategic Execution: Clarity

Use this to critique cluttered designs.
code Text

BAD DESIGN               GOOD DESIGN
(Cluttered)              (Focused)

+-------------+          +-------------+
| BUY NOW!    |          |             |
| 50% OFF     |          |   50% OFF   |  <-- Single Message
| *terms      |          |             |
| NEW STOCK   |          | [Shop Now]  |  <-- Single Action
| click here  |          |             |
+-------------+          +-------------+

## 5. The Z-Pattern (Scanning Hierarchy)

Use for web landing pages and simple layouts.
code Mermaid

graph TD
    TL[Logo/Brand] -->|Scan| TR[Primary Nav/CTA]
    TR -->|Diagonal Scan| BL[Secondary Info/Image]
    BL -->|Final Action| BR[Ultimate CTA]

## 6. Visual Pacing (Rhythm)

Used in magazines and long-scroll websites to prevent fatigue.
code Text

[   TEXT   ]  [   TEXT   ]   (Dense)
[   IMAGE  ]  [   IMAGE  ]   (Breather)
[   TEXT   ]  [   TEXT   ]   (Dense)

## 7. Types of Balance

Use to explain the difference between formal and dynamic layouts.
code Text

\ | /           [Small]
-- CENTER --       [Small]    [LARGE]
   / | \           [Small]
  (Radial)       (Asymmetrical)

## 8. The "Sea of Gray" (B&W Design Strategy)

Visualizing why high contrast is necessary in text-heavy environments (Newspapers/Docs).
code Text

CONTEXT: THE "SEA OF GRAY"

Paper/Mag Page:
...................................
...text...text...text...text.......
...text...text...text...text.......  <- The eye skips this
...text...text...text...text.......     (Low Contrast)
...................................
.                                 .
.   [ WEAK AD ]     [ STRONG AD ] .
.   (Gray wash)     (High Black)  .
.   ::text:::::     ############# .
.   :::img:::::     ##  WHITE  ## .  <- The eye is drawn here
.   :::::::::::     ##  TEXT   ## .     (High Contrast)
.                   ############# .
...................................