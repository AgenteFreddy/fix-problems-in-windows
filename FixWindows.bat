@echo off
echo This .bat will resolve your problems
timeout /t 5
net stop wuauserv
net stop cryptSvc
net stop bits
net stop msiserver
ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
ren C:\Windows\System32\catroot2 catroot2.old
net start wuauserv
net start cryptSvc
net start bits
net start msiserver
sfc /scannow
dism /online /cleanup-image /restorehealth
sfc /scannow
del /q/f/s %TEMP%\*
pause