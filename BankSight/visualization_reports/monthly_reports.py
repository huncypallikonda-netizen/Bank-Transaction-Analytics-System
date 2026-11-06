import pandas as pd

def monthly_summary(transactions):
    """transactions: iterable of dicts containing transaction_date and amount."""
    df=pd.DataFrame(transactions)
    if df.empty:return pd.DataFrame(columns=['month','transaction_count','total_amount'])
    df['transaction_date']=pd.to_datetime(df['transaction_date']);df['month']=df['transaction_date'].dt.to_period('M').astype(str)
    return df.groupby('month',as_index=False).agg(transaction_count=('amount','count'),total_amount=('amount','sum'))
