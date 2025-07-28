# RFID-Net: A Robust Image Forgery Detection Network

## Project Overview

This project implements **RFID-Net**, a robust deep learning model designed for the detection of image forgeries. In today's digital age, image manipulation is becoming increasingly sophisticated. RFID-Net aims to identify subtle inconsistencies and anomalies within images that indicate tampering, thereby contributing to the integrity and trustworthiness of visual content.

## Features

* **Robust Forgery Detection:** Utilizes deep learning techniques to identify various types of image forgeries.
* **Noise Residual Analysis:** Leverages noise characteristics within images to uncover tampering.
* **Dataset Compatibility:** Tested with common image forensics datasets like CASIA 2.0, Columbia, and NIST.
* **Modular Design:** Code is structured for clarity and easy extension.

## Getting Started

Follow these instructions to set up the project locally for development and testing.

### Prerequisites

Ensure you have Python 3.x installed. This project relies on several Python libraries.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/RFID-Net-Image-Forgery-Detection.git](https://github.com/your-username/RFID-Net-Image-Forgery-Detection.git)
    cd RFID-Net-Image-Forgery-Detection
    ```
    *(Replace `your-username` and `RFID-Net-Image-Forgery-Detection` with your actual GitHub username and repository name.)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Dataset

The project utilizes specific datasets for training and evaluation.

* **Dataset Location:** The `Dataset/` folder in this repository contains the necessary image data.
* **Source:** This dataset typically includes image collections like CASIA 2.0, Columbia, and NIST.
* **Note:** If the full dataset is very large, the `Dataset/` folder might only contain a subset, or you may need to download the full dataset from an external source specified in `DatasetLink.txt`.

### Running the Project

#### Training the Model

To train the RFID-Net model, execute the `train.py` script:

```bash
python train.py