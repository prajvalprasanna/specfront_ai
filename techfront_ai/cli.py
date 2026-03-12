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
logger = logging.getLogger("techfront_ai.cli")

def init_workspace():
    from .templates import (
        AGENT_TEMPLATE, PLANNER_TEMPLATE, CODER_TEMPLATE, 
        TESTER_TEMPLATE, SPEC_TEMPLATE, MCP_SERVERS_JSON_TEMPLATE
    )
    
    logger.info("Initializing specfront_ai workspace with multi-agent setup...")
    current_dir = Path.cwd()
    
    # Create .github/agents directory
    agent_dir = current_dir / ".github" / "agents"
    agent_dir.mkdir(parents=True, exist_ok=True)
    logger.debug(f"Ensured directory exists: {agent_dir}")
    
    agents_to_create = {
        "techfront_ai.agent.md": AGENT_TEMPLATE,
        "techfront_ai_planner.agent.md": PLANNER_TEMPLATE,
        "techfront_ai_coder.agent.md": CODER_TEMPLATE,
        "techfront_ai_tester.agent.md": TESTER_TEMPLATE,
    }

    for filename, content in agents_to_create.items():
        agent_file = agent_dir / filename
        if not agent_file.exists():
            with open(agent_file, "w", encoding="utf-8") as f:
                f.write(content)
            logger.info(f"Created agent definition: {filename}")
        else:
            logger.warning(f"Agent {filename} already exists. Skipping.")

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
        
    logger.info("Initialization complete. Try '@techfront_ai Hello' in Copilot Chat.")

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
