@echo off
echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Starting app...
python app.py
pause
