import csv
from pathlib import Path

def export_transactions_csv(rows, output_path='transactions_report.csv'):
    """Export a list of dictionaries to CSV; do not include passwords or API tokens."""
    fields=['id','transaction_type','amount','description','transaction_date','is_flagged']
    path=Path(output_path)
    with path.open('w',newline='',encoding='utf-8') as handle:
        writer=csv.DictWriter(handle,fieldnames=fields,extrasaction='ignore');writer.writeheader();writer.writerows(rows)
    return path
