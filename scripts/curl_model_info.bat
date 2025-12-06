@echo off
setlocal
set PORT=8000
curl -s http://localhost:%PORT%/v1/model_info
echo.
