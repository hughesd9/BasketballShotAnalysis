import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
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