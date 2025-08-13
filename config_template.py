# config_template.py
# Rename this file to config.py and update paths for your system.

BASE_DIR = r"/path/to/Neuro-Forgery-Detect"
MODEL_DIR = fr"{BASE_DIR}/model"
MODEL1_DIR = fr"{BASE_DIR}/model1"
TEST_IMAGES_DIR = fr"{BASE_DIR}/testImages"

NOISE_X_PATH = fr"{MODEL_DIR}/noise_X.npy"
CLEAN_Y_PATH = fr"{MODEL_DIR}/clean_Y.npy"

MODEL_PATH = fr"{MODEL_DIR}/noise_detect_clean.keras"
HISTORY_PATH = fr"{MODEL_DIR}/noise_detect_clean.pckl"

TEST_IMAGE_PATH_1 = fr"{TEST_IMAGES_DIR}/01.png"
TEST_IMAGE_PATH_2 = fr"{TEST_IMAGES_DIR}/02.png"
TEST_IMAGE_PATH_3 = fr"{TEST_IMAGES_DIR}/04.png"
