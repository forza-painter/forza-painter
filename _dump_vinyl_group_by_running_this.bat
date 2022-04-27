@echo off
cd /D "%~dp0"
if "%~1"=="" (
forza-painter.exe -dump
) else (
@echo %1
@echo Don't drag here! This dumps hand made vinyls.
@echo Drag `.json` files onto `forza-painter.exe` to import them.
)
pause