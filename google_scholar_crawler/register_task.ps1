# Registers a daily Windows scheduled task that runs update_stats.py.
# StartWhenAvailable catches up on the next boot/login if the PC was off.
$script = Join-Path $PSScriptRoot "update_stats.py"
$pythonw = Join-Path (Split-Path (Get-Command python).Source) "pythonw.exe"

$action = New-ScheduledTaskAction -Execute $pythonw -Argument "`"$script`""
$trigger = New-ScheduledTaskTrigger -Daily -At "10:17"
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Minutes 15)
Register-ScheduledTask -TaskName "ScholarCitationUpdate" -Action $action -Trigger $trigger `
    -Settings $settings -Description "Refresh Google Scholar citations for xuhaolei.github.io" -Force
