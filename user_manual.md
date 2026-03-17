# Specfront AI: User Manual & Feature Guide

Welcome to **Specfront AI**, your Spec-Driven Development (SDD) multi-agent operating system integrated directly into your IDE via GitHub Copilot. 

Specfront AI transforms your IDE from a basic auto-complete tool into a highly structured, role-based software development team. By leveraging a centralized context repository (the `.spec` directory) and a suite of specialized AI agents, Specfront ensures that your code is secure by default, aligned with your business requirements, and moves at the speed of AI without inheriting AI risk.

---

## 1. Zero-Friction Setup

### Installation
Install the package globally or within your project:
```bash
pip install specfront_ai
```

### Initialization
Initialize the architecture at the root of your project:
```bash
specfront_ai init
```

This command automatically scaffolds the entire AI nervous system in your repository. **No extra user setup is required.** Just add your necessary API keys to your `.env` file, and the agents will automatically configure themselves to connect to the MCP servers and read your workspace.

### The `@` Pop-Up Integration
Specfront AI integrates directly into your editor's natural workflow. You do not need a separate chat window. Simply type `@` in your standard Copilot chat interface or inline chat, and all Specfront agents will appear in the pop-up menu. You can quickly select the desired agent using your mouse or keyboard and immediately continue typing your prompt.

---

## 2. The Specfront AI Team (Role-Based Agents)

To avoid confusing the developer with hundreds of overlapping agents, Specfront AI distills the AI team down to **6 core personas**. 

#### 👑 `@specfront-ai` (The Autonomous Supervisor)
The overarching orchestrator. It acts as your autonomous technical lead. When you have a high-level goal, the supervisor coordinates the workflow, delegates to the specialized agents, and ensures the `.spec` constitution is followed.

#### 📝 `@specfront-ai-planner` (The Product Owner)
Used strictly for writing, formatting, and organizing Markdown specifications, architectural plans, or Jira tickets. It translates loose ideas into rigorous Acceptance Criteria and structured `.md` files.

#### 🎨 `@specfront-ai-frontend` (The UI Developer)
Handles everything client-side (HTML, React, CSS, Vue, etc.). It reads from the `specs/` directory and implements the visual components exactly as defined in the API contracts.

#### ⚙️ `@specfront-ai-backend` (The Backend Engineer)
Handles servers, APIs, databases, and core business logic. It ensures that the implemented data models match the API contracts defined in `.spec/memory/`.

#### 🧪 `@specfront-ai-tester` (The QA Engineer)
Writes unit, integration, and End-to-End tests based *only* on the Acceptance Criteria. It proves features work rather than writing the features themselves.

#### 🚀 `@specfront-ai-deployer` (The DevOps Engineer)
Focuses on CI/CD pipelines, Dockerfiles, cloud infrastructure, and deployment scripts.

---

## 3. The `.spec` Architecture: The Project's Brain

Similar to standard developer tool configurations (like `.github` or `.vscode`), the `.spec` directory is the central nervous system for your agents. Agents rely on this directory to understand the specific context, rules, and scripts of your project.

### Feature 1: Explicit Memories (`.spec/memory/`)
Instead of rewriting prompts every time, store your core rules here.
*   `constitution.md`: The absolute rules your agents must follow globally (e.g., "always use TypeScript", "prefer functional components").
*   `api-contracts.md`: The single source of truth for your data structures and endpoints. Agents use this to ensure the frontend and backend align.

### Feature 2: PowerShell Scripts & Automation (`.spec/scripts/powershell/`)
Store automation scripts here. Your agents are aware of these scripts and will proactively recommend executing them to accelerate your SDLC. 
*   *Example*: A `scaffold-component.ps1` script to quickly generate boilerplate code, which the `@specfront-ai-frontend` agent can invoke upon request.

### Feature 3: Standardized Prompts and Templates (`.spec/templates/`)
Keep your documentation uniform. The Planner agent uses these Markdown templates to generate new designs or specifications, ensuring every feature request follows the exact same structure across your organization.

### Feature 4: Pre-defined Prompts (`.spec/prompts/`)
Save time by storing your frequently used AI prompts here. You can quickly access them in Copilot chat using the `/` key just like memory or templates. 
*   *Example*: A `refactor-prompt.md` to instantly apply your custom architectural guidelines to a piece of code.

### Feature 5: Sub-directory Organization
Your workspace is kept clean. The agent files themselves (`*.agent.md`) can be organized in subdirectories like `@planning`, `@frontend`, `@backend` inside your `.github/agents` folder to ensure logical grouping.

---

## 4. The CT-MCP Security Layer ("Shift-Left" Security)

**The Problem**: 40% of AI-generated code contains vulnerabilities because traditional security tools operate "post-commit" (detect-fix-deploy risk).
**The Solution**: "Prevent-Verify-Trust" via the **Security Context Injector**.

### How it Works:
1. **Context Retrieval via MCP**: When you send a prompt to any Specfront agent (e.g., "Create a login endpoint"), the agent first intercepts the request and connects to the **Model Context Protocol (MCP)** servers.
2. **Context Injection**: The MCP server dynamically fetches security compliance rules relevant to the prompt (e.g., HIPAA compliance rules, parameterized query requirements, mandatory password hashing).
3. **Secure Generation**: These security rules are injected invisibly into the context window *before* the code is generated. 
4. **The Result**: The AI generates code that is "secure by default". You move at AI speed without inheriting technical debt or security friction.

---

## 5. Accelerating the SDLC Workflow

By combining the specialized agents, the `.spec` context, and the MCP security layer, your Software Development Life Cycle (SDLC) is radically accelerated:

1. **Plan**: Use `@specfront-ai-planner` to create a new feature spec in `specs/`. It uses your templates automatically.
2. **Secure Context**: The MCP layer ensures the spec inherently accounts for compliance (e.g., HIPAA).
3. **Backend Impl**: Ask `@specfront-ai-backend` to implement the spec. It reads your `.spec/memory/api-contracts.md` and generates secure, compliant routing.
4. **Frontend Impl**: Ask `@specfront-ai-frontend` to build the UI based on the same API contract.
5. **Verify**: Use `@specfront-ai-tester` to generate a test suite.
6. **Deploy**: Use `@specfront-ai-deployer` to containerize the application.

All while relying on `.spec/scripts/powershell` to automate the mundane glue tasks in between!
