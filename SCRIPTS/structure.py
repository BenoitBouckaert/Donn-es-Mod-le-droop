#This files defines constants about the structure of the project

#Path to the raw data folder
RAW_DATA_PATH = "./00 RAW DATA/"

#Path to the processed data folder
PROCESSED_DATA_PATH = "./01 PROCESSED DATA/"

#Path to the filtered data folder
FILTERED_DATA_PATH = "./02 FILTERED DATA/"

def create_folders():
    """
    Create the necessary folders for the project.
    """
    import os
    if not os.path.exists(RAW_DATA_PATH):
        os.makedirs(RAW_DATA_PATH)
    if not os.path.exists(PROCESSED_DATA_PATH):
        os.makedirs(PROCESSED_DATA_PATH)
    if not os.path.exists(FILTERED_DATA_PATH):
        os.makedirs(FILTERED_DATA_PATH)