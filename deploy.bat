@echo off

:: Create and activate a virtual environment (optional but recommended)
python -m venv myenv
call myenv/Scripts/activate.bat

:: Install dependencies
pip install praw

:: Run main.py or index.py depending on what exists
if exist main.py (
    python main.py
) else if exist index.py (
    python index.py
)
