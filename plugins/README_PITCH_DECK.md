# Pitch Deck Creator Edtech Skill for EdTech Startups

A sophisticated AI agent skill designed to transform raw text content into visually compelling, investor-ready pitch decks. This tool guides EdTech founders through a 7-phase process—from narrative refinement to wireframing, and finally to professional PowerPoint or Google Slides generation.

## 🚀 Capabilities

*   **Narrative Refinement:** Collaboratively edits pitch content for flow, clarity, and emotional impact using proven frameworks (Hero's Journey, Market-First, etc.).
*   **EdTech Specialization:** Applies specific design and content strategies relevant to the education technology sector (e.g., student outcomes, decision-maker complexity).
*   **Visual Validation:** Moves through three levels of visualization to ensure the design is right before code generation:
    1.  *Text Wireframes* (Layout logic)
    2.  *ASCII Wireframes* (Spatial relationships)
    3.  *HTML Prototypes* (Final design)
*   **Hybrid Output:** Generates editable **PowerPoint (.pptx)** files via Node.js and/or **Google Slides** via API.
*   **Accessibility First:** Automatically checks for WCAG AA contrast compliance and font readability.

## 📋 Prerequisites

To run this skill effectively, your environment needs:

1.  **AI Agent Environment:** An LLM interface capable of file I/O (`Read`, `Write`) and executing shell commands (`Bash`).
2.  **Node.js:** Required for the PowerPoint generation phase.
3.  **Dependencies:**
    *   `pptxgenjs` (will be installed automatically by the skill if missing).
4.  **Resources:**
    *   `resources.md`: Contains design principles and narrative frameworks (included in repo).
    *   `examples/`: A folder containing reference images for visual style.

## 🛠️ Setup & Configuration

### 1. Directory Structure
Ensure your working directory is set up as follows:
```text
/project-root
├── skill.md                # The skill definition file
├── resources.md            # Design & narrative resources
├── content.md              # Your raw pitch deck content
├── examples/               # (Optional) Reference images for style
└── pitch_deck_output/      # (Auto-generated) Output folder
```

### 2. Path Configuration
**Important:** The `skill.md` file contains hardcoded but empty paths for templates and resources. Before using, open `skill.md` and find/replace the following paths to match your local machine:
*  Example templates `/pitch-deck-creator-edtech/examples/`
*  User markdown file containing the content for the pitch deck: `/pitch-deck-creator-edtech/content.md`

### 3. Input Format
Create a markdown file (e.g., `content.md`) following this structure:

```markdown
## SLIDE 1: COVER
**Title:** EdTech Solutions
**Tagline:** The future of learning
**Date:** October 2023

## SLIDE 2: THE PROBLEM
### Teachers are overwhelmed
*   Administrative tasks take 40% of time
*   Burnout rates are at an all-time high
*   Student outcomes are suffering
```

## 🔄 The 7-Phase Workflow

The skill operates in a linear, iterative process:

1.  **Discovery:** The agent gathers requirements (audience, tone, brand colors).
2.  **Content Analysis:** Collaborative editing to improve narrative flow and impact.
3.  **Text Wireframes:** Defining the layout structure (header zones, column splits).
4.  **ASCII Wireframes:** Visualizing spatial relationships and hierarchy in the chat.
5.  **HTML Generation:** Creating high-fidelity HTML/CSS slides using brand colors.
6.  **Visual Preview:** User reviews a generated `slide_preview.html` file.
7.  **Deck Creation:** Final conversion to `.pptx` or Google Slides.

## 💻 Usage

### Trigger Phrases
Start the interaction with the AI using phrases like:
*   "Create a pitch deck for my startup."
*   "Design a presentation from this file."
*   "Help me structure my EdTech pitch."

### Interactive Commands
During the process, you can use commands to guide the agent:
*   **"Approve all"** – Accepts current edits or designs.
*   **"Suggest alternative"** – Requests a different layout or wording.
*   **"Change color to [Hex Code]"** – Adjusts branding on the fly.

## 📦 Output Files

All artifacts are saved to the `./pitch_deck_output/` directory:

| File | Description |
| :--- | :--- |
| `content_refined.md` | The final, edited text content. |
| `wireframes_ascii.txt` | Visual layout text representation. |
| `slideXX_[topic].html` | Individual HTML slide files. |
| `slide_preview.html` | A grid view of all slides for easy review. |
| `[DeckName].pptx` | The final PowerPoint presentation. |

## ⚠️ Troubleshooting

*   **Node.js Errors:** If the PPTX generation fails, ensure Node is installed (`node -v`) and run `npm install pptxgenjs` inside the output directory.
*   **Contrast Warnings:** If the agent warns about contrast, your brand colors likely fail WCAG AA standards. Allow the agent to suggest darker/lighter variants.
*   **Google Slides API:** Requires valid OAuth credentials. If authentication fails, the skill will default to PowerPoint generation.

## 📄 License

MIT License