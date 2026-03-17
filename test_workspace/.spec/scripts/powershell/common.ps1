# .spec/scripts/powershell/common.ps1
# Common utility functions for Specfront AI scripts

function Write-Step {
    param([string]$Message)
    Write-Host " [?] $Message" -ForegroundColor Cyan
}

function Write-Success {
    param([string]$Message)
    Write-Host " [V] $Message" -ForegroundColor Green
}

function Write-ErrorMsg {
    param([string]$Message)
    Write-Host " [X] $Message" -ForegroundColor Red
}
