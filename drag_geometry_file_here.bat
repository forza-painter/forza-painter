rem Discord: A-Dawg#0001 (AE)
rem Supports: Forza Horizon 5
rem Offically (v1.405.2.0, v3.414.967.0)
rem Unofficially (most versions should work)
rem License: MIT
rem Year: 2021

echo off
setlocal EnableDelayedExpansion

cd /d "%~dp0"
set "ARG1=%~1"
IF NOT "%ARG1%" == "" GOTO Dragged
set /p ARG1="Geometrize JSON file: "
:Dragged
rem Optionally use `call activate myAnacondaEnvironment` here
@python main.py "%ARG1%"
pause