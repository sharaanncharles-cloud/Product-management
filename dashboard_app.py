import pandas as pd
from dash import Dash, dcc, html, dash_table, Input, Output
from sqlalchemy import create_engine
import plotly.express as px
from urllib.parse import quote_plus
from flask import Response

# Database credentials
db_user = "root"
db_password = quote_plus("Emma@123")
db_host = "localhost"
db_name = "product_management"

# Create SQLAlchemy engine
engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:3306/{db_name}")

# Load views
df_features = pd.read_sql("SELECT * FROM v_feature_summary", engine)
df_tasks = pd.read_sql("SELECT * FROM v_task_summary", engine)
df_releases = pd.read_sql("SELECT * FROM v_release_summary", engine)

# Initialize Dash app
app = Dash(__name__)
server = app.server
app.title = "Product Management Dashboard"

# Layout
app.layout = html.Div([
    html.H1("Product Management Dashboard", style={'textAlign': 'center'}),

    dcc.Tabs([
        # ---------------------- Features Tab ----------------------
        dcc.Tab(label='Features', children=[
            html.Div([
                html.Div([
                    html.H4("Total Features"),
                    html.P(f"{len(df_features)}")
                ], style={"width": "25%", "display": "inline-block"}),

                html.Div([
                    html.H4("Completed Features"),
                    html.P(f"{df_features[df_features['feature_status'] == 'Completed'].shape[0]}")
                ], style={"width": "25%", "display": "inline-block"}),
            ], style={"display": "flex"}),

            html.Label("Filter by Feature Status:"),
            dcc.Dropdown(
                id='feature-status-dropdown',
                options=[{"label": s, "value": s} for s in df_features["feature_status"].dropna().unique()],
                value=None,
                placeholder="Select Status"
            ),

            html.Label("Filter by Product Manager:"),
            dcc.Dropdown(
                id='pm-feature-dropdown',
                options=[{"label": pm, "value": pm} for pm in df_features["product_manager"].dropna().unique()],
                value=None,
                placeholder="Select Product Manager"
            ),

            dcc.Graph(id='features-graph'),

            dash_table.DataTable(
                id='features-table',
                columns=[{"name": i, "id": i} for i in df_features.columns],
                page_size=10,
                style_table={'overflowX': 'auto'},
                filter_action='native',
                sort_action='native',
            ),

            html.Br(),
            html.A("Download Excel", href="/download_features_xlsx", target="_blank")
        ]),

        # ---------------------- Tasks Tab ----------------------
        dcc.Tab(label='Tasks', children=[
            html.Div([
                html.Div([
                    html.H4("Total Tasks"),
                    html.P(f"{len(df_tasks)}")
                ], style={"width": "25%", "display": "inline-block"}),

                html.Div([
                    html.H4("Completed Tasks"),
                    html.P(f"{df_tasks[df_tasks['status'] == 'Completed'].shape[0]}")
                ], style={"width": "25%", "display": "inline-block"}),
            ], style={"display": "flex"}),

            html.Label("Filter by Priority:"),
            dcc.Dropdown(
                id='priority-dropdown',
                options=[{"label": p, "value": p} for p in df_tasks["priority"].dropna().unique()],
                value=None,
                placeholder="Select Priority"
            ),

            html.Label("Filter by Product Manager:"),
            dcc.Dropdown(
                id='pm-task-dropdown',
                options=[{"label": pm, "value": pm} for pm in df_tasks["product_manager"].dropna().unique()],
                value=None,
                placeholder="Select Product Manager"
            ),

            dcc.Graph(id='tasks-graph'),

            dash_table.DataTable(
                id='tasks-table',
                columns=[{"name": i, "id": i} for i in df_tasks.columns],
                page_size=10,
                style_table={'overflowX': 'auto'},
                filter_action='native',
                sort_action='native',
            ),

            html.Br(),
            html.A("Download Excel", href="/download_tasks_xlsx", target="_blank")
        ]),

        # ---------------------- Releases Tab ----------------------
        dcc.Tab(label='Releases', children=[
            html.Div([
                html.Div([
                    html.H4("Total Releases"),
                    html.P(f"{df_releases['release_name'].nunique()}")
                ], style={"width": "25%", "display": "inline-block"}),

                html.Div([
                    html.H4("Total Features Released"),
                    html.P(f"{df_releases['feature_title'].nunique()}")
                ], style={"width": "25%", "display": "inline-block"}),
            ], style={"display": "flex"}),

            dcc.Graph(
                figure=px.pie(df_releases, names="release_name", title="Features per Release")
            ),

            dash_table.DataTable(
                data=df_releases.to_dict('records'),
                columns=[{"name": i, "id": i} for i in df_releases.columns],
                page_size=10,
                style_table={'overflowX': 'auto'},
                filter_action='native',
                sort_action='native',
            ),

            html.Br(),
            html.A("Download Excel", href="/download_releases_xlsx", target="_blank")
        ]),
    ])
])

# ---------------------- Callbacks ----------------------

@app.callback(
    Output('features-graph', 'figure'),
    Output('features-table', 'data'),
    Input('feature-status-dropdown', 'value'),
    Input('pm-feature-dropdown', 'value')
)
def update_feature_tab(status, pm):
    df = df_features
    if status:
        df = df[df["feature_status"] == status]
    if pm:
        df = df[df["product_manager"] == pm]
    fig = px.bar(df, x="feature_title", color="feature_status", title="Features by Title & Status")
    return fig, df.to_dict('records')

@app.callback(
    Output('tasks-graph', 'figure'),
    Output('tasks-table', 'data'),
    Input('priority-dropdown', 'value'),
    Input('pm-task-dropdown', 'value')
)
def update_task_tab(priority, pm):
    df = df_tasks
    if priority:
        df = df[df["priority"] == priority]
    if pm:
        df = df[df["product_manager"] == pm]
    fig = px.bar(df, x="feature_title", color="status", title="Tasks by Feature & Status")
    return fig, df.to_dict('records')

# ---------------------- Excel Export ----------------------

@app.server.route('/download_features_xlsx')
def download_features_xlsx():
    output = pd.ExcelWriter('features.xlsx', engine='xlsxwriter')
    df_features.to_excel(output, index=False, sheet_name='Features')
    output.close()
    with open('features.xlsx', 'rb') as f:
        return Response(f.read(), mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        headers={"Content-Disposition": "attachment;filename=features.xlsx"})

@app.server.route('/download_tasks_xlsx')
def download_tasks_xlsx():
    output = pd.ExcelWriter('tasks.xlsx', engine='xlsxwriter')
    df_tasks.to_excel(output, index=False, sheet_name='Tasks')
    output.close()
    with open('tasks.xlsx', 'rb') as f:
        return Response(f.read(), mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        headers={"Content-Disposition": "attachment;filename=tasks.xlsx"})

@app.server.route('/download_releases_xlsx')
def download_releases_xlsx():
    output = pd.ExcelWriter('releases.xlsx', engine='xlsxwriter')
    df_releases.to_excel(output, index=False, sheet_name='Releases')
    output.close()
    with open('releases.xlsx', 'rb') as f:
        return Response(f.read(), mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        headers={"Content-Disposition": "attachment;filename=releases.xlsx"})

# ---------------------- Run App ----------------------

if __name__ == '__main__':
    app.run(debug=True)
