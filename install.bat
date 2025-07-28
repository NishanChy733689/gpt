@echo off
echo Creating virtual environment...
python -m venv .venv

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Installing required packages...
pip install -r req.txt

echo Downloading model...
python Bot.py --download_only

echo Done!
pause
