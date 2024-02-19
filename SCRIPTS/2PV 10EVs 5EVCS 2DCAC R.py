from data_processor.rawprocessor import process_csv
from data_plot.plot import plot
from data_processor.data_filter import filter_csv
import structure as st

FILE_NAME = "2PV 10EVs 5EVCS 2DCAC R.csv"
RAW_FILE_PATH = st.RAW_DATA_PATH + FILE_NAME
PROCESSED_FILE_PATH = st.PROCESSED_DATA_PATH + FILE_NAME

# Processes the raw data and saves it in the processed data folder
process_csv(RAW_FILE_PATH, PROCESSED_FILE_PATH, start_time='05:00:00', date='2022-06-19')

# Plots (from base data) :
# 1. 'U_DC1' and 'U_DC2' vs 'Time' as a line graph
plot(PROCESSED_FILE_PATH, ['Time'], ['U_DC'], type='line', title='U_DC vs Time', 
     Y_label='bus Voltage', Y_unit='V', X_label='Time', style='display')

plot(PROCESSED_FILE_PATH, ['Time'], ['P_PV1', 'P_PV2'], type='line', title='P_PV1 + P_PV2 vs Time', 
     Y_label='Power', Y_unit='W', X_label='Time', style='display', legend=['$P_{PV1}$', '$P_{PV2}$'])

# 2. 'P_acdc1' + 'P_acdc2, 'P_PV1' + 'P_PV2', and 'P_EVs' vs 'Time' as a line graph
plot(PROCESSED_FILE_PATH, ['Time'], ['P_acdc1', 'P_acdc2', 'P_PV1', 'P_PV2', 'P_EVs'], 
     type='line', title='P_acdc1 + P_acdc2, P_PV1 + P_PV2, and P_EVs vs Time', Y_label='Power', 
     Y_unit='W', X_label='Time', style='display', legend=['$P_{ACDC1}$ + $P_{ACDC2}$', 
                                                           '$P_{PV1}$ + $P_{PV2}$', '$P_{EVs}$'])