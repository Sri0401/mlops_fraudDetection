import os
import subprocess
import pytest
from pathlib import Path

# Get the absolute path to the root of the repository
ROOT_DIR = Path(__file__).resolve().parent.parent

# Use this root path to construct the absolute path to your training script
TRAIN_SCRIPT_PATH = ROOT_DIR / "src" / "modeling" / "model.py"

@pytest.fixture(scope="session", autouse=True)
def run_train_script():
    """Fixture to run the model training script before tests."""
    print("Running training script...")
    print(f"Resolved training script path: {TRAIN_SCRIPT_PATH}")
    print(f"File exists: {TRAIN_SCRIPT_PATH.exists()}")

    # Run the script and capture stdout and stderr
    result = subprocess.run(
        ["python", str(TRAIN_SCRIPT_PATH)],
        check=False,
        capture_output=True,
        text=True
    )

    # Print the output for debugging
    print("--- model.py stdout ---")
    print(result.stdout)
    print("--- model.py stderr ---")
    print(result.stderr)
    print("--- End of script output ---")

    # Check the return code to see if the script failed
    result.check_returncode()

def test_model_training_runs_successfully():
    """Dummy test to ensure training script runs without error."""
    assert True  # Actual assertions can be added later
