@echo off
echo Creating virtual environment...
python -m venv .venv

echo Activating virtual environment...
call .venv\Scripts\activate.bat
ollama pull smollm:135m
ollama pull phi:latest
ollama pull gemma3:1b
echo Installing required packages...
pip install -r req.txt

echo Downloading model...
python Bot.py --download_only

echo Done!
pause
