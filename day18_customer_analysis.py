
import pandas as pd

# Sample retail dataset
data = {
    "CustomerID": [101, 102, 103, 101, 104, 102, 105, 101, 103, 106],
    "OrderID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Amount": [500, 300, 700, 400, 900, 200, 600, 800, 300, 450]
}

df = pd.DataFrame(data)

# 1. Total spending per customer
customer_spending = df.groupby("CustomerID")["Amount"].sum()

print("Total Customer Spending:")
print(customer_spending)

# 2. Purchase frequency
purchase_frequency = df.groupby("CustomerID")["OrderID"].count()

print("\nPurchase Frequency:")
print(purchase_frequency)

# 3. Average order value
average_order = df.groupby("CustomerID")["Amount"].mean()

print("\nAverage Order Value:")
print(average_order)

# 4. Combine customer metrics
customer_analysis = pd.DataFrame({
    "Total_Spending": customer_spending,
    "Purchase_Frequency": purchase_frequency,
    "Average_Order_Value": average_order
})

print("\nComplete Customer Analysis:")
print(customer_analysis)

# 5. Identify high-value customers
high_value = customer_analysis[
    customer_analysis["Total_Spending"] >= 1000
]

print("\nHigh Value Customers:")
print(high_value)
