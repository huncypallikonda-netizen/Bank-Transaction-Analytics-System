"""Basic explainable transaction screening rules for the student project."""
LARGE_TRANSACTION_LIMIT=100000.00

def inspect_transaction(amount: float, transaction_type: str):
    reasons=[]
    if amount>=LARGE_TRANSACTION_LIMIT: reasons.append(f'Large transaction detected: INR {amount:,.2f}')
    if transaction_type=='withdrawal' and amount>=50000: reasons.append('High-value withdrawal requires review')
    return bool(reasons), '; '.join(reasons) if reasons else None

def analyze_dataframe(df):
    """Return a copy with simple rule-based flags; requires amount and transaction_type columns."""
    required={'amount','transaction_type'}
    if not required.issubset(df.columns): raise ValueError(f'Missing columns: {required-set(df.columns)}')
    result=df.copy();result['is_flagged']=result.apply(lambda row: inspect_transaction(float(row['amount']),str(row['transaction_type']).lower())[0],axis=1)
    return result
