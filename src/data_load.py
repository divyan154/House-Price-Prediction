import pandas as pd
import numpy as np

def load_boston_dataset():
    url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(url, sep="\s+", skiprows=22, header=None)
    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]

    columns = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE',
               'DIS','RAD','TAX','PTRATIO','B','LSTAT']
    df = pd.DataFrame(data, columns=columns)
    df['price'] = target
    return df
