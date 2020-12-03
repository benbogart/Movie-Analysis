import pandas as pd
from glob import glob
import os

def get_movie_data():
    csv_files = glob("data/zippedData/*.csv.gz")

    csv_files_dict = {}
    for filename in csv_files:
        filename_cleaned = os.path.basename(filename).replace(".csv.gz", "").replace(".", "_") # cleaning the filenames
        filename_df = pd.read_csv(filename, index_col=0)
        csv_files_dict[filename_cleaned] = filename_df

    csv_files_dict['rt_movie_info'] = pd.read_csv('data/zippedData/rt.movie_info.tsv.gz', sep='\t', index_col='id')
    csv_files_dict['rt_reviews'] = pd.read_csv('data/zippedData/rt.reviews.tsv.gz', sep='\t', encoding='latin-1')
    
    return csv_files_dict

data = get_movie_data()
