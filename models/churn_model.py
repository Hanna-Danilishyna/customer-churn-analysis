from sqlalchemy import create_engine
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
engine = create_engine("postgresql://postgres@localhost:5432/postgres")

df = pd.read_sql("SELECT * FROM customer_features", engine)

X = df[["total_orders", "total_items", "total_revenue", "avg_order_value", "recency"]]
y = df["churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print(model.coef_)