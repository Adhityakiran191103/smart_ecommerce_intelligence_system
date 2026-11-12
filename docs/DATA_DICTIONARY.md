# Data dictionary (expected source fields)

Confirm these against the workbook before coding; source versions may differ.

| Field | Meaning | Typical use |
|---|---|---|
| InvoiceNo | Invoice/order identifier | Frequency; cancellation checks |
| StockCode | Product identifier | Product analysis |
| Description | Product description | Product reporting |
| Quantity | Units on invoice line | Revenue calculation |
| InvoiceDate | Transaction timestamp | Monthly trends; Recency |
| UnitPrice | Price per unit | Revenue calculation |
| CustomerID | Customer identifier | Customer aggregation and RFM |
| Country | Customer/order country | Geographic analysis |

Derived fields planned:

| Field | Definition |
|---|---|
| Revenue | Quantity × UnitPrice |
| Recency | Reference date − customer's latest purchase date |
| Frequency | Count of distinct invoices per customer |
| Monetary | Sum of customer revenue |
| R_Score/F_Score/M_Score | Quantile-based scores with correct direction |
| RFM_Total | Sum of R, F and M scores, if used |
| Segment | Business rule applied to RFM scores |
