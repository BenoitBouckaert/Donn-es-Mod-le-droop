import pandas as pd

def process_csv(input_file, output_file):
    """
    Process the input CSV file by converting the 'Time' column to the desired 
    format and setting the date to November 10th, 2021.

    Args:
        input_file (str): The path to the input CSV file.
        output_file (str): The path to the output CSV file.

    Returns:
        None
    """
    df = pd.read_csv(input_file)
    df['Time'] = df['Time'].str.replace(' sec', '')
    df['Time'] = pd.to_datetime(df['Time'], unit='s') + pd.Timedelta('07:30:00')
    df['Time'] = df['Time'].apply(lambda x: x.replace(year=2021, month=11, day=10))
    df.to_csv(output_file, index=False)
