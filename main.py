from temp_mes import TempMes

class TempManager:

  def __init__(self):
    self.temps_por_mes = {}

  def le_temps(self, nome_arquivo):
    with open(nome_arquivo, 'r') as arq:
      for linha in arq:
        lista_linha = linha.strip().split(';')
        mes = lista_linha[1]
        ano = lista_linha[2]
        temp = lista_linha[4]
        if temp:
          if mes not in self.temps_por_mes:
            self.temps_por_mes[mes] = TempMes(mes, ano)
          self.temps_por_mes[mes].inclui_temp(temp)
  

  def imprime_valores(self):
    for chave in sorted(self.temps_por_mes):
      media = self.temps_por_mes[chave].retorna_media()
      minima = self.temps_por_mes[chave].retorna_minima()
      maxima = self.temps_por_mes[chave].retorna_maxima()
      print(f'{chave} -> min={minima:.1f}, med={media:.1f}, max={maxima:.1f}')

def main():
  tm = TempManager()
  tm.le_temps('temps_portoalegre.csv')
  tm.imprime_valores()

if __name__ == "__main__":
  main()

