from dash import dcc, html

from ..config import past_lst


def generate_description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id = "description-card",
        children = [
            html.H5("Energy Consumption Dashboard"),
            html.Div(
                id = "intro",
            ),
        ],
    )


def generate_control_card(viewType):
    """

    :return: A Div containing controls for graphs.
    """
    id_name = ''
    if viewType == 'view':
        id_name = 'past-selector-dropdown-1'
    elif viewType == 'pie-view':
        id_name = 'past-selector-dropdown-2'
    return html.Div(
        id="control-card",
        children = [
            html.H6("Customize: "),
            html.Br(),
            html.Label('Select time:'),
            dcc.Dropdown(
                id = id_name,
                options = [{"label": i, "value": i} for i in past_lst],
                value = past_lst[0]
            ),
            dcc.Link(
                html.Button('Home Page'), 
                href = '/', 
                refresh = True
            ),
        ], 
        style = {"textAlign": "float-left"}
    )

# Return the left column
def make_menu_layout(viewType):
    return [generate_description_card(), generate_control_card(viewType)]
