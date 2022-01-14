import time

import pandas as pd
from cuml.tsa.auto_arima import AutoARIMA

def main() -> None:
    train = pd.read_csv('data/prepared-data-train.csv')
    train['ds'] = pd.to_datetime(train['ds']) 
    train = train.set_index(['ds', 'unique_ids']).unstack()

    print(train.head())
    
    
    start = time.time()
   
        
    end = time.time()
    print(f'Time: {end - start}')

    forecasts = forecasts.reset_index()
    forecasts.to_csv('data/mlforecast-forecasts.csv', index=False)


if __name__ == '__main__':
    main()
