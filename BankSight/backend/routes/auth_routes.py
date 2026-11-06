from flask import Blueprint,request,jsonify
from db import get_connection
from auth import verify_password
import secrets
bp=Blueprint('auth',__name__)
@bp.post('/login')
def login():
    data=request.get_json(silent=True) or {}; username=str(data.get('username','')).strip(); password=str(data.get('password',''))
    if not username or not password: return jsonify({'error':'Username and password are required'}),400
    conn=get_connection();cur=conn.cursor(dictionary=True)
    try:
        cur.execute('SELECT id,username,password_hash FROM users WHERE username=%s AND is_active=1',(username,)); user=cur.fetchone()
        if not user or not verify_password(password,user['password_hash']): return jsonify({'error':'Incorrect username or password'}),401
        token=secrets.token_urlsafe(32);cur2=conn.cursor();cur2.execute('UPDATE users SET api_token=%s WHERE id=%s',(token,user['id']));conn.commit();cur2.close()
        return jsonify({'token':token,'username':user['username']})
    finally: cur.close();conn.close()
