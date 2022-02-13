param (
    [Parameter(Mandatory=$true)][string]$origFile,
    [Parameter(Mandatory=$true)][string]$pattern,
    [Parameter(Mandatory=$true)][string]$replacement
)

if (Test-Path -Path $origFile -PathType Leaf){
    $dstFile = "latest.yml"
    Write-Host "File $origFile exists, copying it to $dstFile"
    cp $origFile $dstFile
    # Write-Host (Get-Content $dstFile)
    $output = ((Get-Content $dstFile -Raw) -replace $pattern, $replacement)
    # $output = $output -replace $pattern, $replacement
    # Write-Output $output | Out-File -FilePath $dstFile
    # rm ./latest.yml
    $pkg = Get-Content ./package.json | ConvertFrom-Json
    $pkg.version = "1.0.47-12"
    ConvertTo-Json $pkg | Out-File ./package.json
}
else {
    Write-Error "file $orig_file does not exist"
}

