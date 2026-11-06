import hashlib, hmac, secrets
from functools import wraps
from flask import request, jsonify, g
from db import get_connection

def hash_password(password: str) -> str:
    # PBKDF2 is used instead of storing plain-text passwords.
    salt=secrets.token_hex(16)
    digest=hashlib.pbkdf2_hmac('sha256',password.encode(),salt.encode(),200_000).hex()
    return f'{salt}${digest}'

def verify_password(password: str, stored: str) -> bool:
    try:
        salt,digest=stored.split('$',1)
        candidate=hashlib.pbkdf2_hmac('sha256',password.encode(),salt.encode(),200_000).hex()
        return hmac.compare_digest(candidate,digest)
    except ValueError: return False

def token_required(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        token=request.headers.get('Authorization','').removeprefix('Bearer ').strip() or request.args.get('token')
        if not token: return jsonify({'error':'Authentication required'}),401
        conn=get_connection(); cur=conn.cursor(dictionary=True)
        try:
            cur.execute('SELECT id, username FROM users WHERE api_token=%s AND is_active=1',(token,)); user=cur.fetchone()
        finally: cur.close(); conn.close()
        if not user: return jsonify({'error':'Invalid or expired token'}),401
        g.current_user=user
        return fn(*args,**kwargs)
    return wrapper
