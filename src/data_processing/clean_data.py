import pandas as pd


def clean_dataframe(dataframe: pd.DataFrame) -> pd.DataFrame:

 """
clean a pandas dataframe:
- remove duplicates
- handle missing values
- convert data types if needed. 

"""

# remove duplicates
 dataframe = dataframe.drop_duplicates()

 # check for missing values
 if dataframe.isnull().sum().any():
  
  # drop rows with missing values
  dataframe = dataframe.dropna()

 # convert data types if required 

 # make sure exchange rate value are floats

  for column in dataframe.columns:
   if "exchange_rate" in column.lower():
    dataframe[column] = dataframe[column].astype(float)

 return dataframe



