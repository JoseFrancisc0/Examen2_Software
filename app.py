from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Instanciar SQLAlchemy
billetera_api = Flask(__name__)
billetera_api.config['SQLALCHEMY_DATABASE_URI'] = "Database Link"
billetera_api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(billetera_api)
CORS(billetera_api)

# Modelo
class Modelo(db.Model):
    __tablename__ = 'modelo'
    def __repr__(self):
        return f'<Modelo {self.id}>'

# 400 error handler
@billetera_api.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request.'}), 400

# 404 error handler
@billetera_api.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found.'}), 404

# 500 error handler
@billetera_api.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error.'}), 500
    
# Run
if __name__ == '__main__':
    billetera_api.run(host = '0.0.0.0', port = 8001, debug = True)