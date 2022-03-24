class Banco:
  def __init__(self, ID, nombre, fecha, numerocuenta, saldo, importe):
    self.ID = ID
    self.nombre = nombre
    self.fecha  = fecha
    self.numerocuenta = numerocuenta
    self.saldo = saldo
    self.importe = importe
  def retirar_dinero(self, importe):
    self.saldo -= importe
    return
  def ingresar_dinero(self, importe):
    self.saldo += importe
    return
  def transferir_dinero(self, importe):
    
    
    
    