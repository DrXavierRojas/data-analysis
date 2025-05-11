import pandas as pd

def load_and_clean(file_path):
    df = pd.read_csv(file_path)
    # Drop missing values and sort
    df.dropna(inplace=True)
    df.sort_values(by=df.columns[0], inplace=True)
    return df
