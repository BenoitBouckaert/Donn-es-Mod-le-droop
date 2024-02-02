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
     Y_label='bus Voltage', Y_unit='V', X_label='Time', style='display')

# 2. 'P_acdc', 'P_PV', and 'P_EVs' vs 'Time' as a line graph
plot(PROCESSED_FILE_PATH, ['Time'], ['P_acdc', 'P_PV', 'P_EVs'], 
     type='line', title='P_acdc, P_PV, and P_EVs vs Time', Y_label='Power', 
     Y_unit='W', X_label='Time', style='display', legend=['$P_{ACDC}$', '$P_{PV}$', '$P_{EVs}$'])

# 3. 'P_EVs1', 'P_EVs2', 'P_EVs3', 'P_EVs4', and 'P_EVs5' vs 'Time' as stacked area graphs
plot(PROCESSED_FILE_PATH, ['Time'], ['P_EVs1', 'P_EVs2', 'P_EVs3', 'P_EVs4', 'P_EVs5'], 
     type='areas', title='P_EVs1, P_EVs2, P_EVs3, P_EVs4, and P_EVs5 vs Time', X_label='Time',
     Y_label='Power', Y_unit='W', style='display', legend=['$P_{EVs_1}$', '$P_{EVs_2}$', 
                                                           '$P_{EVs_3}$', '$P_{EVs_4}$', 
                                                           '$P_{EVs_5}$'])

# 4. 'P_ACDC' vs 'U_DC' as a scatter plot
plot(PROCESSED_FILE_PATH, ['U_DC'], ['P_acdc'], type='scatter', title='P_acdc vs U_DC', 
     Y_label='Power', Y_unit='W', X_label='bus Voltage', X_unit='V', style='display')

# 5. 'P_EVs1', 'P_EVs2', 'P_EVs3', 'P_EVs4', and 'P_EVs5' vs 'U_DC' as a scatter plot
plot(PROCESSED_FILE_PATH, ['U_DC'], ['P_EVs1', 'P_EVs2', 'P_EVs3', 'P_EVs4', 'P_EVs5'], 
     type='scatter', title='P_EVs1, P_EVs2, P_EVs3, P_EVs4, and P_EVs5 vs U_DC', 
     Y_label='Power', Y_unit='W', X_label='bus Voltage', X_unit='V', style='display', 
     legend=['$P_{EVs_1}$', '$P_{EVs_2}$', '$P_{EVs_3}$', '$P_{EVs_4}$', '$P_{EVs_5}$'])