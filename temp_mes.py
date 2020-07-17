class TempMes:
  def __init__(self, mes, ano):
    self.mes = mes
    self.ano = ano
    self.temps = []
    
  def inclui_temp(self, temperatura):
    self.temps.append(float(temperatura))
    
  def retorna_media(self):
    return sum(self.temps) / len(self.temps)
    
  def retorna_maxima(self):
    return max(self.temps)
  
  def retorna_minima(self):
    return min(self.temps)