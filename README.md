# 🛡️ Neuro Forgery Detect

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-F37626.svg)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A deep learning-powered system for detecting image forgeries using noise residual analysis and CNN-based architecture.  
Built with **Python**, **TensorFlow/Keras**, and **OpenCV** for robust image forgery detection.

---

## ✨ Key Features

- ✔ **Advanced Forgery Detection** – Detects splicing, copy-move, and removal forgeries.
- ✔ **Noise Residual Analysis** – Identifies disruptions in natural noise patterns.
- ✔ **Interactive Jupyter Notebooks** – For exploration, visualization, and debugging.
- ✔ **Pre-trained & Custom Training Support** – Use existing models or train your own.

---

## 📂 Project Structure

Neuro-Forgery-Detect/
├── Dataset/ # Main dataset directory (external link in DatasetLink.txt)
├── model/ # Trained models and data arrays (.keras, .pckl, .npy)
├── model1/ # Experimental models/checkpoints
├── testimages/ # Test images for predictions
├── config_template.py # Template for local path configuration
├── train.py # Training script
├── nfd.py # Core script for prediction/inference
├── noise_clean.ipynb # Notebook for noise residual processing
├── nfd.ipynb # Notebook for testing and visualization
├── requirements.txt # Python dependencies
├── run.bat # (Optional) Windows execution script
├── DatasetLink.txt # Dataset download info
└── README.md # Project documentation



## 🛠 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/AayushPrasad22/Neuro-Forgery-Detect.git
cd Neuro-Forgery-Detect
2. Create Virtual Environment

python -m venv venv
Activate it:

Windows:

.\venv\Scripts\activate


Linux/Mac:

source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt


⚙️ Configuration
Edit your config file to set paths:


MODEL_DIR = r"C:\Path\To\Your\model"
TEST_IMAGES_DIR = r"C:\Path\To\Your\testimages"
NOISE_X_PATH = fr"{MODEL_DIR}\noise_X.npy"
CLEAN_Y_PATH = fr"{MODEL_DIR}\clean_Y.npy"
MODEL_PATH = fr"{MODEL_DIR}\noise_detect_clean.keras"

🚀 Usage
Train the Model

python train.py
Predict Forgery
python nfd.py

Explore with Notebooks

jupyter notebook

📦 Dataset
Uses CASIA 2.0, Columbia, and NIST forensic datasets.
Download link is provided in DatasetLink.txt.

🤝 Contributing
Fork the repo

Create a branch:

git checkout -b feature-name

Commit & push:

git add .
git commit -m "Add feature"
git push origin feature-name
Open a Pull Request

📄 License
MIT License – Free to use and modify.

📬 Contact
Author: Aayush Prasad
GitHub: AayushPrasad22
