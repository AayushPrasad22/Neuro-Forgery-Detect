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

## 🛠 Installation
1️⃣ Clone the repository
```
git clone https://github.com/AayushPrasad22/Neuro-Forgery-Detect.git
cd Neuro-Forgery-Detect
```
2️⃣ Create and activate a virtual environment
```
Windows:
python -m venv venv
venv\Scripts\activate

Linux/Mac:
python3 -m venv venv
source venv/bin/activate

```
3️⃣ Install dependencies
```
pip install -r requirements.txt

```
4️⃣ Download Dataset
```
Check DatasetLink.txt for dataset download link and place it in the Dataset/ folder.
```
5️⃣ Run Jupyter Notebook or Scripts
```
Start Jupyter Notebook:
jupyter notebook

Or run the main prediction script:
python nfd.py
```
5️⃣ Configure Paths
```
Create your local config.py file based on config_template.py:
MODEL_DIR = r"C:\path\to\model"
TEST_IMAGES_DIR = r"C:\path\to\testimages"

NOISE_X_PATH = fr"{MODEL_DIR}\noise_X.npy"
CLEAN_Y_PATH = fr"{MODEL_DIR}\clean_Y.npy"

MODEL_PATH = fr"{MODEL_DIR}\noise_detect_clean.keras"
HISTORY_PATH = fr"{MODEL_DIR}\noise_detect_clean.pckl"

TEST_IMAGE_PATH_1 = fr"{TEST_IMAGES_DIR}\01.png"
TEST_IMAGE_PATH_2 = fr"{TEST_IMAGES_DIR}\02.png"
TEST_IMAGE_PATH_3 = fr"{TEST_IMAGES_DIR}\04.png"
```
Usage
```
✅ Train the Model
python train.py
✅ Run Predictions
python nfd.py
✅ Explore with Jupyter Notebook
jupyter notebook

```plaintext
Then open:
noise_clean.ipynb → For noise residual processing
nfd.ipynb → For inference and visualization
```
📊 Results & Visualization
```
The model outputs a forgery heatmap that highlights manipulated regions in an image.
Example output:

Original Image → Predicted Forgery Map
(Insert before/after sample images here)
```
🧩 Tech Stack
```
Python 3.8+

TensorFlow/Keras

OpenCV

NumPy, Matplotlib

Jupyter Notebooks
```
🤝 Contributing
```
Contributions are welcome!
```
1.Fork the repo
```
2.Create a new branch:
```
git checkout -b feature/your-feature-name
```
3.Commit your changes:
```
git commit -m "Add your feature"
```
4.Push to your branch:
```
git push origin feature/your-feature-name
```
```
5.Create a Pull Request

```
📜 License
```
This project is licensed under the MIT License – see the LICENSE file for details.
```
📧 Contact
```
👤 Aayush Prasad
📩 GitHub: AayushPrasad22
