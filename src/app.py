from dash import html, dcc
from dash.dependencies import Input, Output

from device_app.data import get_data
from device_app.main import server, app
from device_app.views.piechart import Piechart
from device_app.views.show import Show
from device_app.views.menu import make_menu_layout

from flask import redirect, render_template, request
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

@server.route('/')

def home():
    # if request.method == 'POST':
    #     if request.form.get('action1') == 'vis':
    #         render_dashboard()
    # elif request.method == 'GET':
    #     return render_template('home.html')
    
    return render_template('home.html')

@server.route('/visualization/')
def render_dashboard():
    return redirect('/dash1')

# Create data
df = get_data()

# Instantiate custom views
show = Show("show", df)
piechart_1 = Piechart("piechart-energy", df)
piechart_2 = Piechart("piechart-price", df)

# Define layout
app.layout = html.Div(
    id = "app-container",
    children = [
        # Left column: Define menu in app
        html.Div(
            id = "left-column",
            className = "three columns",
            children = make_menu_layout(False)
        ),

        # Right column: Define 2 tabs/pages in app
        html.Div(
            id = "right-column",
            className = "nine columns",
            children = [
                dcc.Tabs(
                    id = 'tab-aggregator',
                    value = 'view',
                    children = [
                        dcc.Tab(label = 'Show View', value = 'view'),
                        dcc.Tab(label = 'Pie Chart View', value = 'pie-view')
                    ]
                ),
                # TODO make it fill the rest of the page
                html.Div(id = 'tabs-content')
            ],
        ),
    ],
)

# Generate show in the 1st page of app
@app.callback(
    Output("show", "children"),
    Input("past-selector-dropdown-1", "value"),
)
def update_show(data_needed):
    return show.update(data_needed)

# Generate piechart-energy in the 1st page of app
@app.callback(
    Output("piechart-energy", "figure"),
    Input("past-selector-dropdown-2", "value")
)
def update_pie_1(data_needed):
    return piechart_1.update(data_needed, "energy")

# Generate piechart-price in the 1st page of app
@app.callback(
    Output("piechart-price", "figure"),
    Input("past-selector-dropdown-2", "value")
)
def update_pie_2(data_needed):
    return piechart_2.update(data_needed, "price")


# Generate menu on the left side of the app
@app.callback(
    Output('tabs-content', 'children'),
    Output('left-column', 'children'),
    Input('tab-aggregator', 'value')
)
# Update menu based on the type of chart/view chosen
def update_view(tab):
    if tab == 'view':
        return html.Div([show]), make_menu_layout(tab)    
    elif tab == 'pie-view':
        return html.Div([piechart_1, piechart_2]), make_menu_layout(tab)

entire_app = DispatcherMiddleware(server, {
    '/dash1': app.server
})

if __name__ == '__main__':
    # entire_app.run_server(debug = False, dev_tools_ui = False, use_reloader = True, host = "127.0.0.1", port = "8050")
    run_simple('127.0.0.1', 8050, entire_app, use_reloader = True, use_debugger = True)
    
server = app.server