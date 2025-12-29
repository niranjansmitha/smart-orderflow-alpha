def add_label(df, horizon=5):
    df['future_mid'] = df['mid_price'].shift(-horizon)
    df['y'] = (df['future_mid'] - df['mid_price']) / df['mid_price']
    return df
