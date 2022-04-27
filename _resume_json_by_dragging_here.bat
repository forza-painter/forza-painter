@echo off
cd /D "%~dp0"
if "%~1"=="" (
@echo You must drag a `.json` geometry file to resume.
) else (
forza-painter.exe %* -resume
)
pause
