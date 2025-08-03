import os
import subprocess
import pytest

# The path to your training script relative to the project root
TRAIN_SCRIPT_PATH = "src/models/train_model.py"

@pytest.fixture(scope="session", autouse=True)
def run_train_script():
    """Fixture to run the training script before tests."""
    print("Running training script...")
    
    # Run the script and capture stdout and stderr
    result = subprocess.run(
        ["python", TRAIN_SCRIPT_PATH], 
        check=False,  # Set check=False to prevent immediate failure
        capture_output=True,
        text=True
    )
    
    # Print the output for debugging
    print("--- train_model.py stdout ---")
    print(result.stdout)
    print("--- train_model.py stderr ---")
    print(result.stderr)
    print("--- End of script output ---")
    
    # Now, check the return code
    result.check_returncode() # This will raise CalledProcessError if it failed
    
    # Yield control to the tests
    yield

    # Clean up the generated model file after tests are done
    try:
        os.remove("models/trained_model.joblib")
    except OSError:
        pass  # Ignore if the file doesn't exist

def test_model_file_created():
    """Test to check if the trained model file is created successfully."""
    assert os.path.exists("models/trained_model.joblib")