@echo off

:: Create and activate a virtual environment (optional but recommended)
python3 -m venv myenv
call myenv/Scripts/activate.bat

:: Install dependencies
if exist requirements.txt (
    python3 main.py
)

:: Run main.py or index.py depending on what exists
if exist main.py (
    python3 main.py
) else if exist index.py (
    python3 index.py
)
