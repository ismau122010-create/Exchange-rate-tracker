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