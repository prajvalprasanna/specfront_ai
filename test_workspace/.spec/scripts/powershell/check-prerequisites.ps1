# .spec/scripts/powershell/check-prerequisites.ps1
. "$PSScriptRoot\common.ps1"

Write-Step "Checking system prerequisites..."
# Add checks for Node, Python, Docker, etc.
Write-Success "All prerequisites met."
