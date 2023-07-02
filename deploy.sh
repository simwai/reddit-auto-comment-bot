#!/bin/bash

# Create and activate a virtual environment (optional but recommended)
python -m venv myenv
source myenv/bin/activate

# Install dependencies
pip install praw

# Run main.py or index.py depending on what exists
if [ -f main.py ]; then
    python3.6 main.py
elif [ -f index.py ]; then
    python3.6 index.py
fi
