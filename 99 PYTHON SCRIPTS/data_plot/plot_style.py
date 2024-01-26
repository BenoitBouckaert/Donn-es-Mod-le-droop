def style(plt_obj, style='display', title='title', X_label='', Y_label='', X_unit='', Y_unit='', **kwargs):
    """
    Style the plot according to the specified parameters.

    Parameters:
    plt_obj (plotly.Figure): The plot object to be styled.
    style (str, optional): The style to be applied to the plot. Defaults to 'display'.
    title (str, optional): The title of the plot. Defaults to 'title'.
    Y_unit (str, optional): The unit of the y-axis. Defaults to ''.
    X_unit (str, optional): The unit of the x-axis. Defaults to ''.

    Returns:
    None
    """
    
    plt_obj.update_layout(
        title=title,
        xaxis_title=X_label + ' ({' + X_unit + '})',
        yaxis_title=Y_label + ' ({' + Y_unit + '})',
    )

    if style == 'display':
        _style_display()
    elif style == 'printing':
        _style_printing()

def _style_printing():
    #TODO: Style the plot for printing
    pass

def _style_display():
    #TODO: Style the plot for display
    pass