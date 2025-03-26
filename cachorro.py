class Cachorro:
    def _init_(self, nome, raca, comida):
        self.nome = nome
        self.raca = raca
        self.comida = comida
        self.acordado = True
        self.feliz = False

    def comer(self):
        if self.comida > 0:
            self.comida -= 1
            self.feliz = True
            print(f"{self.nome} comeu e está feliz!")
        else:
            print(f"{self.nome} não tem comida suficiente para comer.")

    def dormir(self):
        self.acordado = False
        print(f"{self.nome} foi dormir.")

    def acordar(self):
        self.acordado = True
        print(f"{self.nome} acordou!")

    def brincar(self):
        if self.acordado:
            self.feliz = True
            print(f"{self.nome} brincou e está muito feliz!")
        else:
            print(f"{self.nome} está dormindo e não pode brincar agora.")

    def ignorar(self):
        self.feliz = False
        print(f"{self.nome} está triste porque foi ignorado.")

    def latir(self):
        if self.acordado:
            print(f"{self.nome} está latindo: Au Au!")
        else:
            print(f"{self.nome} está dormindo e não pode latir.")

# Criando objetos da classe Cachorro
cachorro1 = Cachorro("Rex", "Labrador", 3)
cachorro2 = Cachorro("Bolt", "Pastor Alemão", 2)

# Interagindo com os cachorros
cachorro1.comer()
cachorro1.latir()
cachorro1.dormir()
cachorro1.latir()
cachorro1.acordar()
cachorro1.ignorar()

cachorro2.comer()
cachorro2.brincar()
cachorro2.dormir()