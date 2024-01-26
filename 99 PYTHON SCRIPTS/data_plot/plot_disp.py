import plotly.io as pio

def display(plot, style='display'):
    """
    Display the plot according to the specified parameters.

    Parameters:
    plot (plotly.graph_objects.Figure): The plot object to be displayed.
    style (str, optional): The style to be applied to the plot. Defaults to 'display'.

    Returns:
    None
    """
    if style == 'display':
        _display_display(plot)
    elif style == 'printing':
        _display_printing(plot)

def _display_display(plot):
    pio.show(plot, renderer="browser")

def _display_printing(plot):
    pass