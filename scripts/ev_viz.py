import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

def year_plot(df, countries=None, powertrain=None, log=False, title=None):
    if countries is None:
        countries = ['Spain', 'Germany', 'France', 'EU27']
        
    if any(re.search(r'per', col, re.IGNORECASE) for col in df.columns) or powertrain is None:
        bev_data = df.loc[df['region'].isin(countries)].copy()
    else:
        bev_data = df.loc[(df['powertrain'] == powertrain) & (df['region'].isin(countries))].copy()
    # Adjusts the EU27 region to show the average between the 27 EU members
    if 'EU27' in countries:
        eu27_mask = bev_data['region'] == 'EU27'
        bev_data.loc[eu27_mask, 'value'] /= 27

    fig, ax = plt.subplots(figsize=(11, 6))

    palette = {
        'Spain': 'red',
        'Germany': 'black',
        'France': 'blue',
        'EU27': 'cyan'
    }

    sns.lineplot(data=bev_data, x='year', y='value', hue='region', palette=palette,linestyle='-')

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