@echo off
echo Discord: A-Dawg#0001 (AE)
echo Supports: Forza Horizon 5
echo Offically: MS Store/XBOX PC App (latest version), Steam (latest version).
echo Unofficially: Every version that isn't running on a console of via cloud gaming should work.
echo License: MIT
echo Year: 2022

color 0F
title forza-painter-geometrize by A-Dawg#0001

cd /d "%~dp0"
set "ARG1=%~1"

IF NOT "%ARG1%" == "" GOTO Dragged

set /p ARG1="[MANUAL MODE] Paste the image path: "

:Dragged
rem Optionally use `call activate myAnacondaEnvironment` here

@forza-painter-geometrize.exe "%ARG1%"
cls
color 0F
echo FINISHED!
pause