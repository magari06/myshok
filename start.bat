@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ========================================================
echo   MYSHOK — 3D Portfolio Local Server
echo   Serving 3D Models: fox.glb, ghost.glb, harrenhal.glb
echo   URL: http://localhost:3000/
echo ========================================================
start http://localhost:3000/
node server.js
pause
