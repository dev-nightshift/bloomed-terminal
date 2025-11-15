@echo off
setlocal
set PORT=8000

curl -s -X POST http://localhost:%PORT%/v1/chat ^
  -H "Content-Type: application/json" ^
  -d "{ \"messages\": [ {\"role\":\"system\",\"content\":\"You are Bloomed Terminal.\"}, {\"role\":\"user\",\"content\":\"Give me a one-sentence creative entry about neon rain.\"} ], \"max_new_tokens\": 64 }"
echo.
