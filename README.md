# Custom Claude Skills Marketplace

A curated collection of custom plugins, agents, and tools designed for the Claude Desktop App. This repository hosts a **Marketplace** that allows you to easily install and manage specific AI skills.

## 🚀 Quick Start

To add this marketplace to your Claude Desktop environment, simply type the following command into any Claude chat window:

```bash
/plugin marketplace add beerspitnight/cc-skills
```

Once the marketplace is added, you can browse and install individual plugins using the `/plugin install` command or via the settings menu.

## 📦 Available Plugins

| Plugin Name | Version | Description |
| :--- | :--- | :--- |
| **Pitch Deck Creator Edtech** | `1.1.0` | specialized agent that transforms raw text into investor-ready PowerPoint & Google Slides presentations. Includes wireframing and narrative refinement. |
| *(More coming soon)* | | |

## 🛠️ Plugin Details

### Pitch Deck Creator Edtech (EdTech Focus)
A powerful tool for founders. It takes markdown content and runs a 7-phase design process to generate `.pptx` files.

**Prerequisites:**
*   **Node.js** (Required for PowerPoint generation)
*   Run `node -v` in your terminal to ensure it is installed.

**Installation:**
```bash
/plugin install pitch-deck-creator-edtech
```

**Usage:**
> "Create a pitch deck for my startup based on the attached `content.md` file."

## 📂 Repository Structure

For developers or those curious about the source code, the repository is organized as follows:

```text
beerspitnight/cc-skills/
├── .claude-plugin/
│   └── marketplace.json               # The Marketplace Catalog definition
├── plugins/
│   └── pitch-deck-creator-edtech/     # Source code for the Pitch Deck tool
│       ├── plugin.json                # Plugin Manifest
│       ├── skill.md                   # Agent Logic & Prompts
│       └── resources/                 # Assets and Templates
└── README.md                          # You are here
```

## 🤝 Contributing

Contributions are welcome! If you have a new skill idea or an improvement for an existing one:

1.  Fork this repository.
2.  Create a new folder under `plugins/` for your tool.
3.  Add a `plugin.json` manifest (ensure `strict: true`).
4.  Submit a Pull Request.

## 📄 License

[MIT](LICENSE) © Bruno
