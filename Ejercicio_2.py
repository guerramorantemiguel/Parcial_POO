import animal from

class animal:
  def __init__(self,especie):
    self.especie = especie

  def clasificacion(self):
    especie = input("Introduzca el animal que desea clasificar ")
    if especie == "Pollo":
      print("Animal, ovíparo")
    if especie == "Gato":
      print("Animal, mamífero")
    if especie == "Ornitorrinco":
      print("Animal, mamífero, ovíparo")
    
