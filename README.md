🛡️ Neuro Forgery Detect
A deep learning-powered system for detecting image forgeries using noise residual analysis and CNN-based architecture.
Built with Python, TensorFlow/Keras, OpenCV for robust image forgery detection.

✨ Key Features
✔ Advanced Forgery Detection – Detects splicing, copy-move, and removal forgeries.
✔ Noise Residual Analysis – Identifies disruptions in natural noise patterns.
✔ Interactive Jupyter Notebooks – For exploration, visualization, and debugging.
✔ Pre-trained & Custom Training Support – Use existing models or train your own.

📂 Project Structure

Neuro-Forgery-Detect/
├── Dataset/                  # Main dataset directory (external link in DatasetLink.txt)
├── model/                    # Trained models and data arrays (.keras, .pckl, .npy)
├── model1/                   # Experimental models/checkpoints
├── testimages/               # Test images for predictions
├── config_template.py        # Template for local path configuration
├── train.py                  # Training script
├── nfd.py                    # Core script for prediction/inference
├── noise_clean.ipynb         # Notebook for noise residual processing
├── nfd.ipynb                 # Notebook for testing and visualization
├── requirements.txt          # Python dependencies
├── run.bat                   # (Optional) Windows execution script
├── DatasetLink.txt           # Dataset download info
└── README.md                 # Project documentation


🛠 Installation & Setup

1. Clone the Repository

git clone https://github.com/AayushPrasad22/Neuro-Forgery-Detect.git
cd Neuro-Forgery-Detect

2. Create Virtual Environment

python -m venv venv

Activate it:

Windows:

.\venv\Scripts\activate

Linux/Mac:

3. Install Dependencies

pip install -r requirements.txt

⚙️ Configuration

MODEL_DIR = r"C:\Path\To\Your\model"
TEST_IMAGES_DIR = r"C:\Path\To\Your\testimages"
NOISE_X_PATH = fr"{MODEL_DIR}\noise_X.npy"
CLEAN_Y_PATH = fr"{MODEL_DIR}\clean_Y.npy"
MODEL_PATH = fr"{MODEL_DIR}\noise_detect_clean.keras"

🚀 Usage
1. Train the Model
python train.py

2. Predict Forgery
python nfd.py

3. Explore with Notebooks
jupyter notebook

📦 Dataset
CASIA 2.0, Columbia, NIST forensics datasets

Download link in DatasetLink.txt

🤝 Contributing
1.Fork the repo

2.Create a branch:
git checkout -b feature-name

3.Commit & push

4.Open a Pull Request

📄 License
MIT License – Free to use and modify

📬 Contact
Author: Aayush Prasad
GitHub: AayushPrasad22


