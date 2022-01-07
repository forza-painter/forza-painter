@echo off
echo Discord: A-Dawg#0001 (AE)
echo Supports: Forza Horizon 5
echo Offically: MS Store/XBOX PC App (latest version), Steam (latest version).
echo Unofficially: Every version that isn't running on a console of via cloud gaming should work.
echo License: MIT
echo Year: 2022

color 0F
title forza-painter by A-Dawg#0001
setlocal EnableDelayedExpansion

reg query "hkcu\software\Python" > NUL
if %ERRORLEVEL% NEQ 0 goto NO_PYTHON
echo:
@python --version 2>NUL
if not ERRORLEVEL==0 goto NO_PYTHON
for /f "delims=" %%V in ('python -V') do @set python_version=%%V
echo Above version detected. (Please note only 3.8 or later officially supported)
echo:
echo If having trouble please READ THE README, and join the discord:
echo https://discord.gg/BJNFCxPKhu
echo:
cd /d "%~dp0"
set "ARG1=%~1"
IF NOT "%ARG1%" == "" GOTO Dragged
set /p ARG1="[MANUAL MODE] Paste the .json geometry file path: "
:Dragged
rem Optionally use `call activate myAnacondaEnvironment` here
@python main.py "%ARG1%"
goto EOF

:NO_PYTHON
cls
color 04
echo You must install python 3.8 or later and make sure to `Add to PATH` when installing.
echo:
echo If you have installed python already, you likely forgot to select `Add to PATH` during installation.
echo Try installing it from the Microsoft Store if you continue to have issues!
pause

:EOF
cls
color 0F
echo FINISHED!
pause