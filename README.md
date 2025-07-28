# 🛡️ RFID-Net: A Robust Image Forgery Detection Network

## ✨ Project Overview

In an era where digital visual content is ubiquitous, the integrity of images is paramount. This project introduces **RFID-Net**, a cutting-edge deep learning model meticulously designed to detect subtle and sophisticated manipulations within digital images. Leveraging advanced neural network architectures, RFID-Net aims to distinguish genuine images from doctored ones by identifying inconsistencies and anomalies introduced during the forgery process. Our goal is to contribute to a more trustworthy digital ecosystem by providing a robust tool for image forensics.

---

## 🚀 Features

* **Advanced Forgery Detection:** Employs a deep neural network to identify various types of image forgeries (e.g., splicing, copy-move, removal).
* **Noise Residual Analysis:** Specifically designed to analyze inherent noise patterns and their disruptions, which are key indicators of tampering.
* **Comprehensive Dataset Support:** Trained and evaluated using widely recognized image forensics datasets such as CASIA 2.0, Columbia, and NIST.
* **Modular & Extensible Codebase:** Organized Python scripts and Jupyter notebooks ensure clarity, ease of understanding, and potential for future enhancements.
* **User-Friendly Setup:** Simplified steps to get the project up and running quickly.

---

## 🛠️ Getting Started

Follow these steps to set up your local development environment and run the RFID-Net project.

### Prerequisites

Ensure you have the following installed on your system:

* **Python 3.8+** (Recommended version)
* **Git**

### Installation

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/AayushPrasad22/RFID-Net--Robust-Image-Forgery-Detection.git](https://github.com/AayushPrasad22/RFID-Net--Robust-Image-Forgery-Detection.git)
    cd RFID-Net--Robust-Image-Forgery-Detection
    ```

2.  **Create a virtual environment (highly recommended for dependency management):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS / Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 📂 Dataset

The core of RFID-Net's training and evaluation relies on specialized image forgery datasets.

* **Location:** The `Dataset/` directory within this repository contains the structured image data.
* **Included Subsets:** This typically includes images from known forensics benchmarks such as `CASIA 2.0`, `Columbia`, and `NIST`.
* **External Link (if applicable):** If the full dataset exceeds GitHub's size limits or requires external download, please refer to `DatasetLink.txt` for instructions or download URLs.

---

## 🚀 Usage

### Training the Model

To train your own RFID-Net model, execute the `train.py` script:

```bash
python train.py
