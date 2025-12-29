import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    df.columns = [c.lower().strip() for c in df.columns]

    df['timestamp'] = pd.to_datetime(
        df['date'] + ' ' + df['time'],
        format='%d-%m-%Y %H:%M:%S'
    )

    df = df.sort_values('timestamp').reset_index(drop=True)
    return df
