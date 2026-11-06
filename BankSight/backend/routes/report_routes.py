from flask import Blueprint,send_file,g
from auth import token_required
from visualization_reports.charts import create_monthly_chart
from db import get_connection
from io import BytesIO
bp=Blueprint('reports',__name__)
@bp.get('/reports/monthly-chart')
@token_required
def monthly_chart():
    conn=get_connection();cur=conn.cursor(dictionary=True)
    try:cur.execute("SELECT DATE_FORMAT(transaction_date,'%%Y-%%m') month, SUM(amount) total FROM transactions WHERE user_id=%s GROUP BY month ORDER BY month",(g.current_user['id'],));rows=cur.fetchall()
    finally:cur.close();conn.close()
    image=create_monthly_chart(rows);return send_file(BytesIO(image),mimetype='image/png',download_name='monthly_activity.png')
