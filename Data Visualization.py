"""
Data Visualization
DSC-240
Brian Chaffee
04/24/2024
"""
#%% == Imports ==
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

#%% == Data Files ==

df_age = pd.read_csv('data/cancer_age_data.csv')
df_site = pd.read_csv('data/cancer_site_data.csv')
df_ohio = pd.read_csv('data/ohio_cancer_data.csv')

df_emission = pd.read_excel('data/OH-AirPollution-BYCOUNTY.xlsx')
df_emission = df_emission.drop(['SCC Code', 'EIS Sector', 'Source Description', 'SCC LEVEL 1', 'SCC LEVEL 2', 'SCC LEVEL 3', 'SCC LEVEL 4'], axis=1)

#%% == Prelimanary Visualizations


