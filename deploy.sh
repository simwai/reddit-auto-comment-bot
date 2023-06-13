#!/bin/bash

# Create and activate a virtual environment (optional but recommended)
python3 -m venv myenv
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run main.py or index.py depending on what exists
if [ -f main.py ]; then
    python3 main.py
elif [ -f index.py ]; then
    python3 index.py
fi