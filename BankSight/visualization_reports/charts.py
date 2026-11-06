from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def create_monthly_chart(rows):
    labels=[r['month'] for r in rows];values=[float(r['total']) for r in rows]
    fig,ax=plt.subplots(figsize=(7,3.5));ax.bar(labels,values);ax.set_title('Monthly transaction value');ax.set_ylabel('Amount (INR)');ax.set_xlabel('Month');ax.tick_params(axis='x',rotation=35);fig.tight_layout()
    output=BytesIO();fig.savefig(output,format='png',dpi=130);plt.close(fig);output.seek(0);return output.getvalue()
