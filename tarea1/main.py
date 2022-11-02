import csv
lista_libros=[]
class Libro:
    def __init__(self):
        
        self.__id=0
        self.__titulo=""
        self.__genero=""
        self.__id_ISBN=""
        self.__editorial=""
        self.__autores=[]
    
    #SETTER
     def set_id(self,i):
        self.__id=i
    
    
    def set_titulo(self,tittle):
        self.__titulo=tittle
    def set_genero(self,x):
        self.__genero=x
    def set_isbn(self,code):
        self.__id_ISBN=code
    def set_editorial(self,ed):
        self.__editorial=ed
    def set_autor(self,autor):
        autor=autor.split(',')
        for i in autor:
            self.__autores.append(i)
    def set_attributes(self,id,titulo,genero,isbn,editorial,autores):
        self.__id=id
        self.__titulo=titulo
        self.__genero=genero
        self.__id_ISBN=isbn
        self.__editorial=editorial
        self.__autores=autores
    #GETTER
    def get_attributes(self):
        return self.__id,self.__titulo,self.__genero,self.__id_ISBN,self.__editorial,self.__autores
    
    def get_archivo(self):
        return self.__archivo
    def mostrar_libro(self):
        id,tit,gen,isb,edi,auto=self.get_attributes()
        print(f"{tit}, {gen}, {id}, {isb}, {edi}, {auto}")
    
    

class Sistema_libros:
    def __init__(self,lista=[]):
        self.__archivo=""
        self.libro=Libro()
        self.lista_libros=lista
    def set_list(self,libro):
        self.lista_libros.append(libro)
    
    def set_archivo(self,y):
        self.__archivo=y
    
    def get_archivo(self):
        return self.__archivo

    def listar_libros(self):
        print("Listado de libros")
        for v,a in enumerate(self.lista_libros,start=1):
            print(f"{v}->",end=" ")
            a.mostrar_libro()
    
    def leer_archivo(self,name):
        self.set_archivo(name)
        with open(self.get_archivo()) as f:
                # next(f)
            x=csv.reader(f)
            next(x)
            for row in x :
                self.libro.set_id(row[0])
                self.libro.set_titulo(row[1])
                self.libro.set_genero(row[2])
                self.libro.set_isbn(row[3])
                self.libro.set_editorial(row[4])
                self.libro.set_autor(row[5])
                self.lista_libros.append(self.libro)

libro=Sistema_libros()
libro.leer_archivo('libro.csv')
libro.listar_libros()

