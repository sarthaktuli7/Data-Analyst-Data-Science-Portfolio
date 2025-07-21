**Follow these steps to set up and run the Syracuse Rent Analyzer on your local machine:**

Prerequisites
Python 3.7+ (Anaconda is recommended for environment management)

pip (Python package installer)

1. Set Up Your Environment
Open your Anaconda Prompt (or your terminal/command prompt) and navigate to your desired project directory.

# Navigate to where you want to create your project folder
cd C:\Users\YourUser\Documents\Projects 

# Create the project folder
mkdir syracuse_rent_analyzer
cd syracuse_rent_analyzer

# Create the 'data' subfolder
mkdir data

# Activate your base environment (or create a new one)
conda activate base 
2. Install Dependencies
In the Anaconda Prompt (with your environment activated), install the necessary Python libraries:

Bash

conda install pandas streamlit geopy
# If conda has issues, you can try:
# pip install pandas streamlit geopy

3. Place Your Data File
Make sure your rental data file is named corrected_csv.csv and placed inside the data folder within your syracuse_rent_analyzer project directory.

4. Your Streamlit Application Code (housing.py)

5. Run the Application
Once you have placed housing.py and the data/corrected_csv.csv file in their respective locations within the syracuse_rent_analyzer directory, open your Anaconda Prompt, navigate to the syracuse_rent_analyzer folder, and run:

streamlit run housing.py
