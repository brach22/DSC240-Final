"""
File Formatting
DSC-240
Brian Chaffee
04/24/2024
"""
#%% imports
import pandas as pd
import numpy as np

#%% == USCS COUNTY DATASET ==
df_county = pd.read_csv('/Users/brianchaffee/Data Science/Projects/Project Data/DSC240/USCS-1999-2020-ASCII/BYAREA_COUNTY.TXT', sep='|')

# == Filter data for Ohio
df_county_filter = df_county[df_county['STATE'] == 'OH']
df_county_filter = df_county_filter[df_county_filter['YEAR'] != '1999']

# == Drop unneeded columns
df_county_filter = df_county_filter.drop(['AGE_ADJUSTED_CI_LOWER', 'AGE_ADJUSTED_CI_UPPER', 'CRUDE_CI_LOWER', 'CRUDE_CI_UPPER'], axis=1)
#df_county_filter = df_county_filter[~(df_county_filter['AGE_ADJUSTED_RATE'].str.contains("~", regex=False, na=False))]
df_county_filter = df_county_filter[df_county_filter['RACE'] == 'All Races']


# == Add in FIPS Column Specific
df_county_filter['FIPS'] = df_county_filter['AREA'].str.extract(r'\((\d+)\)')

# == Change Row formats
df_county_filter['COUNT'] = pd.to_numeric(df_county_filter['COUNT'], errors='coerce')
df_county_filter['AGE_ADJUSTED_RATE'] = pd.to_numeric(df_county_filter['AGE_ADJUSTED_RATE'], errors='coerce')
df_county_filter['CRUDE_RATE'] = pd.to_numeric(df_county_filter['CRUDE_RATE'], errors='coerce')
df_county_filter['POPULATION'] = pd.to_numeric(df_county_filter['POPULATION'], errors='coerce')

# ==Drop NaN values
df_county_filter = df_county_filter.dropna()

# == Turn into CSV file format
df_county_filter.to_csv('data/ohio_cancer_data.csv', index=False)

#%% == USCS AGE DATASET ==
df_age = pd.read_csv('/Users/brianchaffee/Data Science/Projects/Project Data/DSC240/USCS-1999-2020-ASCII/BYAGE.TXT', sep='|')

df_age_filter = df_age.drop(['CI_LOWER', 'CI_UPPER'], axis=1)

df_age_filter = df_age_filter[df_age_filter['RACE'] == 'All Races']
df_age_filter = df_age_filter[df_age_filter['YEAR'] != '1999']

df_age_filter['COUNT'] = pd.to_numeric(df_age_filter['COUNT'], errors='coerce')
df_age_filter['RATE'] = pd.to_numeric(df_age_filter['RATE'], errors='coerce')
df_age_filter['POPULATION'] = pd.to_numeric(df_age_filter['POPULATION'], errors='coerce')
df_age_filter['YEAR'] = pd.to_datetime(df_age_filter['YEAR'], format='%Y', errors='coerce')

df_age_filter = df_age_filter.dropna()

df_age_filter['YEAR'] = df_age_filter['YEAR'].dt.year.astype(int)

df_age_filter.to_csv('data/cancer_age_data.csv', index=False)

# %% == USCS SITE DATASET ==
df_site = pd.read_csv('/Users/brianchaffee/Data Science/Projects/Project Data/DSC240/USCS-1999-2020-ASCII/BYSITE.TXT', sep='|')

df_site_filter = df_site.drop(['AGE_ADJUSTED_CI_LOWER', 'AGE_ADJUSTED_CI_UPPER', 'CRUDE_CI_LOWER', 'CRUDE_CI_UPPER'], axis=1)

df_site_filter = df_site[df_site['RACE'] == 'All Races']

df_site_filter = df_site_filter[df_site_filter['YEAR'] != '2016-2020']
df_site_filter = df_site_filter[df_site_filter['YEAR'] != '1999']

df_site_filter['COUNT'] = pd.to_numeric(df_site_filter['COUNT'], errors='coerce')
df_site_filter['AGE_ADJUSTED_RATE'] = pd.to_numeric(df_site_filter['AGE_ADJUSTED_RATE'], errors='coerce')
df_site_filter['CRUDE_RATE'] = pd.to_numeric(df_site_filter['CRUDE_RATE'], errors='coerce')
df_site_filter['POPULATION'] = pd.to_numeric(df_site_filter['POPULATION'], errors='coerce')
df_site_filter['YEAR'] = pd.to_datetime(df_site_filter['YEAR'], format='%Y', errors='coerce')

df_site_filter = df_site_filter.dropna()

df_site_filter['YEAR'] = df_site_filter['YEAR'].dt.year.astype(int)

df_site_filter.to_csv('data/cancer_site_data.csv', index=False)

# %%
