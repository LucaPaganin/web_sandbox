param (
    [Parameter(Mandatory=$true)][string]$scriptPath
)

$scriptPath = "./test.py"
Write-Host $scriptPath

Start-Process -FilePath "./test.py"
