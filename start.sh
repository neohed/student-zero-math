#!/usr/bin/env bash
set -e

VENV=".venv"
KERNEL_NAME="student-zero-math"

# Create venv on first run
if [ ! -d "$VENV" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV"
fi

source "$VENV/bin/activate"

# Install / sync dependencies
echo "Checking dependencies..."
pip install -q -r requirements.txt

# Register kernel into the venv itself
echo "Registering Jupyter kernel..."
python -m ipykernel install --user --name "$KERNEL_NAME" --display-name "$KERNEL_NAME"

echo ""
echo "Ready. Open a notebook in VS Code and select kernel: $KERNEL_NAME"
echo "Or run: jupyter lab"
