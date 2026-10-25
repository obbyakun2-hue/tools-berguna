@echo off
chcp 65001 >nul
title Installer Tools Berguna - 1 Klik
echo ============================================================
echo   INSTALLER TOOLS BERGUNA (sumber resmi via winget)
echo ============================================================
echo Script ini menjalankan PowerShell installer di folder yang sama.
echo Pastikan file Installer-1Klik.ps1 ada di samping file ini.
echo.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0Installer-1Klik.ps1"
echo.
pause
