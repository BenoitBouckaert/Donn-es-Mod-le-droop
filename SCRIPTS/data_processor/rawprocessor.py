import pandas as pd

def process_csv(input_file, output_file, start_time='07:30:00', date='2021-11-10'):
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
    df['Time'] = pd.to_datetime(df['Time'], unit='s') + pd.Timedelta(start_time) + _date_to_timedelta(date)
    df.to_csv(output_file, index=False)

def _date_to_timedelta(date):
    """
    Convert the date to a timedelta object, knowing that the base date is 1970-01-01.

    Args:
        date (str): The date to convert in format 'YYYY-MM-DD'.

    Returns:
        pd.Timedelta: The date as a timedelta object.
    """
    yr = int(date[:4])
    mth = int(date[5:7])
    day = int(date[8:10])

    delta = pd.Timedelta(day, unit='d')
    delta += pd.Timedelta(_months_to_days(mth, _isYearBissexile(yr)), unit='d')
    delta += pd.Timedelta(_years_to_days(yr), unit='d')

    return pd.Timedelta(delta)

def _months_to_days(months, isYearBissexile=False):
    """
    Convert the months's number to the number of days.

    Args:
        months (int): The monts's number to convert.

    Returns:
        int: The number of days.
    """
    switcher = {
        0: 0,
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30
    }
    if isYearBissexile:
        switcher[2] = 29
    days=0
    for i in range(1, months):
        days += switcher[i]
    
    return days

def _years_to_days(years):
    """
    Convert the number of years to the number of days.

    Args:
        years (int): The number of years to convert.

    Returns:
        int: The number of days.
    """
    days=0
    for i in range(1970, years):
        days += 365
        if _isYearBissexile(i):
            days += 1
    return days

def _isYearBissexile(year):
    """
    Check if the year is bissexile.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is bissexile, False otherwise.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)