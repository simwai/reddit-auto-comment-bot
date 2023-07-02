@echo off

:: Create and activate a virtual environment (optional but recommended)
python3.6 -m venv myenv
call myenv/Scripts/activate.bat

:: Install dependencies
pip3 install -r requirements.txt

:: Run main.py or index.py depending on what exists
if exist main.py (
    python3.6 main.py
) else if exist index.py (
    python3.6 index.py
)
