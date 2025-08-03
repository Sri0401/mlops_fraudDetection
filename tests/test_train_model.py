import os
import subprocess
import pytest
from pathlib import Path

# Get the absolute path to the root of the repository
ROOT_DIR = Path(__file__).resolve().parent.parent

# Use this root path to construct the absolute path to your training script
TRAIN_SCRIPT_PATH = ROOT_DIR / "src" / "models" / "train_model.py"

@pytest.fixture(scope="session", autouse=True)
def run_train_script():
    """Fixture to run the training script before tests."""
    print("Running training script...")
    
    # Run the script and capture stdout and stderr
    # We use the absolute path we constructed above
    result = subprocess.run(
        ["python", str(TRAIN_SCRIPT_PATH)],
        check=False,
        capture_output=True,
        text=True
    )
    
    # Print the output for debugging
    print("--- train_model.py stdout ---")
    print(result.stdout)
    print("--- train_model.py stderr ---")
    print(result.stderr)
    print("--- End of script output ---")
    
    # Check the return code to see if the script failed
    result.check_returncode()
    
    # Yield control to the tests
    yield

    # Clean up the generated model file after tests are done
    try:
        os.remove("models/trained_model.joblib")
    except OSError:
        pass

def test_model_file_created():
    """Test to check if the trained model file is created successfully."""
    # Check for the model file at the correct path
    assert os.path.exists(str(ROOT_DIR / "models" / "trained_model.joblib"))