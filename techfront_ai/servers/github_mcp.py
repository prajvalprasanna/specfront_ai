import logging
from fastmcp import FastMCP
from typing import List

logger = logging.getLogger("techfront_ai.servers.github")
logger.setLevel(logging.INFO)

# Initialize GitHub FastMCP Server
mcp = FastMCP("Techfront GitHub Server")
logger.info("Initializing techfront_ai GitHub FastMCP server tools...")

@mcp.tool()
def search_github_code(query: str, repo_owner: str, repo_name: str) -> List[str]:
    """
    Searches a specific GitHub repository for code snippets matching the query.
    Useful for finding existing implementations, architectural references, or boilerplate before writing new code.
    
    Args:
        query: The codebase search term (e.g., 'def init_workspace')
        repo_owner: The organization or user (e.g., 'techfront')
        repo_name: The repository name (e.g., 'core-app')
    """
    logger.info(f"GitHub Tool called: searching {repo_owner}/{repo_name} for '{query}'")
    return [
        "Found match in src/main.py: `def init_workspace(): return True`",
        "Found reference in docs/architecture.md"
    ]

@mcp.tool()
def get_github_file(file_path: str, repo_owner: str, repo_name: str) -> str:
    """
    Retrieves the raw text content of a file from a specified GitHub repository.
    
    Args:
        file_path: The path to the file in the repository (e.g., 'package.json')
        repo_owner: The organization or user
        repo_name: The repository name
    """
    logger.info(f"GitHub Tool called: fetching {file_path} from {repo_owner}/{repo_name}")
    return f"// Simulated contents of {file_path} from {repo_owner}/{repo_name}\n" + "{\n  \"dependencies\": {\n    \"react\": \"^18.2.0\"\n  }\n}"

if __name__ == "__main__":
    mcp.run()
