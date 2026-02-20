The purpose of the project: 

Analyse the curruncies and see how they change over time. 


Top-level Pseudo-code 

1- Load configuration
2- Fetch latest exchange rates from API
  
   validate API response
   if response invalid:
     handle error and exit

  Extract relevant exchange rate fields
  add current timestamp to each record 

3- Load existing historical dateset (if exists)
4- append new record to historical dataset / save updated dataset to storage 
5- analyse historical exchange rate trends 

6- genrate visualizations: 
 - trend over time (line plit)
-latest comparison(bar chart)
- distribution of rate change(histogram)


8- tell the final story using the graphs 


