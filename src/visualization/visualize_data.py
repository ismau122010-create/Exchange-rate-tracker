import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def visualize_data(dataframe):

    """
   genrate and save visulaization using timstamp as x-axis: 
    - line plot (time series)
    - bar chart (latest snapshot)
    - distribution plot
    """


  # validate and prepare time stamp

    if "timestamp" not in dataframe.columns:
       raise ValueError("timestamp column is required for visualization")  
    # this converts the timestamp string into proper datatime format
    dataframe["timestamp"] = pd.to_datetime(dataframe["timestamp"])
    # This sorts the time in order to avoid issues plotting the line forawrd 
    dataframe = dataframe.sort_values("timestamp")

    # output directory 
    output_dir = "outputs/figures"
    os.makedirs(output_dir,exist_ok=True)

    # ------------------

    # Line plot ( time series)
    numeric_cols = dataframe.select_dtypes(include="number").columns
    
    for rate in dataframe["target_currency"].unique():
        currency_df = dataframe[dataframe["target_currency"]== rate]

        plt.figure(figsize=(10,5))
        for col in numeric_cols:
            plt.plot(
                currency_df["timestamp"],
                currency_df[col],
                label = col
            )
        
        plt.title(f"Exchange trends over time - {rate}")
        plt.xlabel("Time")
        plt.ylabel("value")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        
        filename = f"line_plot_{rate.lower()}.png"
        plt.savefig(os.path.join(output_dir,filename))
        plt.show

        # -----------------------------------------------

        # bar chart 
        latest_df = dataframe.sort_values("timestamp").tail(len(dataframe["target_currency"].unique()))

        if len(latest_df.columns) >= 2:
            plt.figure(figsize=(10,5))
            sns.barplot(
                x="target_currency",
                y="exchange_rate",
                data= latest_df
            )


            plt.title("Exchange rate for each currency")
            plt.xlabel("target_currency")
            plt.ylabel("exchange_rate")
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, "bar_chart.png"))
            plt.show

        
        # distribution plot 

        if len(numeric_cols) > 0:
            plt.figure(figsize=(8,4))
            sns.histplot(dataframe[numeric_cols[0]], kde=True)
            plt.title(f"distribution of {numeric_cols[0]}")
            plt.xlabel(numeric_cols[0])
            plt.tight_layout()
            plt.savefig(
                os.path.join(output_dir, f"distribution_{numeric_cols[0]}.png")
            )
            plt.show()