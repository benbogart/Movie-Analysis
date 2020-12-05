def get_budget_class(budget):
    '''Takes a budget number in USD and returns the IATSE budget tier.
    (IATSE is the union that covers most of the below-the-line crew)
    '''
    if budget < 600000:
        return 'under 6m'
    elif budget >= 6000000 and budget < 10000000:
        return '6-10m'
    elif budget >= 10000000 and budget < 14200000:
        return '10-14.2m'
    elif budget >= 14200000:
        return '14.2m +'

def calculate_roi(budget, gross):
    return (gross - budget) / budget * 100

# TODO: add roi
def clean_tn_movie_budgets(df):
    import pandas as pd
    from scipy.stats import zscore

    #convert releae_data to datetime and add a release_year column
    df['release_date'] = pd.to_datetime(df['release_date'])
    df['release_year'] = df['release_date'].dt.year

    # convert numbers to int
    cols = ['production_budget','domestic_gross','worldwide_gross']
    df[cols] = df[cols].replace('[^0-9]', '', regex = True).astype('int')

    # remove rows with 0 budget or 0 worldwide_gross
    df = df[df['production_budget'] > 0]
    df = df[df['worldwide_gross'] > 0]

    df['ROI'] = calculate_roi(df['production_budget'], df['worldwide_gross'])
    # calculate overall zscore
    df['ROI_zscore'] = zscore(df['ROI'])
    return df
