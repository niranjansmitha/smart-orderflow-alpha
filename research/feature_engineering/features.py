import numpy as np

def add_features(df):

    # Returns
    df['ret1'] = df['mid_price'].pct_change(1)
    df['ret5'] = df['mid_price'].pct_change(5)

    # Volatility
    df['vol10'] = df['ret1'].rolling(10).std()
    df['vol30'] = df['ret1'].rolling(30).std()

    # Price pressure (microstructure proxy)
    df['pressure'] = (df['close'] - df['low']) - (df['high'] - df['close'])

    # Trend strength
    df['trend10'] = df['mid_price'].rolling(10).mean()
    df['trend30'] = df['mid_price'].rolling(30).mean()

    df['trend_ratio'] = df['trend10'] / df['trend30']

    return df
