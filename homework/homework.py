import pandas as pd
# from sqlalchemy import create_engine
# from tqdm.auto import tqdm
# import click


url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet'
print(pd.read_parquet(url) )

