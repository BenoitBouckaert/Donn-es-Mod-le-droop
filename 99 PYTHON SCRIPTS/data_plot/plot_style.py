def style(plt_obj, style='display', title='title', X_label='', Y_label='', X_unit='', Y_unit='', **kwargs):
    """
    Style the plot according to the specified parameters.

    Parameters:
    plt_obj (plotly.Figure): The plot object to be styled.
    style (str, optional): The style to be applied to the plot. Defaults to 'display'.
    title (str, optional): The title of the plot. Defaults to 'title'.
    X_label (str, optional): The label for the x-axis. Defaults to ''.
    Y_label (str, optional): The label for the y-axis. Defaults to ''.
    Y_unit (str, optional): The unit of the y-axis. Defaults to ''.
    X_unit (str, optional): The unit of the x-axis. Defaults to ''.
    legend (list, optional): The legend labels for the data. Defaults to [''].

    Returns:
    None
    """
    
    lab_x = X_label +  (f' ({X_unit})' ) if X_unit != '' else ''
    lab_y = Y_label +  (f' ({Y_unit})' ) if Y_unit != '' else ''


    plt_obj.update_layout(
        title=title,
        xaxis_title=lab_x,
        yaxis_title=lab_y
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