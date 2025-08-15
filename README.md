# 🛡️ Neuro Forgery Detect

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-F37626.svg)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A deep learning-powered system for detecting image forgeries using noise residual analysis and CNN-based architecture.  
Built with **Python**, **TensorFlow/Keras**, and **OpenCV** for robust image forgery detection.

---

---

## ✨ Key Features
- ✔ **Advanced Forgery Detection** – Detects splicing, copy-move, and removal forgeries.
- ✔ **Noise Residual Analysis** – Identifies disruptions in natural noise patterns.
- ✔ **Interactive Jupyter Notebooks** – For exploration, visualization, and debugging.
- ✔ **Pre-trained & Custom Training Support** – Use existing models or train your own.

---

## 📂 Project Structure
```plaintext
Neuro-Forgery-Detect/
├── Dataset/                # Main dataset directory (external link in DatasetLink.txt)
├── model/                  # Trained models and data arrays (.keras, .pckl, .npy)
├── model1/                 # Experimental models/checkpoints
├── testimages/             # Test images for predictions
├── config_template.py      # Template for local path configuration
├── train.py                # Training script
├── nfd.py                  # Core script for prediction/inference
├── noise_clean.ipynb       # Notebook for noise residual processing
├── nfd.ipynb               # Notebook for testing and visualization
├── requirements.txt        # Python dependencies
├── run.bat                 # (Optional) Windows execution script
├── DatasetLink.txt         # Dataset download info
└── README.md               # Project documentation
```

---

## 🛠 Installation
1️⃣ Clone the repository
git clone https://github.com/AayushPrasad22/Neuro-Forgery-Detect.git
cd Neuro-Forgery-Detect

2️⃣ Create and activate a virtual environment

Windows:

python -m venv venv
venv\Scripts\activate


Linux/Mac:

python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Download Dataset

Check DatasetLink.txt for dataset download link and place it in the Dataset/ folder.

5️⃣ Run Jupyter Notebook or Scripts

Start Jupyter Notebook:

jupyter notebook


Or run the main prediction script:

python nfd.py
