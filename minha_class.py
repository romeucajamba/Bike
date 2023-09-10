class Bicicleta:
    def __init__(self, cor, modelo, valor, ano, aro=18):
        self.cor = cor
        self.modelo = modelo 
        self.valor = valor 
        self.ano = ano
        self.aro = aro
    
    def buzinar(self):
        print("Priimm priimm!")
    
    def parar(self):
        print("Parando...")
        print("Bicicleta parada")
    
    def correr(self):
        print("Vruummm")
    
    def marcha(self):
        print("Trocar marcha...")
        print("Marcha trocada!")

    def __str__(self):
        #Dessa forma não teremos mais que escrever toda hora
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"#meu dicionario, sendo iterado e mostrar as chaves e valores

objt = Bicicleta("Amarela", "Renault", 16000, 2008)


objt.parar() 
objt.buzinar()
objt.correr()
objt.parar() 


print(objt)