from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres@localhost:5432/postgres")

recency_query = """
ALTER TABLE customer_features
ADD COLUMN IF NOT EXISTS recency INT;

UPDATE customer_features
SET recency =
    ('2011-12-09'::date - last_purchase_date::date);
"""

with engine.begin() as conn:
    conn.execute(text(recency_query))