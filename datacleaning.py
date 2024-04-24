# Data Cleaning
# Start: 04-12-2024
# End: 

#%% imports
import pandas as pd
import numpy as np

#%% == Cancer County Cleaning Function ==

def cancercountyclean(df):

    df = df.drop(['AGE_ADJUSTED_CI_LOWER', 'AGE_ADJUSTED_CI_UPPER', 'CRUDE_CI_LOWER', 'CRUDE_CI_UPPER'], axis=1)
    df = df[~(df['AGE_ADJUSTED_RATE'].str.contains("~", regex=False, na=False))]
    df['FIPS'] = df['AREA'].str.extract(r'\((\d+)\)')

    df['COUNT'] = pd.to_numeric(df['COUNT'], errors='coerce')
    df['AGE_ADJUSTED_RATE'] = pd.to_numeric(df['AGE_ADJUSTED_RATE'], errors='coerce')
    df['CRUDE_RATE'] = pd.to_numeric(df['CRUDE_RATE'], errors='coerce')
    df['POPULATION'] = pd.to_numeric(df['POPULATION'], errors='coerce')

    return df


def airclean(df):
    df = 


# %%
