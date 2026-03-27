#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm




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




# In[19]:


parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]



# In[26]:


'''df = pd.read_csv(
    prefix + 'yellow_tripdata_2021-01.csv.gz',
    nrows=100,
    dtype=dtype,
    parse_dates=parse_dates)'''


# In[27]:


#len(df)


# In[28]:


#df.head()


# In[29]:


#uv add alchemy


# In[31]:


#get_ipython().system('uv add sqlalchemy')


# In[36]:

def run():
    year = 2021
    month = 1
    pg_user = 'root'
    pg_password = 'root'
    pg_host = 'localhost'
    pg_port = 5433
    pg_db = 'ny_taxi'
    prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
    url = f'{prefix}yellow_tripdata_{year}-{month:02d}.csv.gz'

    # Small sample dataframe for schema preview/debugging.
    df = pd.read_csv(
        url,
        nrows=100,
        dtype=dtype,
        parse_dates=parse_dates
    )

    df_iter = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=100000
    )

    engine = create_engine(f'postgresql+psycopg://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}')

    first = True

    for df_chunk in df_iter:

        if first:
            # Create table schema (no data)
            df_chunk.head(0).to_sql(
                name="yellow_taxi_data",
                con=engine,
                if_exists="replace"
            )
            first = False
            print("Table created")

        # Insert chunk
        df_chunk.to_sql(
            name="yellow_taxi_data",
            con=engine,
            if_exists="append"
        )

        print("Inserted:", len(df_chunk))
    

if __name__ == '__main__':
    run()



# In[35]:


#get_ipython().system('uv add psycopg2')


# In[37]:


#get_ipython().system('uv add psycopg2-binary')


# In[42]:


#print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# In[41]:





# In[62]:





# In[63]:





# In[46]:





# In[64]:




# In[58]:





# In[ ]:




