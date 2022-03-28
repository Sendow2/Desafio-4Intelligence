from flask import Flask
from flask_restful import Api
from resources.fornecedores import Fornecedores, Fornecedor



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQL_ALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)


@app.before_first_request
def cria_banco():
    banco.create_all()



api.add_resource(Fornecedores,'/fornecedores')
api.add_resource(Fornecedor, '/fornecedores/<string:company>')


if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)

#http://127.0.0.1:5000/fornecedores
