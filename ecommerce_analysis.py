import pandas as pd
import matplotlib.pyplot as plt

raw = pd.read_csv("data/raw_dataset.csv")
df = raw.drop_duplicates(subset=["Order_ID"]).copy()
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Unit_Price"] = df["Unit_Price"].fillna(df["Unit_Price"].median())
df["City"] = df["City"].fillna("Unknown")

df["Gross_Sales"] = df["Quantity"] * df["Unit_Price"]
df["Discount_Amount"] = df["Gross_Sales"] * df["Discount_Pct"]
df["Net_Sales"] = df["Gross_Sales"] - df["Discount_Amount"]
df["Month"] = df["Order_Date"].dt.strftime("%b")
df["Month_Num"] = df["Order_Date"].dt.month
df["Quarter"] = df["Order_Date"].dt.to_period("Q").astype(str)
df["Day_of_Week"] = df["Order_Date"].dt.day_name()

df.to_csv("data/cleaned_dataset.csv", index=False)

monthly = df.groupby(["Month_Num","Month"])["Net_Sales"].sum().sort_index()
category = df.groupby("Category")["Net_Sales"].sum().sort_values(ascending=False)
payment = df.groupby("Payment_Method")["Net_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(9,5))
plt.plot(monthly.index.get_level_values("Month"), monthly.values, marker="o")
plt.title("Monthly Net Sales — 2024"); plt.xlabel("Month"); plt.ylabel("Net Sales")
plt.tight_layout(); plt.savefig("dashboard/monthly_sales.png", dpi=180); plt.close()

plt.figure(figsize=(9,5))
category.sort_values().plot(kind="barh")
plt.title("Net Sales by Category — 2024"); plt.xlabel("Net Sales")
plt.tight_layout(); plt.savefig("dashboard/category_sales.png", dpi=180); plt.close()

plt.figure(figsize=(8,5))
payment.plot(kind="bar")
plt.title("Net Sales by Payment Method — 2024"); plt.ylabel("Net Sales")
plt.tight_layout(); plt.savefig("dashboard/payment_sales.png", dpi=180); plt.close()

print("Total orders:", len(df))
print("Total net sales:", round(df["Net_Sales"].sum(),2))
print("Average order value:", round(df["Net_Sales"].mean(),2))
print("Top category:", category.index[0])
