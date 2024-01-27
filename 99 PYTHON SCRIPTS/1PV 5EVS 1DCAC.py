from data_processor.rawprocessor import process_csv
from data_plot.plot import plot
import structure as st

FILE_NAME = "1PV 5EVS 1DCAC.csv"
RAW_FILE_PATH = st.RAW_DATA_PATH + FILE_NAME
PROCESSED_FILE_PATH = st.PROCESSED_DATA_PATH + FILE_NAME

# Processes the raw data and saves it in the processed data folder
process_csv(RAW_FILE_PATH, PROCESSED_FILE_PATH)

# Plots :
# 1. 'U_DC' vs 'Time' as a line graph
plot(PROCESSED_FILE_PATH, ['Time'], ['U_DC'], type='line', title='U_DC vs Time', 
     Y_label='DC bus Voltage' ,Y_unit='V', style='display')

# 2. 'P_acdc', 'P_PV', and 'P_EVs' vs 'Time' as a line graph
plot(PROCESSED_FILE_PATH, ['Time'], ['P_acdc', 'P_PV', 'P_EVs'], 
     type='line', title='P_acdc, P_PV, and P_EVs vs Time', Y_label='Power', 
     Y_unit='W', style='display', legend=['$P_{ACDC}$', '$P_{PV}$', '$P_{EVs}$'])

# 3. 'P_EVs1', 'P_EVs2', 'P_EVs3', 'P_EVs4', and 'P_EVs5' vs 'Time' as stacked area graphs
plot(PROCESSED_FILE_PATH, ['Time'], ['P_EVs1', 'P_EVs2', 'P_EVs3', 'P_EVs4', 'P_EVs5'], 
     type='areas', title='P_EVs1, P_EVs2, P_EVs3, P_EVs4, and P_EVs5 vs Time', 
     Y_label='Power', Y_unit='W', style='display', legend=['$P_{EVs_1}$', '$P_{EVs_2}$', 
                                                           '$P_{EVs_3}$', '$P_{EVs_4}$', 
                                                           '$P_{EVs_5}$'])