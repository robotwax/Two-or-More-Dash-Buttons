# -*- coding: UTF-8 -*-

import json

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
import numpy.ma as ma
import plotly.plotly as py


import plotly.plotly as py
import plotly.graph_objs as go

from plotly.graph_objs import *

app = dash.Dash(__name__)

app.config['suppress_callback_exceptions'] = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

server = app.server



styles = {
    'hr': { 
    'display': 'block',
    'margin-top': '0.1rem',
    'margin-bottom': '0.1rem',
    'margin-left': 'auto',
    'margin-right': 'auto',
    'border-style': 'inset',
    'border-width': '0.1rem'}
}


app.layout = html.Div(children=
      html.Div([
            html.Div([
                  html.H1('Rainbow Calendar C-14',
                  className = "six columns"),
                  html.H4(gc,
                  className = "six columns", style={'float': 'left', 'margin-left': 0},
                  ),
            ], className = "row"),          
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Hr(style=styles['hr']),
            html.Div([
                html.Div([
                    html.Button('1980-1984', id='btn-1', n_clicks = 0, style={'background-color': 'rgb(19, 24, 26)', 'color': 'white', 'width': '12.5%'}),
                    html.Button('1984-1987', id='btn-2', n_clicks = 0, style={'background-color': 'rgb(19, 24, 26)', 'color': 'white', 'width': '12.5%'}),
                    html.Button('1987-1991', id='btn-3', n_clicks = 0, style={'background-color': 'rgb(19, 24, 26)', 'color': 'white', 'width': '12.5%'}),
                    html.Button('1991-1995', id='btn-4', n_clicks = 0, style={'background-color': 'rgb(19, 24, 26)', 'color': 'white', 'width': '12.5%'}),
                    html.Button('1995-1999', id='btn-5', n_clicks = 0, style={'background-color': 'rgb(19, 24, 26)', 'color': 'white', 'width': '12.5%'}),
                    html.Button('1999-2003', id='btn-6', n_clicks = 0, style={'background-color': 'rgb(19, 24, 26)', 'color': 'white', 'width': '12.5%'}),
                    html.Button('2003-2006', id='btn-7', n_clicks = 0, style={'background-color': 'rgb(19, 24, 26)', 'color': 'white', 'width': '12.5%'}),
                    html.Button('2006-2010', id='btn-8', n_clicks = 0, style={'background-color': 'rgb(19, 24, 26)', 'color': 'white', 'width': '12.5%'}),
                ], className='row'),
            html.Div(children=None, id='graph-output'),
            ], className='row'),
                html.Div([
                    html.Button('Reset', id='reset', n_clicks = 0, style={'background-color': 'rgb(19, 24, 26)', 'color': 'white', 'width': '12.5%'}),
                ], className='row'),
            html.Br(),
            html.Hr(style=styles['hr']),
      ]),    
)    


@app.callback(dash.dependencies.Output('graph-output', 'children'),
[dash.dependencies.Input('reset', 'n_clicks'),
dash.dependencies.Input('btn-1', 'n_clicks'),
dash.dependencies.Input('btn-2', 'n_clicks'),
dash.dependencies.Input('btn-3', 'n_clicks'),
dash.dependencies.Input('btn-4', 'n_clicks'),
dash.dependencies.Input('btn-5', 'n_clicks'),
dash.dependencies.Input('btn-6', 'n_clicks'),
dash.dependencies.Input('btn-7', 'n_clicks'),
dash.dependencies.Input('btn-8', 'n_clicks')])
def func(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, reset):
    clicks2= np.array([int(btn1), int(btn2), int(btn3), int(btn4), int(btn5), int(btn6), int(btn7), int(btn8)])
    sum_clicks2=clicks2.sum()
    sum_mod = sum_clicks2 % 2
    clicks3 = clicks2.tolist()
    button= nd.array(['button1', 'button2', 'button3', 'button4', 'button5', 'button6', 'button7', 'button8'])
    if sum_clicks2 == 0:
        with open('mod2.txt', 'w') as outfile:
            json.dump(clicks3, outfile)
        with open('mod1.txt', 'w') as outfile:
            json.dump(clicks3, outfile)
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 1'
                }
            }
            return figure
    elif sum_mod == 1:
        with open('mod1.txt', 'w') as outfile:
            json.dump(clicks3, outfile)
        with open('mod2.txt') as json_file:  
            mod2 = json.load(json_file)
        mod2 = np.array(mod2)
        diff2 = mod2 + clicks2
        diff2 = diff2 % 2
        max_clicks2= max((x) for x in diff2)
        elimin8 = [diff2 != max_clicks2]
        mask2 = ma.masked_array(button, elimin8)
        mask2=mask2.tolist()
        result= [i for i in mask2 if i is not None]
        if result[0] == 'button1':
            json.dump(clicks3, outfile)
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 1'
                }
            }
            return figure
        elif result[0] == 'button2':
            json.dump(clicks3, outfile)
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [1, 4, 5], 'type': 'line', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [1, 3, 6], 'type': 'bar', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 2'
                }
            }
            return figure
        elif result[0] == 'button3':
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 6], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 3'
                }
            }
            return figure
        elif result[0] == 'button4':
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [2, 3, 5], 'type': 'line', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [6, 7, 2], 'type': 'line', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 4'
                }
            }
            return figure
        elif result[0] == 'button5':
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 5'
                }
            }
            return figure
        elif result[0] == 'button6':
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [3, 4, 5], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [7, 8, 1], 'type': 'line', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 6'
                }
            }
            return figure
        elif result[0] == 'button7':            	
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 7'
                }
            }
            return figure
    elif sum_mod == 0:
        with open('mod2.txt', 'w') as outfile:
            json.dump(clicks3, outfile)
        with open('mod1.txt') as json_file:  
            mod1 = json.load(json_file)
        mod1 = np.array(mod1)
        diff2 = mod1 + clicks2
        diff2 = diff2 % 2
        max_clicks2= max((x) for x in diff2)
        elimin8 = [diff2 != max_clicks2]
        mask2 = ma.masked_array(button, elimin8)
        mask2=mask2.tolist()
        result= [i for i in mask2 if i is not None]
        if result[0] == 'button1':
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 1'
                }
            }
            return figure
        elif result[0] == 'button2':
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [1, 4, 5], 'type': 'line', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [1, 3, 6], 'type': 'bar', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 2'
                }
            }
            return figure
        elif result[0] == 'button3':
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 6], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 3'
                }
            }
            return figure
        elif result[0] == 'button4':
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [2, 3, 5], 'type': 'line', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [6, 7, 2], 'type': 'line', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 4'
                }
            }
            return figure
        elif result[0] == 'button5':
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 5'
                }
            }
            return figure
        elif result[0] == 'button6':
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [3, 4, 5], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [7, 8, 1], 'type': 'line', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 6'
                }
            }
            return figure
        elif result[0] == 'button7':            	
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 7'
                }
            }
            return figure
        else:
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
             'layout': {
                 'title': 'Dash Data Visualization 8'
                }
            }
            return figure



if __name__ == '__main__':
    app.run_server(debug=True)

