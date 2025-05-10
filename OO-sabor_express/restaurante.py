class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.status = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"Nome: {self.nome}, Categoria: {self.categoria}, Status: {self.status}"
    
    def listar():
        c = 0
        for r in Restaurante.restaurantes:
            c += 1
            print(f"Restaurante {c} --> Nome: {r.nome} | Categoria: {r.categoria} | Status: {r.status}")
    
rest01 = Restaurante("Sushi", "Japonesa")
rest02 = Restaurante("Churrasco", "Brasileiro")

Restaurante.listar()