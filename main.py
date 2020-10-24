import pandas as pd
import plotly.express as px
import pickle

grouped_shots_df = pd.read_csv('srcdata/league_shots_by_dist.csv')

fig = px.scatter(grouped_shots_df, x="avg_dist", y="shots_accuracy", size="shots_counts", color='shot_type', size_max=25)
fig.show()