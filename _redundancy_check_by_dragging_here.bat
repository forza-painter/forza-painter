@echo off
cd /D "%~dp0"
if "%~1"=="" (
@echo You must drag a `.json` geometry file to do a redundant shape check.
) else (
forza-painter.exe %* -redundant
)
pause