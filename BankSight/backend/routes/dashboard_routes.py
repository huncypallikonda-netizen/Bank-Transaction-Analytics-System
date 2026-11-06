from flask import Blueprint,jsonify,g
from db import get_connection
from auth import token_required
bp=Blueprint('dashboard',__name__)
@bp.get('/dashboard')
@token_required
def dashboard():
    conn=get_connection();cur=conn.cursor(dictionary=True)
    try:
        cur.execute('SELECT COUNT(*) total_transactions, COALESCE(SUM(amount),0) total_amount, COALESCE(SUM(is_flagged),0) flagged_transactions FROM transactions WHERE user_id=%s',(g.current_user['id'],));summary=cur.fetchone()
        cur.execute('SELECT id,transaction_type,amount,description,transaction_date,is_flagged FROM transactions WHERE user_id=%s ORDER BY transaction_date DESC LIMIT 10',(g.current_user['id'],));summary['recent_transactions']=cur.fetchall();return jsonify(summary)
    finally:cur.close();conn.close()
@bp.get('/alerts')
@token_required
def alerts():
    conn=get_connection();cur=conn.cursor(dictionary=True)
    try:cur.execute('SELECT id,message,created_at FROM alerts WHERE user_id=%s ORDER BY created_at DESC LIMIT 20',(g.current_user['id'],));return jsonify(cur.fetchall())
    finally:cur.close();conn.close()
