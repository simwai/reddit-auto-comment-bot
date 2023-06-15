#!/bin/bash

# Create and activate a virtual environment (optional but recommended)
python3.10 -m venv myenv
source myenv/bin/activate

# Install dependencies
python3.10 -m pip install praw

# Run main.py or index.py depending on what exists
if [ -f main.py ]; then
    python3.10 main.py
elif [ -f index.py ]; then
    python3.10 index.py
fi
