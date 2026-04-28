from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres@localhost:5432/postgres")

query = """
ALTER TABLE customer_features
ADD COLUMN IF NOT EXISTS churn INT;

UPDATE customer_features
SET churn = CASE
    WHEN recency > 90 THEN 1
    ELSE 0
END;
"""

with engine.begin() as conn:
    conn.execute(text(query))