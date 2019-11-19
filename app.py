import dash
import dash_core_components as dcc
import dash_html_components as html

print(dcc.__version__) # 0.6.0 or above is required

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page-2'),

    # content will be rendered in this element
    html.Div(id='page-content'),
    html.Div(id='my-indicator'),
    html.Button("Click-Me", id="click-me", n_clicks=0),
    html.Button("Reset", id="reset-click-me"),

]
)


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    return html.Div([
        html.H3('You are on page {}'.format(pathname))
    ])

@app.callback(dash.dependencies.Output('my-indicator','children'),
[dash.dependencies.Input('click-me','n_clicks')])
def update_click_count(count):
    return html.Div([html.P("You clicked it {} times".format(count))])

@app.callback(dash.dependencies.Output('click-me','n_clicks'),
[dash.dependencies.Input('reset-click-me','n_clicks')])
def reset_click_count(count):
    return 0

if __name__ == '__main__':
    app.run_server(debug=True)