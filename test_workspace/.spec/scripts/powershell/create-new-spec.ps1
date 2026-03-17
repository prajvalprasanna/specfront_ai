# .spec/scripts/powershell/create-new-spec.ps1
param([string]$SpecName)

. "$PSScriptRoot\common.ps1"

$SpecsDir = Join-Path (Split-Path $PSScriptRoot -Parent -Parent) "specs"
if (-not (Test-Path $SpecsDir)) { New-Item -ItemType Directory -Path $SpecsDir | Out-Null }

$TargetFile = Join-Path $SpecsDir "$SpecName.md"
Copy-Item (Join-Path $PSScriptRoot "..\templates\tasks-template.md") $TargetFile

Write-Success "Created new spec at $TargetFile"
