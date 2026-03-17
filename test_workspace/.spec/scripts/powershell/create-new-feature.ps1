# .spec/scripts/powershell/create-new-feature.ps1
param([string]$FeatureName)

. "$PSScriptRoot\common.ps1"

if (-not $FeatureName) {
    Write-ErrorMsg "FeatureName is required."
    exit 1
}

Write-Step "Creating feature scaffolding for: $FeatureName"
# Add logic to scaffold UI/BE components
Write-Success "Scaffolding complete."
