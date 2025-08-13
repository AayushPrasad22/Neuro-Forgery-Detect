# config_template.py
# Copy this file to config.py and update the paths for your system

PROJECT_ROOT = r"/path/to/project"
MODEL_DIR = fr"{PROJECT_ROOT}/model"
TEST_IMAGES_DIR = fr"{PROJECT_ROOT}/testImages"

# Dataset .npy files
NOISE_X_PATH = fr"{MODEL_DIR}/noise_X.npy"
CLEAN_Y_PATH = fr"{MODEL_DIR}/clean_Y.npy"
X_PATH = fr"{MODEL_DIR}/X.npy"
Y_PATH = fr"{MODEL_DIR}/Y.npy"

# Model weights & history
NOISE_MODEL_PATH = fr"{MODEL_DIR}/noise_detect_clean.hdf5"
NOISE_HISTORY_PATH = fr"{MODEL_DIR}/noise_detect_clean.pckl"
RIFD_MODEL_PATH = fr"{MODEL_DIR}/rifd.hdf5"
RIFD_HISTORY_PATH = fr"{MODEL_DIR}/rifd.pckl"

# Test images
TEST_IMAGE_PATH_1 = fr"{TEST_IMAGES_DIR}/01.png"
TEST_IMAGE_PATH_2 = fr"{TEST_IMAGES_DIR}/02.png"
TEST_IMAGE_PATH_3 = fr"{TEST_IMAGES_DIR}/04.png"
