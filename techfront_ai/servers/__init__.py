"""
Central export for all FastMCP servers in the techfront_ai architectures.
"""
from .github_mcp import mcp as github_mcp
from .jira_mcp import mcp as jira_mcp
from .figma_mcp import mcp as figma_mcp

__all__ = ["github_mcp", "jira_mcp", "figma_mcp"]
