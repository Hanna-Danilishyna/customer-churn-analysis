from sqlalchemy import create_engine
import pandas as pd
engine = create_engine("postgresql://postgres@localhost:5432/postgres")

df = pd.read_csv("data/sample_data.csv")

df.to_sql(
    "transactions",
    engine,
    if_exists="replace",
    index=False
)