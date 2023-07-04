@echo off

:: Install dependencies
pip install praw

:: Run main.py or index.py depending on what exists
if exist main.py (
    python main.py
) else if exist index.py (
    python index.py
)
