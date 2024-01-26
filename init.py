import os

# This script creates the folders needed for the project
# You wil have to download raw data to use the project after this (see README.md)

# Create "00 RAW DATA" folder
raw_data_folder = "00 RAW DATA"
os.makedirs(raw_data_folder, exist_ok=True)

# Create "01 PROCESSED DATA" folder
processed_data_folder = "01 PROCESSED DATA"
os.makedirs(processed_data_folder, exist_ok=True)
