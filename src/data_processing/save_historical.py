import os 
import pandas as pd 


def save_historical_data(
    cleaned_df : pd.DataFrame,
    csv_path: str,
    backfill_date: str= "2026-02-08") -> pd.DataFrame:
    
    """
   safely merge new cleaned data into a historical csv file.

   - handle empty or currupted csvs
   - remve duplicate columns
   - ensures scheme consistency 
   - bckfills timestamps for old rows
   - write to disk ones

   retruns :
   pd.dataframe: updated historical dataframe 

    """

    COLUMNS = [
        "timestamp",
        "base_code",
        "target_currency",
        "exchange_rate",
        
    ]

# Ensure output directory exists     
    os.makedirs(os.path.dirname(csv_path),exist_ok=True)

    # load existing data safely 

    if os.path.exists(csv_path):
        try:
            existing_df = pd.read_csv(csv_path)

            if existing_df.empty or len(existing_df.columns) == 0:
                raise ValueError("Exisitng CSV is empty")
            
        except(pd.errors.EmptyDataError,ValueError):
            existing_df = pd.DataFrame(columns=COLUMNS)

    else:
        existing_df = pd.DataFrame(columns=COLUMNS)


    # normalize both dataframes

    existing_df = existing_df.loc[:, ~existing_df.columns.duplicated()]    
    cleaned_df =  cleaned_df.loc[:, ~cleaned_df.columns.duplicated()]

    # Ensure timestamp exists 
    if "timestamp" not in existing_df.columns:
        existing_df["timestamp"] = pd.NaT


    if "timestamp" not in cleaned_df.columns:
        cleaned_df["timestamp"] = pd.Timestamp.now()

    #  backfill only old news
    existing_df["timestamp"] = existing_df["timestamp"].fillna(
        pd.Timestamp(backfill_date)
    )  

    # Enforce scheme 
    existing_df = existing_df.reindex(columns=COLUMNS)
    cleaned_df = cleaned_df.reindex(columns=COLUMNS)

    # merge 

    updated_df = pd.concat(
        [existing_df,cleaned_df],
        ignore_index=True
    )                  

    # save once 

    updated_df.to_csv(csv_path, index=False)

    return updated_df