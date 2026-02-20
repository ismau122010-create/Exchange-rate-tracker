import pandas as pd
from src.api.fetch_data import fetch_data_from_api

def load_data(currencies_data: list[dict]) -> pd.DataFrame:

    return pd.DataFrame(currencies_data)


if __name__ == "__main__":
    raw_data = fetch_data_from_api()
    result = load_data(raw_data)
    print(result)