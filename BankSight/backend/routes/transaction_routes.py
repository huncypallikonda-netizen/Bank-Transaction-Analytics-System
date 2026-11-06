from flask import Blueprint,request,jsonify,g
from db import get_connection
from auth import token_required
from analytics_security.analyzer import inspect_transaction
bp=Blueprint('transactions',__name__)
@bp.get('/transactions')
@token_required
def list_transactions():
    conn=get_connection();cur=conn.cursor(dictionary=True)
    try: cur.execute('SELECT id,transaction_type,amount,description,transaction_date,is_flagged FROM transactions WHERE user_id=%s ORDER BY transaction_date DESC',(g.current_user['id'],));return jsonify(cur.fetchall())
    finally:cur.close();conn.close()
@bp.post('/transactions')
@token_required
def add_transaction():
    data=request.get_json(silent=True) or {}; kind=str(data.get('transaction_type','')).strip().lower(); description=str(data.get('description',''))[:255]
    try: amount=float(data.get('amount'))
    except (TypeError,ValueError): return jsonify({'error':'A valid amount is required'}),400
    if kind not in ('deposit','withdrawal','transfer','payment'): return jsonify({'error':'Type must be deposit, withdrawal, transfer or payment'}),400
    if amount<=0: return jsonify({'error':'Amount must be greater than zero'}),400
    flagged,reason=inspect_transaction(amount,kind)
    conn=get_connection();cur=conn.cursor()
    try:
        cur.execute('INSERT INTO transactions(user_id,transaction_type,amount,description,is_flagged,flag_reason) VALUES(%s,%s,%s,%s,%s,%s)',(g.current_user['id'],kind,amount,description,int(flagged),reason));txid=cur.lastrowid
        if flagged: cur.execute('INSERT INTO alerts(user_id,transaction_id,message) VALUES(%s,%s,%s)',(g.current_user['id'],txid,reason))
        conn.commit();return jsonify({'id':txid,'is_flagged':flagged,'message':'Transaction saved'}),201
    finally:cur.close();conn.close()
