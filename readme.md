# Customer Churn Analysis (Online Retail II)

## Project Objective

This project aims to analyze customer purchasing behavior and predict customer churn using transactional e-commerce data.

The main goals are:
- Identify customers at risk of churn
- Understand behavioral patterns behind churn
- Build a predictive model using machine learning
- Provide actionable business insights for retention strategies

---

## Dataset

Source: Online Retail II (e-commerce transaction data)

### Data preparation steps:
- Removed invalid transactions (negative quantities and prices)
- Dropped missing customer IDs
- Sampled dataset to 300,000 rows for performance optimization
- Loaded cleaned data into PostgreSQL

---

## Data Pipeline

Raw CSV
   ↓
Data Cleaning (Python)
   ↓
Sampling (300k rows)
   ↓
PostgreSQL (transactions table)
   ↓
SQL Feature Engineering
   ↓
customer_features table
   ↓
Churn labeling
   ↓
EDA + ML Modeling

## Feature Engineering


Customer-level features were created using SQL aggregation:

total_orders → number of unique invoices
total_items → total quantity purchased
total_revenue → lifetime revenue
avg_order_value → average basket size
first_purchase_date → customer acquisition date
last_purchase_date → last activity
recency → days since last purchase

## Churn Definition

A customer is considered churned if:

They have not made a purchase in the last 90 days

churn = 1 if recency > 90 else 0
## Exploratory Data Analysis
## Churn distribution
![Churn distribution](../figures/churn_distribution.png)

## Recency vs Churn
![Recency by Churn](../figures/recency_by_churn.png)

## Revenue vs Churn
![Revenue by Churn](../figures/revenue_by_churn.png)

## Orders vs Churn
![Orders by Churn](../figures/orders_by_churn.png)

## Feature Correlation
![Feature Correlation](../figures/correlation_heatmap.png)

## Key Business Insights
1. Recency is the strongest churn driver

Customers who have not purchased recently are significantly more likely to churn.

2. Revenue is not a strong predictor

High-spending customers are not necessarily loyal.

3. One-time buyers are high-risk segment

Customers with low engagement frequency are more likely to churn.

4. Engagement matters more than monetary value

Behavioral activity is more predictive than revenue metrics.

## Machine Learning Model

A Logistic Regression model was trained using RFM-based features.

Features used:
total_orders
total_items
total_revenue
avg_order_value
recency

## Model Results Interpretation
Feature	Impact
Recency	Strong positive impact on churn

Total orders	Moderate impact
Monetary features	Weak impact
Key insight:

Customer inactivity (recency) is the strongest predictor of churn.

## Business Recommendations
Focus retention campaigns on customers with 60–120 days inactivity
Prioritize engagement over revenue-based targeting
Design onboarding strategies for one-time buyers
Segment customers based on recency and frequency behavior
## Tech Stack
Python (pandas, scikit-learn, matplotlib)
PostgreSQL
SQL (feature engineering)
Jupyter Notebook
Git/GitHub
## Project Structure
customer-churn-analysis/
│
├── data/
├── sql/
├── scripts/
├── notebooks/
├── figures/
├── models/
└── README.md

## Summary

This project demonstrates an end-to-end data analytics workflow:

Data cleaning and preprocessing
Feature engineering in SQL
Exploratory data analysis
Machine learning modeling
Business insight generation

The final model highlights that customer recency is the most important factor in predicting churn, providing actionable insights for retention strategies.
