import sys
import pandas as pd

print("arguments", sys.argv)

month = int(sys.argv[1])

print(f"Hello pipeline!, month={month}")

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]


df = pd.DataFrame({
    "A": [1,2],
    "B": [3,4]
})


df["month"] = month
print(df.head())

df.to_parquet(f"output_{month}.parquet")