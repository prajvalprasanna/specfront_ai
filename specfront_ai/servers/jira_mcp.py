import logging
from fastmcp import FastMCP
from typing import Dict, Any

logger = logging.getLogger("specfront_ai.servers.jira")
logger.setLevel(logging.INFO)

# Initialize Jira FastMCP Server
mcp = FastMCP("Techfront Jira Server")
logger.info("Initializing specfront_ai Jira FastMCP server tools...")

@mcp.tool()
def get_jira_issue(issue_key: str) -> Dict[str, Any]:
    """
    Fetch details (User Story, Acceptance Criteria) of a specific Jira issue.
    Use this to pull requirements before writing specs or code.
    
    Args:
        issue_key: The Jira issue identifier (e.g., 'PROJ-123')
    """
    logger.info(f"Jira Tool called: get_jira_issue for key {issue_key}")
    return {
        "key": issue_key,
        "summary": "Implement Requirements via Human-in-the-Loop",
        "description": "User wants an App. Agent must write a command to install React, but explicitly ask the user to run it before proceeding.",
        "status": "In Progress"
    }

@mcp.tool()
def create_jira_issue(summary: str, description: str, project_key: str) -> str:
    """
    Create a new Jira issue/User Story.
    
    Args:
        summary: Issue title
        description: Detailed description of the issue
        project_key: Key of the Jira project
    """
    logger.info(f"Jira Tool called: create_jira_issue in project {project_key}.")
    new_issue_key = f"{project_key}-101"
    return new_issue_key

if __name__ == "__main__":
    mcp.run()
