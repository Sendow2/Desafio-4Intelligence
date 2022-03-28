from flask_restful import Resource, reqparse
from datetime import datetime
from models.fornecedores import FornecedorModel



class Fornecedores(Resource):
    #READ com todas os fornecedores cadastrados
    def get(self):
        return {"Fornecedores": [fornecedor.json() for fornecedor in FornecedorModel.query.all()]}


class Fornecedor(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('id',type = str, required = True, help = 'ID can not be blank')
    argumentos.add_argument('name',type = str, required = True, help = 'Name can not be blank')
    argumentos.add_argument('created_at',type = str, required = True, help = 'Date and time of creation can not be blank')
    argumentos.add_argument('amount_of_products',type = int, required = True, help = 'The amount of products of the company can not be blank')
    
    #READ escolhendo apenas uma empresa para mostrar do banco de dados
    def get(self, company):
        fornecedor = FornecedorModel.search_fornecedor(company)
        if fornecedor:
            return fornecedor.json()
        return {'Message' : 'Company not found'}, 404 # not found

    #CREATE
    def post(self, company):
        if FornecedorModel.search_fornecedor(company):
            return {"Message": "{} supplier already exists!".format(company)}

        dados = Fornecedor.argumentos.parse_args()
        fornecedor = FornecedorModel(company,**dados)
        try:
            fornecedor.save_fornecedor()
        except:
            return {'Message':'There was an error while trying to save the new supplier'}, 500

        return fornecedor.json()

    #CREATE/UPDATE
    def put(self, company):

        dados = Fornecedor.argumentos.parse_args()
        fornecedor_encontrado = FornecedorModel.search_fornecedor(company)

        if fornecedor_encontrado:
            fornecedor_encontrado.update_fornecedor(**dados)
            fornecedor_encontrado.save_fornecedor()
            return fornecedor_encontrado.json(), 200 #fornecedor atualizado com sucesso

        fornecedor = FornecedorModel(company,**dados)            
        try:
            fornecedor.save_fornecedor()
        except:
            return {'Message':'There was an error while trying to save the new supplier'}, 500
        return fornecedor.json(), 201 #fornecedor criado

    #DELETE
    def delete(self, company):
        fornecedor = FornecedorModel.search_fornecedor(company)
        if fornecedor:
            try:
                fornecedor.delete_fornecedor()
            except:
                return {'Message' : 'There was an error while trying to delete the supplier.'}, 500
            return {"Message": "Company deleated!"}
        return {"Message" : 'Company not found!'}, 404
