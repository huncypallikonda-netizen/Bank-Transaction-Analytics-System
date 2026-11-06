from flask import Flask,jsonify
from flask_cors import CORS
from config import Config
from routes.auth_routes import bp as auth_bp
from routes.transaction_routes import bp as transaction_bp
from routes.dashboard_routes import bp as dashboard_bp
from routes.report_routes import bp as report_bp

def create_app():
    app=Flask(__name__);app.config.from_object(Config);CORS(app,resources={r'/api/*':{'origins':'*'}})
    app.register_blueprint(auth_bp,url_prefix='/api');app.register_blueprint(transaction_bp,url_prefix='/api');app.register_blueprint(dashboard_bp,url_prefix='/api');app.register_blueprint(report_bp,url_prefix='/api')
    @app.get('/api/health')
    def health(): return jsonify({'status':'ok','application':'BankSight'})
    return app
if __name__=='__main__': create_app().run(host='127.0.0.1',port=5000,debug=True)
