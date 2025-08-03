import os
import subprocess
import pytest

# You might need to adjust the path depending on where your script is located
TRAIN_SCRIPT_PATH = "src/models/train_model.py"

@pytest.fixture(scope="session", autouse=True)
def run_train_script():
    """Fixture to run the training script before tests."""
    # This runs your training script to generate the model file
    subprocess.run(["python", TRAIN_SCRIPT_PATH], check=True)

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