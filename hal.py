
class Lixo:
    
    def __init__(self, distancia_inicial):
        self.distancia_inicial = distancia_inicial
        self.movimento = True
        self.tampa_lixo = "aberta"

    def preenchimento_atual(self, distancia_atual):
        distancia_lixo = self.distancia_inicial - distancia_atual
        preenchimento_lixo = distancia_lixo / self.distancia_inicial
        self.preenchimento_percentual = (100 - (preenchimento_lixo * 100))

        return self.preenchimento_percentual

    def tampa(self, movimento):
        if movimento:
            self.tampa_lixo = 1
        else:
            self.tampa_lixo = 0
        return self.tampa_lixo

    def coletar_lixo(self, coletar_lixo):
        print("lixo coletado")
