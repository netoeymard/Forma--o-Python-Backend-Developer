class Client:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

    def __iter__(self):
        return iter((self.nome,self.email))