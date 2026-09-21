# E-Commerce Sales Analysis — 2024

## Project Overview
This project analyzes e-commerce transaction data for 2024 using Python and Pandas. The workflow demonstrates a practical data-analyst pipeline: raw data → cleaning → feature engineering → exploratory analysis → charts → dashboard.

> **Dataset note:** The included `raw_dataset.csv` is a reproducible synthetic dataset created for portfolio/learning use. It is not presented as proprietary real-world customer data.

## Dataset
- Period: January–November 2024
- Transactions: 3,660
- Categories: 7
- Payment methods: 5
- Cities: 8

## Folder Structure
```text
Ecommerce_Sales_Analysis_2024/
├── data/
│   ├── raw_dataset.csv
│   └── cleaned_dataset.csv
├── python/
│   └── ecommerce_analysis.py
├── dashboard/
│   ├── dashboard.pdf
│   ├── monthly_sales.png
│   ├── category_sales.png
│   ├── payment_sales.png
│   └── city_sales.png
└── README.md
```

## Data Cleaning
The raw file intentionally contains a small number of quality issues to demonstrate the cleaning process:
- Duplicate Order IDs
- Missing City values
- Missing Unit Price values
- Date conversion
- Duplicate removal
- Median imputation for missing Unit Price
- "Unknown" category for missing City

## KPIs
- Total Orders: 3,660
- Total Net Sales: ₹1,350,649.90
- Average Order Value: ₹369.03
- Average Rating: 3.02/5

## Analysis Performed
1. Monthly net-sales trend
2. Category-level sales performance
3. Payment-method analysis
4. City-level sales performance
5. Average order value
6. Customer rating analysis
7. Discount impact

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- CSV
- ReportLab

## How to Run
```bash
pip install pandas numpy matplotlib
python python/ecommerce_analysis.py
```

## Project Outcome
The project demonstrates the complete lifecycle of a small business analytics project and is suitable as a beginner/intermediate Data Analyst portfolio project.
