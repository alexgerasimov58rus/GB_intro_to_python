import random
import pandas as pd


def one_hot(df):
    df_vals = sorted(list(set(df['whoAmI'])))
    df_cols = list(df.columns)
    indeces = list(df.index)

    data = dict()

    for col in df_cols:
        for val in df_vals:
            name = f'{col}_{val}'
            column = []
            for i in indeces:
                if df[col][i] == val:
                    column.append(True)
                else:
                    column.append(False)
            data[name] = column            
    return pd.DataFrame(data)

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(one_hot(data))
