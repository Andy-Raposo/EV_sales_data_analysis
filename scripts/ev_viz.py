import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

sns.set_style("whitegrid")

default_country_palette = {
    'Spain': 'red',
    'Germany': 'black',
    'France': 'blue',
    'EU27': 'cyan'
}
default_powertrain_palette = {
    'PHEV': 'green',
    'BEV': 'blue'
}


def year_plot(df, countries=None, powertrain=None, log=False, title=None, smooth=None):

    """
    Plots EV sales over time for selected regions and powertrain types.

    Parameters:
    - df (pd.DataFrame): Must contain 'year', 'region', 'value', optionally 'powertrain'.
    - countries (list[str], optional): Regions to include. Defaults to ['Spain','Germany','France','EU27'].
    - powertrain (str, optional): Filter by vehicle powertrain (e.g., 'BEV'). If None or 'per' in columns, no filter.
    - log (bool): Use log scale for y-axis.
    - title (str, optional): Custom plot title.
    """
    
    if countries is None:
        countries = ['Spain', 'Germany', 'France', 'EU27']
    if powertrain is None:
        powertrain = ['BEV', 'PHEV']
        
    if any(re.search(r'per', col, re.IGNORECASE) for col in df.columns):
        bev_data = df.loc[df['region'].isin(countries)].copy()
    else:
        bev_data = df.loc[(df['powertrain'] == powertrain) & (df['region'].isin(countries))].copy()
    # Adjusts the EU27 region to show the average between the 27 EU members
    if 'EU27' in countries:
        bev_data.loc[bev_data['region'] == 'EU27', 'value'] /= 27

    ### COULD ADD SMOOTHNESS HERE

    fig, ax = plt.subplots(figsize=(11, 6))

    sns.lineplot(data=bev_data, x='year', y='value', hue='region', palette=default_country_palette,linestyle='-')

    # Optional — to set custom automated titles (needs branching)
    # if any(re.search(r'per', col, re.IGNORECASE) for col in df.columns) or powertrain is None:
    #     ax.set_title(title, fontsize=16)
    # else:  
    #     ax.set_title(title, fontsize=16)

    if title is not None:
        ax.set_title(title, fontsize=16)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('EV Car Sales', fontsize=12)

    if log:
        ax.set_yscale('log') 

    ax.grid(True, linestyle='--', alpha=0.6)

    plt.legend(title='Regions')
    plt.show()
    return fig 

####

def powertrain_plot(df, countries, powertrain=None, log=False, title=None):

    if powertrain is None:
        powertrain = ['BEV', 'PHEV']
    bev_data = df.loc[(df['powertrain'].isin(powertrain)) & (df['region'].isin(countries))]

    fig, ax = plt.subplots(figsize=(11, 6))

    sns.lineplot(data=bev_data, x='year', y='value', hue='powertrain', palette=default_powertrain_palette,linestyle='-')

    ax.set_title(title, fontsize=16)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Stock Volume', fontsize=12)
    ax.grid('True', linestyle='--', alpha=0.6)

    plt.legend(title='Powertrain')
    plt.show()
    return fig

####


# Testing purposes

def filter_regions(df, countries, powertrain):
    if any(re.search(r'per', col, re.IGNORECASE) for col in df.columns) or powertrain is None:
        df = df.loc[df['region'].isin(countries)].copy()
    else:
        df = df.loc[(df['powertrain'] == powertrain) & (df['region'].isin(countries))].copy()
    if 'EU27' in countries:
        df.loc[df['region'] == 'EU27', 'value'] /= 27
    return df