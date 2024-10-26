## Setting Up the Food-Allergen-Detector

### Prerequisites
- Python 3.x
- Required libraries (install using `pip install -r requirements.txt`)

### Steps to Download and Process Images

1. **Download the Food-101 Dataset**: 
   Download the dataset from [Food-101](https://data.vision.ee.ethz.ch/cvl/food-101.tar.gz) and extract it.

2. **Directory Structure**:
   Place the extracted images in the following structure:

3. **Run the Preprocessing Code**:
Execute the preprocessing script:
```bash
python src/data_preprocessing.py
```
4. **Check Processed Images**:
   After running the script, the processed images will be in the data/processed_images folder.
