import structure as st
from data_processor.rawprocessor import process_csv

FILE_NAME = "1PV 5EVS 1DCAC.csv"
RAW_FILE_PATH = st.RAW_DATA_PATH + FILE_NAME
PROCESSED_FILE_PATH = st.PROCESSED_DATA_PATH + FILE_NAME

process_csv(RAW_FILE_PATH, PROCESSED_FILE_PATH)

