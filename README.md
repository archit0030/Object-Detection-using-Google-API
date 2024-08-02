# Bounding Box Detection with Gemini API

This repository contains a Python script that uses the Gemini API to generate bounding box coordinates for objects in an image. Specifically, the script processes an image of a mop basket and returns the bounding box coordinates for the basket. The bounding box is then drawn on the image and displayed.

## Prerequisites

- Python 3.9 or above
- Pillow (PIL) library
- IPython display module
- Gemini API access

## Setup

1. **Install the required libraries:**

   ```bash
   pip install pillow ipython google-generativeai
   
2. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/bounding-box-detection.git
    cd bounding-box-detection

3. **Configure the Gemini API:**

    Replace YOUR_API_KEY in the code with your actual Gemini API key.
