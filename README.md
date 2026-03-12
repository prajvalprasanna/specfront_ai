# Techfront AI - Spec-Driven Copilot Agents

Techfront AI provides a "zero-friction" architecture for **Spec-Driven Development (SDD)** natively inside your GitHub Copilot workspace. By using `.github/agents/*.agent.md` files, this package instantly configures a **Supervisor Agent** and specialized **Worker Agents** (Planner, Coder, Tester) in your IDE, without needing complex LangChain orchestrators or external API keys.

It also includes an integrated **FastMCP Server** to pull context directly from Jira and Figma into your Copilot Chat.

## 🌟 Features

*   **Native Copilot Integration:** Agents live right in your IDE chat. Just type `@techfront_ai`.
*   **Multi-Agent Architecture:** Delegate tasks to specialized personas:
    *   `@techfront_ai` (Supervisor): Orchestrates the workflow and delegates commands.
    *   `@techfront_ai_planner`: Focuses strictly on writing Markdown Specifications and Jira tickets.
    *   `@techfront_ai_coder`: Implements code based *only* on the strict requirements of the spec.
    *   `@techfront_ai_tester`: Writes test suites to prove the spec's Acceptance Criteria are met.
*   **Official MCP Integration:** Automatically generates an `mcp-servers.json` configuration file, securely linking your IDE to the official GitHub, Figma, and Jira Model Context Protocol servers.

---

## 🚀 Installation & Usage

Because Techfront AI is packaged purely as a CLI tool, installation takes seconds.

### 1. Install via PyPI
You can install the package directly into your virtual environment from the Python Package Index once published:

```bash
pip install specfront_ai
```

### 2. Scaffold the Agents
Open your existing application project in VS Code / Cursor. In your terminal, run:

```bash
specfront_ai init
```

*What happens?*
The CLI will instantly generate:
1. The `.github/agents/` prompt files.
2. A `specs/` directory with a sample Hotel Management specification.
3. An `mcp-servers.json` file containing the precise initialization commands for the official GitHub, Jira, and Figma servers.

Copilot will automatically detect these `.agent.md` files—**no restarts needed.**

### 3. Talk to the Agent
Open Copilot Chat and invoke the supervisor:
> `@techfront_ai Hello! I want to start building the Hotel Inventory module.`

Or invoke a specialized agent directly to get to work:
> `@techfront_ai_coder /implement Please read the hotel_inventory.md spec and create the Django models.`

---

## 🔌 Activating the Official MCP Servers

To give your Copilot agents extra superpowers (like reading Jira tickets or inspecting Figma design tokens), you need to provide your exact API keys to the generated `mcp-servers.json`.

1. Open `mcp-servers.json` in your workspace root.
2. Replace the placeholder `<YOUR_GITHUB_TOKEN>`, `<YOUR_JIRA_TOKEN>`, and `<YOUR_FIGMA_TOKEN>` with your actual security tokens.
3. Point your IDE (Cursor, VS Code via Claude Desktop, etc.) to read this configuration file. The IDE will automatically install the servers via `npx` and attach them to your Copilot chats.

---

## 🛠️ Development & Publishing

If you want to contribute to the CLI or publish it to the official PyPI registry:

1.  Read the `pyproject.toml` file to see the build configuration.
2.  Consult `PIP_PACKAGING_GUIDE.md` for exact `build` and `twine` publishing commands.
3. **Daily Updates:** When making everyday updates, remember to **increment the version** in `pyproject.toml` before running `python -m build` and `twine upload dist/*`. See the packaging guide for the full redeployment workflow.