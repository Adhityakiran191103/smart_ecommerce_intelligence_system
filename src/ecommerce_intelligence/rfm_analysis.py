"""RFM metric calculation and scoring."""


def calculate_rfm(df, reference_date=None):
    """Calculate Recency, Frequency, and Monetary per customer.

    TODO:
    - Recency: reference date minus each customer's latest InvoiceDate.
    - Frequency: number of distinct invoices/orders.
    - Monetary: sum of Quantity * UnitPrice.
    Validate the dataset's column names and cancellation handling.
    """
    raise NotImplementedError("Integrate and validate your Day 16/17 RFM work here.")


def score_rfm(rfm, bins=5):
    """Create R, F and M scores using quantile-based scoring.

    TODO: decide score direction carefully: lower Recency is better;
    higher Frequency and Monetary are better. Handle tied quantile edges.
    """
    raise NotImplementedError("Complete this during the RFM scoring days.")
