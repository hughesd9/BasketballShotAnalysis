import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pickle

#grouped_shots_df = pd.read_csv('srcdata/league_shots_by_dist.csv')

#fig = px.scatter(grouped_shots_df, x="avg_dist", y="shots_accuracy", size="shots_counts", color='shot_type', size_max=25)
#fig.show()

with open('srcdata/league_hexbin_stats.pickle', 'rb') as f:
    league_hexbin_stats = pickle.load(f)
    
xlocs = league_hexbin_stats['xlocs']
ylocs = league_hexbin_stats['ylocs']
accs_by_hex = league_hexbin_stats['accs_by_hex']
freq_by_hex = league_hexbin_stats['freq_by_hex']

fig = go.Figure()
fig.add_trace(go.Scatter(x=xlocs, y=ylocs, mode='markers', name='markers', marker=dict(
    size=freq_by_hex, sizemode='area', sizeref=2. * max(freq_by_hex) / (11. ** 2), sizemin=2.5,
    color=accs_by_hex, line=dict(width=1, color='#333333'), symbol='hexagon',
)))

fig.show(config=dict(displayModeBar=False))

#definition to create court layout

def draw_plotly_court(fig, fig_width=600, margins=10):

    # From: https://community.plot.ly/t/arc-shape-with-path/7205/5
    def ellipse_arc(x_center=0.0, y_center=0.0, a=10.5, b=10.5, start_angle=0.0, end_angle=2 * np.pi, N=200, closed=False):
        t = np.linspace(start_angle, end_angle, N)
        x = x_center + a * np.cos(t)
        y = y_center + b * np.sin(t)
        path = f'M {x[0]}, {y[0]}'
        for k in range(1, len(t)):
            path += f'L{x[k]}, {y[k]}'
        if closed:
            path += ' Z'
        return path

    fig_height = fig_width * (470 + 2 * margins) / (500 + 2 * margins)
    fig.update_layout(width=fig_width, height=fig_height)

    #set axes ranges
    fig.update_xaxes(range=[-250 - margins, 250 + margins])
    fig.update_yaxes(range=[-52.5 - margins, 417.5 + margins])

    threept_break_y = 89.47765084
    three_line_col = "#777777"
    main_line_col = "#777777"


