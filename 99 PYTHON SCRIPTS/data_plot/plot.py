import pandas as pd
import plotly.graph_objects as go

from data_plot.plot_style import style as stl
from data_plot.plot_disp import display

def plot(filename, X, Y, type='line', title='title', X_label='', Y_label='', X_unit='', Y_unit='', style='display', legend = None, **kwargs):
    """
    Plot the data from a CSV file using Plotly graph objects and styles it according to the specified parameters.

    Parameters:
    filename (str): The path to the CSV file.
    X (list(str)): The column name for the X-axis data.
    Y (list(str)): The columns names for the Y-axis data.
    type (str, optional): The type of plot to generate. Defaults to 'line'.
    title (str, optional): The title of the plot. Defaults to 'title'.
    X_label (str, optional): The label for the X-axis. Defaults to ''.
    Y_label (str, optional): The label for the Y-axis. Defaults to ''.
    Y_unit (str, optional): The unit of measurement for the Y-axis data. Defaults to ''.
    X_unit (str, optional): The unit of measurement for the X-axis data. Defaults to ''.
    style (str, optional): The style of the plot. Defaults to 'display'.
    legend (list, optional): The legend labels for the data. Defaults to None.
    **kwargs: Additional keyword arguments to be passed to the plotting function.
    
    Raises:
    ValueError: If an invalid plot type is specified.

    Returns:
    None
    """
    data = pd.read_csv(filename)
    data['Time'] = pd.to_datetime(data['Time'])
    
    if type == 'line':
        plt_obj = _plot_line(data, X, Y, legend=legend)
    elif type == 'areas':
        plt_obj = _plot_areas(data, X, Y, legend=legend)
    else:
        raise ValueError("Invalid plot type")
    
    stl(plt_obj, title=title, style=style, X_label=X_label, Y_label=Y_label, 
        X_unit=X_unit, Y_unit=Y_unit, **kwargs)
    display(plt_obj, style)


def _plot_line(data, X, Y, legend=None):
    """
    Plot a line graph using Plotly graph objects.

    Parameters:
    data (pandas.DataFrame): The data to be plotted.
    Y (str): The columns names for the Y-axis data.
    X (str): The column name for the X-axis data.
    legend (list, optional): The legend labels for the data. Defaults to None.

    Returns:
    plotly.graph_objects.Figure: The plotly figure object.
    """
    fig = go.Figure()
    for x in X:
        for i in range(len(Y)):
            try:
                fig.add_trace(go.Scatter(x=data[x], y=data[Y[i]], mode='lines', name=legend[i]))
            except TypeError:
                fig.add_trace(go.Scatter(x=data[x], y=data[Y[i]], mode='lines'))
    return fig

def _plot_areas(data, X, Y, legend=None):
    """
    Plot a stacked areas graph using Plotly graph objects.

    Parameters:
    data (pandas.DataFrame): The data to be plotted.
    Y (str): The columns names for the Y-axis data.
    X (str): The column name for the X-axis data.
    legend (list, optional): The legend labels for the data. Defaults to None.

    Returns:
    plotly.graph_objects.Figure: The plotly figure object.
    """
    fig = go.Figure()
    for x in X:
        for i in range(len(Y)):
            try:
                fig.add_trace(go.Scatter(x=data[x], y=data[Y[i]], mode='lines', stackgroup='one', name=legend[i]))
            except TypeError:
                fig.add_trace(go.Scatter(x=data[x], y=data[Y[i]], mode='lines', stackgroup='one'))
    
    return fig
