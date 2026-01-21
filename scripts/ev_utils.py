import pandas as pd

default_countries = ['Germany', 'France', 'Spain', 'EU27']

def veh_evo(df, powertrain, region, start_year, end_year, verbose=False):

    """
    Returns a DataFrame with vehicle units sold for a given country and powertrain.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame with vehicle data
        country (str): Country to filter
        powertrain (str): Powertrain type (e.g., BEV, PHEV)
        start_year & end_year (int): Years to calculate growth and compare data from
    
    Returns:
        float: Percentage change between start_year and end_year, and each year's sales volume of EVs
        None: If verbose=True, prints the change instead of returning
    """

    if start_year == end_year:
        raise ValueError("Start year and end year cannot be the same.")
    if start_year > end_year:
        raise ValueError("Start year cannot be higher than end year.")
    if start_year not in df['year'].unique() or end_year not in df['year'].unique():
        raise ValueError("The years must be within the scope of the database (2010-2023).")
    if powertrain not in df['powertrain'].unique():
        raise ValueError("Powertrain must be present in the database ('BEV', 'PHEV', 'FCEV').")
    if region not in df['region'].values:
        raise ValueError("Region must be present in the database.")

    df_clean = df.loc[
        (df['powertrain'] == powertrain) &
        (df['region'] == region) &
        (df['year'].between(start_year, end_year))
    ]

    if df_clean.empty:
        raise ValueError(f"No data found for {powertrain} in {region} in the period {start_year}-{end_year}.")

    # The following includes the calculation of the values for the region and years specified.

    first_value = df_clean.loc[(df_clean['year'] == start_year), 'value'].sum()
    last_value = df_clean.loc[(df_clean['year'] == end_year), 'value'].sum()

    if first_value == 0:
        print(f"{powertrain} sales in {region} were 0 in {start_year} and {last_value} in {end_year} — probable new market entry.")
        return

    per_change = ((last_value / first_value) - 1) * 100

    if verbose:
        print(f"For {region} region and {powertrain} powertrain, "
              f"the percentage change between {start_year} and {end_year} has been of {per_change:.2f}%,"
              f"\n with {first_value:.0f} units in {start_year}, and {last_value:.0f} units in {end_year}.")
    
    return per_change

# Usage: per_evo(df_vehicles_sales, 'BEV', 'Germany', 2022, 2023, verbose=True)



# Reusable percentage evolution function:
def per_evo(df, region, start_year, end_year, verbose=False):

    """
    Returns a DataFrame with percentage evolution for a given country and powertrain.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame with vehicle data
        country (str): Country to filter
        powertrain (str): Powertrain type (e.g., BEV, PHEV)
        start_year & end_year (int): Years to calculate growth and compare data from
    
    Returns:
        float: Percentage change between start_year and end_year, and each year's percentage share of EVs
        None: If verbose=True, prints the change instead of returning
    """

    if start_year == end_year:
        raise ValueError("Start year and end year cannot be the same.")
    if start_year > end_year:
        raise ValueError("Start year cannot be higher than end year.")
    if start_year not in df['year'].unique() or end_year not in df['year'].unique():
        raise ValueError("The years must be within the scope of the database (2010-2023).")
    if region not in df['region'].values:
        raise ValueError("Region must be present in the database.")

    df_clean = df.loc[
        (df['region'] == region) &
        (df['year'].between(start_year, end_year))
    ]

    if df_clean.empty:
        raise ValueError(f"No data found in {region} in the period {start_year}-{end_year}.")

    # The following includes the calculation of the values for the region and years specified.

    first_value = round(df_clean.loc[(df_clean['year'] == start_year), 'value'].sum(), 2)
    last_value = round(df_clean.loc[(df_clean['year'] == end_year), 'value'].sum(), 2) 

    per_change = ((last_value / first_value) - 1) * 100

    df_type = df_clean['parameter'].unique().tolist()

    if first_value == 0:
        print(f"Percentage share for {df_type[0]} in {region} was 0% in {start_year} and {last_value}% in {end_year} — probable new market entry.")

    if verbose:
        print(f"For {region}, "
              f"the percentage change for {df_type[0]} between {start_year} and {end_year} has been of {per_change:.2f}%,"
              f"\nwith {first_value:.2f}% in {start_year}, and {last_value:.2f}% in {end_year}.")
    else:
        print(f"Also, the percentage change for {df_type[0]} between {start_year} and {end_year} has been of {per_change:.2f}%,"
              f"\nwith {first_value:.2f}% in {start_year}, and {last_value:.2f}% in {end_year}.")

# Usage: per_evo(df_percentage_sales, 'BEV', 'Germany', 2022, 2023, verbose=True)