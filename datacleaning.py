# Data Cleaning
# Start: 04-12-2024
# End: 

#%% imports
import pandas as pd
import numpy as np
#%%
# == USCS CANCER DATASET ==
# data = pd.read_csv('/Users/brianchaffee/Data Science/Projects/Project Data/DSC240/USCS-1999-2020-ASCII/BYAREA_COUNTY.TXT', sep='|')

# # Filter data for Ohio
# ohio_data = data[data['STATE'] == 'OH']

# ohio_data.to_csv('data/ohio_cancer_data.csv', index=False)
#%%
df_c = pd.read_csv('data/ohio_cancer_data.csv')
df_e = pd.read_excel('data/OH-AirPollution-BYCOUNTY.xlsx')


#%%
df_c.info()
df_e.info()
# %% == Cancer Cleaning Function ==


def cancerclean(df):
    df = df.drop(['AGE_ADJUSTED_CI_LOWER', 'AGE_ADJUSTED_CI_UPPER', 'CRUDE_CI_LOWER', 'CRUDE_CI_UPPER'], axis=1)
    df = df[~(df['AGE_ADJUSTED_RATE'].str.contains("~", regex=False, na=False))]
    return df


# def airclean(data):
#     df = 


# %%
