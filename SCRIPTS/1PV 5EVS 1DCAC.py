from data_processor.rawprocessor import process_csv
from data_plot.plot import plot
from data_processor.data_filter import filter_csv
import structure as st

FILE_NAME = "1PV 5EVS 1DCAC.csv"
RAW_FILE_PATH = st.RAW_DATA_PATH + FILE_NAME
PROCESSED_FILE_PATH = st.PROCESSED_DATA_PATH + FILE_NAME
FILTERED_EVS_FILE_PATH = st.FILTERED_DATA_PATH + "EV_filtered_" + FILE_NAME

# Processes the raw data and saves it in the processed data folder
process_csv(RAW_FILE_PATH, PROCESSED_FILE_PATH)

# Plots (from base data) :
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

#Processes EV3 data to keep only data with 50% < SOC < 92% to only plot data during charging
filter_csv(PROCESSED_FILE_PATH, 'EV_SoC3', 92, 'P_EVs3', '<', FILTERED_EVS_FILE_PATH)
filter_csv(FILTERED_EVS_FILE_PATH, 'EV_SoC3', 50, 'P_EVs3', '>', FILTERED_EVS_FILE_PATH)

# 5. 'P_EVs1', 'P_EVs2', 'P_EVs3', 'P_EVs4', and 'P_EVs5' vs 'U_DC' as a scatter plot
plot(FILTERED_EVS_FILE_PATH, ['U_DC'], ['P_EVs3'], 
     type='scatter', title='P_EVs1, P_EVs2, P_EVs3, P_EVs4, and P_EVs5 vs U_DC', 
     Y_label='Power', Y_unit='W', X_label='bus Voltage', X_unit='V', style='display')