Functions Pseudoc-Code:


1- fetch_exchange_rate: 
 create an empty list called records 
 
Define API request parameters:
- example: base currency, target currencies, API key.


Try: 
 Send HTTP request to exchange rate API
 
if response status is not successful:
  return error 
 
Parse response Json

for each target currency:
 extract excahnge rate
 create structured record:
  - base currency
  - target currency
  - exchange currency
  - timestamp 

 Append record to reocrds list



except network error:
log error

 return empty reutls 


 # ----------------------------------------------------------------------------------------


 2- create load_raw_data function:
  load the raw data and convert it to Pandas Dataframe 

  -------------------------------------------



  3- Clean the dataframe date using pandas. 
   
   if there is duplicates in the dataframe drop it
   if there is missing values do 2 metod: 
    either frop the column.
    or fill the column.

    also convert data types if needed. 



   -----------------------------------------------------------

   4- 

  FUNCTION save_historical_data(cleaned_df, csv_path, backfill_date)

    DEFINE COLUMNS AS:
        ["timestamp",
         "base_code",
         "target_currency",
         "exchange_rate"]

    --------------------------------------------------
    STEP 1: Ensure Output Directory Exists
    --------------------------------------------------
    CREATE directory for csv_path IF it does not exist

    --------------------------------------------------
    STEP 2: Load Existing CSV Safely
    --------------------------------------------------
    IF file at csv_path EXISTS THEN
        TRY
            READ CSV file INTO existing_df

            IF existing_df is EMPTY OR has NO columns THEN
                RAISE error
            END IF

        CATCH empty file OR corrupted file error
            CREATE empty existing_df WITH COLUMNS
        END TRY

    ELSE
        CREATE empty existing_df WITH COLUMNS
    END IF

    --------------------------------------------------
    STEP 3: Remove Duplicate Columns
    --------------------------------------------------
    REMOVE duplicated columns FROM existing_df
    REMOVE duplicated columns FROM cleaned_df

    --------------------------------------------------
    STEP 4: Ensure Timestamp Column Exists
    --------------------------------------------------
    IF "timestamp" NOT IN existing_df THEN
        ADD "timestamp" column WITH empty datetime values
    END IF

    IF "timestamp" NOT IN cleaned_df THEN
        ADD "timestamp" column WITH current datetime
    END IF

    --------------------------------------------------
    STEP 5: Backfill Missing Old Timestamps
    --------------------------------------------------
    FOR each row IN existing_df
        IF timestamp IS missing THEN
            REPLACE timestamp WITH backfill_date
        END IF
    END FOR

    --------------------------------------------------
    STEP 6: Enforce Schema Consistency
    --------------------------------------------------
    REORDER AND LIMIT existing_df columns TO match COLUMNS
    REORDER AND LIMIT cleaned_df columns TO match COLUMNS

    --------------------------------------------------
    STEP 7: Merge Data
    --------------------------------------------------
    CONCATENATE existing_df AND cleaned_df
        INTO updated_df
        RESET index

    --------------------------------------------------
    STEP 8: Save to Disk (Once)
    --------------------------------------------------
    WRITE updated_df TO csv_path WITHOUT index column

    RETURN updated_df

END FUNCTION


------------------------------------------------------------

5-   📁 src/analysis/analyze_data.py
Function: analyze_data
FUNCTION analyze_data(dataframe):

    EXTRACT numerical columns

    CALCULATE statistics using NumPy:
        - mean
        - minimum
        - maximum
        - median
        - std

    STORE results in a dictionary or variable
    RETURN analysis results



-----------------------------------------------------------------------------


6- 📁 src/visualization/visualize_data.py
Function: visualize_data
FUNCTION visualize_data(dataframe):

    CREATE line plot to show trends
    CREATE bar chart for comparisons
    OPTIONAL: create distribution plot

    LABEL axes and title
    DISPLAY plots


 Function: save_plots
FUNCTION save_plots():

    SAVE generated plots to outputs/figures folder



    
-----------------------------------------------------------------------------




7- 📁 src/main.py
Function: main
FUNCTION main():

    DEFINE API URL

    CALL fetch_data_from_api()
    STORE raw JSON data

    CALL load_data_into_dataframe()
    STORE DataFrame

    CALL clean_dataframe()
    STORE cleaned DataFrame

    Call historical_save_data()
    STORE historical data in CSV
    
    CALL analyze_data()
    STORE analysis results

    CALL visualize_data()
        SAVE plots

    PRINT completion message





    
-----------------------------------------------------------------------------
