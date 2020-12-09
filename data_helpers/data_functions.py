def calculate_roi(budget, gross):
    return (gross - budget) / budget * 100

def clean_tn_movie_budgets(pd, df):

    ''' Cleans the tn_movie_budgets DataFrame

    Parameters
    ----------
    pd: a pandas instance
    df: the DataFrame to clean

    Returns
    ----------
    Cleaned pandas DataFrame
    '''

    # from scipy.stats import zscore

    #convert releae_data to datetime and add a release_year column
    df['release_date'] = pd.to_datetime(df['release_date'])
    df['release_year'] = df['release_date'].dt.year

    # convert numbers to int
    cols = ['production_budget','domestic_gross','worldwide_gross']
    df[cols] = df[cols].replace('[^0-9]', '', regex = True).astype('int')

    # remove rows with 0 budget or 0 worldwide_gross
    df = df[df['production_budget'] > 0]
    df = df[df['worldwide_gross'] > 0]

    # create ROI feature
    df['ROI'] = calculate_roi(df['production_budget'], df['worldwide_gross'])

    # create ROI_zscore feature
    # df['ROI_zscore'] = zscore(df['ROI'])
    return df

def compute_iqr_table(pd, df, col = 'genres'):
    ''' Creates a quartile table, for each group in col.

    Parameters
    ----------
    pd: a pandas object
    df: the DataFrame to operate on
    col: the column to group by

    Returns
    ----------
    padas DataFrame with the columns
        Q1 - first quartile by group
        Q3 - third quartile by group
        IQR - Interquartile range
        upper_thresh = Q3 + (1.5 * IQR)
        lower_thresh = Q1 - (1.5 * IQR)
'''

    import pandas as pd

    iqr = pd.DataFrame()
    #df = df.explode('genres')
    iqr['Q1'] = df.groupby('genres').ROI.quantile(.25)
    iqr['Q3'] = df.groupby('genres').ROI.quantile(.75)
    iqr['IQR'] = iqr['Q3'] - iqr['Q1']
    iqr['upper_thresh'] = iqr['Q3'] + 1.5*iqr['IQR']
    iqr['lower_thresh'] = iqr['Q1'] - 1.5*iqr['IQR']
    return iqr
