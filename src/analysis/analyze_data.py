import numpy as np
import pandas as pd


def analyze_data(dataframe: pd.DataFrame) -> dict:
    
    """
    analyse numerical data in a dataframe using numpy

    parameters: 
    
    datafra,e(pd.dataframe): cleaned pandas dataframe

    return:
    dict: dictionary containing statstical analysis result. 

     """
    
   # Extract numric columns only
    numeric_df = dataframe.select_dtypes(include=["number"])
   
   # if there are no numric columns, return empty results
    if numeric_df.empty:
        return []
    
    # calculate statstic using numpy 

    analysis_results = {
       "mean": numeric_df.mean().to_dict(),
       "min": numeric_df.min().to_dict(),
       "max": numeric_df.max().to_dict(),
       "median": numeric_df.median().to_dict(),
       "std": numeric_df.std().to_dict(),

    }
    
    return analysis_results