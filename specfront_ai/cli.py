import logging
import argparse
import sys
import os
from pathlib import Path

# Setup basic logging for the CLI
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("specfront_ai.cli")

def init_workspace():
    from .templates import (
        AGENT_TEMPLATE, PLANNER_TEMPLATE, FRONTEND_TEMPLATE,
        BACKEND_TEMPLATE, TESTER_TEMPLATE, DEPLOYER_TEMPLATE,
        SPEC_TEMPLATE, MCP_SERVERS_JSON_TEMPLATE,
        API_CONTRACTS_TEMPLATE, CONSTITUTION_TEMPLATE,
        COMMON_PS1_TEMPLATE, CHECK_PREREQUISITES_PS1_TEMPLATE,
        CREATE_NEW_FEATURE_PS1_TEMPLATE, CREATE_NEW_SPEC_PS1_TEMPLATE,
        SETUP_PLAN_PS1_TEMPLATE, UPDATE_AGENT_CONTEXT_PS1_TEMPLATE,
        API_CONTRACTS_TPL_TEMPLATE, CONSTITUTION_TPL_TEMPLATE,
        DESIGN_TEMPLATE_TEMPLATE, TASKS_TEMPLATE_TEMPLATE,
        REFACTOR_PROMPT_TEMPLATE, CODE_REVIEW_PROMPT_TEMPLATE,
        SECURITY_COMPLIANCE_TEMPLATE,
        SPECFRONT_AI_ANALYZE_TEMPLATE,
        SPECFRONT_AI_API_CONTRACTS_TEMPLATE,
        SPECFRONT_AI_CLARIFY_TEMPLATE,
        SPECFRONT_AI_CODER_TEMPLATE,
        SPECFRONT_AI_CONSTITUTION_TEMPLATE,
        SPECFRONT_AI_DESIGN_TEMPLATE,
        SPECFRONT_AI_DESIGNTOKENS_TEMPLATE,
        SPECFRONT_AI_HTML_TEMPLATE,
        SPECFRONT_AI_IMPLEMENT_TEMPLATE,
        SPECFRONT_AI_TASKS_TEMPLATE
    )
    
    logger.info("Initializing specfront_ai workspace with multi-agent setup...")
    current_dir = Path.cwd()
    
    # Create .github/agents directory
    agent_dir = current_dir / ".github" / "agents"
    agent_dir.mkdir(parents=True, exist_ok=True)
    logger.debug(f"Ensured directory exists: {agent_dir}")
    
    agents_to_create = {
        "specfront-ai.agent.md": AGENT_TEMPLATE,
        "specfront-planner.agent.md": PLANNER_TEMPLATE,
        "specfront-frontend.agent.md": FRONTEND_TEMPLATE,
        "specfront-backend.agent.md": BACKEND_TEMPLATE,
        "specfront-tester.agent.md": TESTER_TEMPLATE,
        "specfront-deployer.agent.md": DEPLOYER_TEMPLATE,
        "specfront-ai-analyze.agent.md": SPECFRONT_AI_ANALYZE_TEMPLATE,
        "specfront-ai-api-contracts.agent.md": SPECFRONT_AI_API_CONTRACTS_TEMPLATE,
        "specfront-ai-clarify.agent.md": SPECFRONT_AI_CLARIFY_TEMPLATE,
        "specfront-ai-coder.agent.md": SPECFRONT_AI_CODER_TEMPLATE,
        "specfront-ai-constitution.agent.md": SPECFRONT_AI_CONSTITUTION_TEMPLATE,
        "specfront-ai-design.agent.md": SPECFRONT_AI_DESIGN_TEMPLATE,
        "specfront-ai-designtokens.agent.md": SPECFRONT_AI_DESIGNTOKENS_TEMPLATE,
        "specfront-ai-html.agent.md": SPECFRONT_AI_HTML_TEMPLATE,
        "specfront-ai-implement.agent.md": SPECFRONT_AI_IMPLEMENT_TEMPLATE,
        "specfront-ai-tasks.agent.md": SPECFRONT_AI_TASKS_TEMPLATE,
    }

    for filename, content in agents_to_create.items():
        agent_file = agent_dir / filename
        if not agent_file.exists():
            with open(agent_file, "w", encoding="utf-8") as f:
                f.write(content)
            logger.info(f"Created agent definition: {filename}")
        else:
            logger.warning(f"Agent {filename} already exists. Skipping.")

    # Create .spec architecture
    spec_structure = {
        ".spec/memory": {
            "api-contracts.md": API_CONTRACTS_TEMPLATE,
            "constitution.md": CONSTITUTION_TEMPLATE
        },
        ".spec/prompts": {
            "refactor-prompt.md": REFACTOR_PROMPT_TEMPLATE,
            "code-review-prompt.md": CODE_REVIEW_PROMPT_TEMPLATE
        },
        ".spec/security": {
            "compliance-rules.md": SECURITY_COMPLIANCE_TEMPLATE
        },
        ".spec/scripts/powershell": {
            "common.ps1": COMMON_PS1_TEMPLATE,
            "check-prerequisites.ps1": CHECK_PREREQUISITES_PS1_TEMPLATE,
            "create-new-feature.ps1": CREATE_NEW_FEATURE_PS1_TEMPLATE,
            "create-new-spec.ps1": CREATE_NEW_SPEC_PS1_TEMPLATE,
            "setup-plan.ps1": SETUP_PLAN_PS1_TEMPLATE,
            "update-agent-context.ps1": UPDATE_AGENT_CONTEXT_PS1_TEMPLATE
        },
        ".spec/templates": {
            "api-contracts-template.md": API_CONTRACTS_TPL_TEMPLATE,
            "constitution-template.md": CONSTITUTION_TPL_TEMPLATE,
            "design-template.md": DESIGN_TEMPLATE_TEMPLATE,
            "tasks-template.md": TASKS_TEMPLATE_TEMPLATE
        }
    }

    for dir_path, files in spec_structure.items():
        target_dir = current_dir / dir_path
        target_dir.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Ensured directory exists: {target_dir}")
        for filename, content in files.items():
            target_file = target_dir / filename
            if not target_file.exists():
                with open(target_file, "w", encoding="utf-8") as f:
                    f.write(content)
                logger.info(f"Created spec file: {dir_path}/{filename}")
            else:
                logger.warning(f"Spec file {dir_path}/{filename} already exists. Skipping.")

    # Create specs directory
    specs_dir = current_dir / "specs"
    specs_dir.mkdir(parents=True, exist_ok=True)
    logger.debug(f"Ensured directory exists: {specs_dir}")
    
    spec_file = specs_dir / "01_hotel_inventory.md"
    if not spec_file.exists():
        with open(spec_file, "w", encoding="utf-8") as f:
            f.write(SPEC_TEMPLATE)
        logger.info(f"Created sample spec at: {spec_file}")
    else:
        logger.warning(f"Sample spec already exists at: {spec_file}. Skipping creation.")

    # Create mcp-servers.json configuration
    mcp_config_file = current_dir / "mcp-servers.json"
    if not mcp_config_file.exists():
        with open(mcp_config_file, "w", encoding="utf-8") as f:
            f.write(MCP_SERVERS_JSON_TEMPLATE)
        logger.info(f"Created official MCP configuration at: {mcp_config_file}. (Please fill in your API tokens!)")
    else:
        logger.warning(f"MCP configuration already exists at: {mcp_config_file}. Skipping creation.")
        
    logger.info("Initialization complete. Try '@specfront_ai Hello' in Copilot Chat.")

def main():
    parser = argparse.ArgumentParser(description="Specfront AI CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # init command
    init_parser = subparsers.add_parser("init", help="Initialize the specfront_ai agents in the current workspace")
    
    args = parser.parse_args()
    
    if args.command == "init":
        init_workspace()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
