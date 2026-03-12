import logging
from fastmcp import FastMCP
from typing import Dict, Any, List

logger = logging.getLogger("techfront_ai.servers.figma")
logger.setLevel(logging.INFO)

# Initialize Figma FastMCP Server
mcp = FastMCP("Techfront Figma Server")
logger.info("Initializing techfront_ai Figma FastMCP server tools...")

@mcp.tool()
def get_figma_node(file_key: str, node_id: str) -> Dict[str, Any]:
    """
    Retrieve design element details and UI layout constraints from a Figma file.
    Use this when the user asks to implement a UI to get exact specifications.
    
    Args:
        file_key: The unique identifier of the Figma file
        node_id: The specific node/element ID to inspect
    """
    logger.info(f"Figma Tool called: get_figma_node for file {file_key}, node {node_id}")
    return {
        "id": node_id,
        "name": "Target UI Component",
        "type": "FRAME",
        "properties": {
            "backgroundColor": "#FFFFFF",
            "layoutMode": "VERTICAL",
            "padding": 24,
            "cornerRadius": 8
        }
    }

@mcp.tool()
def get_figma_comments(file_key: str) -> List[Dict[str, Any]]:
    """
    Get all comments and human feedback left on a specific Figma design file.
    
    Args:
        file_key: The unique identifier of the Figma file
    """
    logger.info(f"Figma Tool called: get_figma_comments for file {file_key}")
    return [
        {
            "id": "comment_1",
            "message": "Make sure the dashboard matches the new branding guidelines.",
            "user": "Design Lead",
            "resolved": False
        }
    ]

if __name__ == "__main__":
    mcp.run()
