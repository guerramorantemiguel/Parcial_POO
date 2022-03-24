class libro:
  def __init__(self, titulo, autor, genero, ISBN):
    self.titulo = titulo
    self.autor = autor
    self.genero = genero
    self.ISBN = ISBN
  def setTitulo(self):
    return self.titulo
  def setAutor(self):
    return self.autor
  def setGenero(self):
    return self.genero
  def setISBN(self):
    return self.ISBN

  def mostrarLibro(self):
    print("n\Titulo: "+ self.setTitulo()+"n\Autor: "+self.setAutor()+"n\Genero: "+ self.setGenero()+"n\ISBN: "+str(self.setISBN()))
  
titulo = raw_input("Por favor ingrese el título ")
autor = raw_input("Por favor ingrese el autor ")
genero = raw_input("Por favor ingrese el género ")
ISBN = input("Por favor ingrese el ISBN ")
l = Libro(titulo, autor, genero, ISBN)
l.mostrarLibro