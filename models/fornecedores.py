from sql_alchemy import banco


class FornecedorModel(banco.Model):
    __tablename__ = "fornecedores"

    company = banco.Column(banco.String,primary_key = True)
    name = banco.Column(banco.String(80))
    id = banco.Column(banco.String(200))
    created_at = banco.Column(banco.String(50))
    amount_of_products = banco.Column(banco.Integer)

    def __init__(self, company, id, name, created_at, amount_of_products):
        self.company = company
        self.id = id
        self.name = name
        self.created_at = created_at
        self.amount_of_products = amount_of_products

    def json(self):
        return {
        
            'company': self.company,
            'id' : self.id,
            'name': self.name,
            'created_at' : self.created_at,
            'amount_of_products' : self.amount_of_products
        }

    @classmethod
    def search_fornecedor(cls,company):

        fornecedor = cls.query.filter_by(company = company).first()
        if fornecedor:
            return fornecedor

        return None

    def save_fornecedor(self):
        banco.session.add(self)
        banco.session.commit()

    def update_fornecedor(self, id, name, created_at, amount_of_products):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.amount_of_products = amount_of_products

    def delete_fornecedor(self):
        banco.session.delete(self)
        banco.session.commit()