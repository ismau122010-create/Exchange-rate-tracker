import os 
from pathlib import Path
import pandas as pd

import json

from src.api.fetch_data import fetch_data_from_api
from src.data_processing.load_data import load_data
from src.data_processing.clean_data import clean_dataframe
from src.analysis.analyze_data import analyze_data

from src.data_processing.save_historical import save_historical_data
from src.visualization.visualize_data import visualize_data

def main():

 # fetch raw jason data
 raw_data= fetch_data_from_api()

 # 2- load data into dataframe

 raw_df = load_data(raw_data)


 # 3- clean dataframe

 cleaned_df = clean_dataframe(raw_df)   

# 4- save historical data

 csv_path = "data/processed/cleaned_data.csv"

 historical_df = save_historical_data(cleaned_df,csv_path)
 print("Historical data")
 print(historical_df)
 print(historical_df.shape)

# 5- analyse data

 analysis_results = analyze_data(historical_df)
 print("analysis")
 print(analysis_results)


# 6- visualize data

 visualize_data(historical_df)

 

if __name__ == "__main__":
 main()