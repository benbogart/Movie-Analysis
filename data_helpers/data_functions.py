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
