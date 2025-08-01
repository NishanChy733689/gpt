@echo off
echo Activating virtual environment...
call .venv\Scripts\activate.bat

ipconfig

echo Starting app...
ssh -R 80:localhost:5000 serveo.net
streamlit run app.py --server.port=5000

echo Open it on the ipv4 address and port 5000
pause
