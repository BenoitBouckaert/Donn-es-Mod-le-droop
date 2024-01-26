import pandas as pd
import plotly.graph_objects as go

from data_plot.plot_style import style as stl
from data_plot.plot_disp import display

def plot(filename, X, Y, type='line', title='title', X_label='', Y_label='', X_unit='', Y_unit='', style='display', **kwargs):
    """
    Plot the data from a CSV file using Plotly graph objects and styles it according to the specified parameters.

    Parameters:
    filename (str): The path to the CSV file.
    X (str): The column name for the X-axis data.
    Y (str): The columns names for the Y-axis data.
    type (str, optional): The type of plot to generate. Defaults to 'line'.
    title (str, optional): The title of the plot. Defaults to 'title'.
    X_label (str, optional): The label for the X-axis. Defaults to ''.
    Y_label (str, optional): The label for the Y-axis. Defaults to ''.
    Y_unit (str, optional): The unit of measurement for the Y-axis data. Defaults to ''.
    X_unit (str, optional): The unit of measurement for the X-axis data. Defaults to ''.
    style (str, optional): The style of the plot. Defaults to 'display'.
    **kwargs: Additional keyword arguments to be passed to the plotting function.
    
    Raises:
    ValueError: If an invalid plot type is specified.

    Returns:
    None
    """
    data = pd.read_csv(filename)
    data['Time'] = pd.to_datetime(data['Time'])
    
    if type == 'line':
        plt_obj = _plot_line(data, X, Y)
    elif type == 'areas':
        plt_obj = _plot_areas(data, X, Y)
    else:
        raise ValueError("Invalid plot type")
    
    stl(plt_obj, title, X_label, Y_label, X_unit, Y_unit, style, **kwargs)
    display(plt_obj, style)


def _plot_line(data, X, Y):
    """
    Plot a line graph using Plotly graph objects.

    Parameters:
    data (pandas.DataFrame): The data to be plotted.
    Y (str): The columns names for the Y-axis data.
    X (str): The column name for the X-axis data.

    Returns:
    plotly.graph_objects.Figure: The plotly figure object.
    """
    fig = go.Figure()
    for x in X:
        for y in Y:
            fig.add_trace(go.Scatter(x=data[x], y=data[y], mode='lines'))
    return fig

def _plot_areas(data, X, Y):
    """
    Plot a stacked areas graph using Plotly graph objects.

    Parameters:
    data (pandas.DataFrame): The data to be plotted.
    Y (str): The columns names for the Y-axis data.
    X (str): The column name for the X-axis data.

    Returns:
    plotly.graph_objects.Figure: The plotly figure object.
    """
    fig = go.Figure()
    for y in Y:
        fig.add_trace(go.Scatter(x=data[X], y=data[y], mode='lines', stackgroup='one'))
    
    return fig
