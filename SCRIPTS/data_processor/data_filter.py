import pandas as pd

def filter_csv(file_path, column_filter, value, column_data, comparison_operator, output_file_path):
    df = pd.read_csv(file_path)
    
    if comparison_operator == '<':
        df.loc[df[column_filter] >= value, column_data] = None
    elif comparison_operator == '>':
        df.loc[df[column_filter] <= value, column_data] = None
    elif comparison_operator == '<=':
        df.loc[df[column_filter] > value, column_data] = None
    elif comparison_operator == '>=':
        df.loc[df[column_filter] < value, column_data] = None
    elif comparison_operator == '==':
        df.loc[df[column_filter] != value, column_data] = None
    elif comparison_operator == '!=':
        df.loc[df[column_filter] == value, column_data] = None
    else:
        raise ValueError("Invalid comparison operator")
    
    df.to_csv(output_file_path, index=False)
