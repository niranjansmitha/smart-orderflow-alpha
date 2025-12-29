def add_mid_price(df):
    df['mid_price'] = (df['high'] + df['low']) / 2
    return df
