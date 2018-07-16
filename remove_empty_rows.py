import pandas as pd
df = pd.read_csv('trail.csv')
df.to_csv('trail_removed.csv', index=False)
