import csv



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
        self.__autores.append(autor)
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

    def get_titulo(self):
        return self.__titulo
    def get_autores(self):
        return self.__autores
    def get_editorial(self):
        return self.__editorial
    def get_archivo(self):
        return self.__archivo
    def get_genero(self):
        return self.__genero
    def get_id(self):
        return self.__id
    def get_isbn(self):
        return self.__id_ISBN
    #Funciones
    def mostrar_autores(self):
        auto=self.__autores
        for i in range(len(auto)):
            if(i==len(auto)-1):
                print(f"{auto[i]}",end="\n")
            else:
                print(f"{auto[i]}, ",end=" ")
    def mostrar_libro(self):
        id,tit,gen,isb,edi,auto=self.get_attributes()
        # print(tit)
        # ,gen,id,isb,edi,auto,sep=" ")
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
            id,tit,gen,isb,edi,auto=a.get_attributes()
            print(f"{v} -> {tit}, {gen}, {id}, {isb}, {edi}, ",end=" ")
            a.mostrar_autores()

    def agregar_libro(self):
        print("Ingrese los siguientes datos del libro: ")
        nm=self.libro
        nm.set_titulo(input("Título del libro: "))
        nm.set_genero(input("Género del libro: "))
        nm.set_isbn(input("ID o ISBN: "))
        nm.set_id(len(self.lista_libros))
        nm.set_editorial(input("Editorial: "))
        nmk=int(input("Ingrese la cantidad de autores: "))
        autor=[]
        for vk in range(nmk):
            a=input(f"Ingrese el autor {vk+1}: ")
            nm.set_autor(a)
        
        self.set_list(nm)
    
    def leer_archivo(self,name):
        self.set_archivo(name)
        with open(name) as f:
            x=csv.reader(f)
            next(x)
            for row in x :
                # print()
                new_val=Libro()
                new_val.set_id(row[0])
                new_val.set_titulo(row[1])
                new_val.set_genero(row[2])
                new_val.set_isbn(row[3])
                new_val.set_editorial(row[4])
                lista=[]
                for l in str(row[5]):
                    if l.isalpha() or l==' ' or l==',':
                        lista.append(l)
                    new_row_5="".join(lista)
                                     
                val_autor=new_row_5.split(',')

                for k in val_autor:
                    new_val.set_autor(k)

                
            
                self.lista_libros.append(new_val)
    def eliminar_libro(self):
        eliminar=input("Ingrese el título del libro: ")
        for el in self.lista_libros:
            if el.get_titulo()==eliminar:
                self.lista_libros.remove(el)
                return True
        return False
            
    
    def buscar_libro(self):
        busqueda=input("Ingrese ISBN o título del libro: ")
        for k in self.lista_libros:
            if k.get_isbn()==busqueda or k.get_titulo()==busqueda:
                id,titulo,genero,isbn,editoria,_=k.get_attributes()
                # print("id \t\t titulo \t\t genero \t\t isbn \t\t editorial")
                print(f"{id} ,{titulo}, {genero}, {isbn}, {editoria}, ",end="")
                k.mostrar_autores()
    
    def ordenar_libros(self):
        orden_lista=[]
        print("Ordenar libros por título")
        orden_lista=[i.get_titulo().lower() for i in self.lista_libros]
        orden_lista_titulo=sorted(orden_lista)
        lista_libros_nuevo=[]
        for kv2 in orden_lista_titulo:
            for kv1 in self.lista_libros:
                if kv2==kv1.get_titulo().lower():
                    id,titulo,genero,isbn,editoria,_=kv1.get_attributes()
                    print(f"{titulo}, {genero}, {isbn}, {editoria}, ",end="")
                    kv1.mostrar_autores()
    
    def buscar_libros_autor(self):
        val=False
        print("Buscar libros por autor, editorial o género")
        print("Buscar libro por autor")
        entrada=input("Ingrese el autor del libro: ").lower()
        for nk in self.lista_libros:
            # print(type(list(nk.get_autores())))
            for mk in nk.get_autores():
                if mk.lower()==entrada:
                    print("Se encontro una coincidencia")
                    id,titulo,genero,isbn,editoria,_=nk.get_attributes()
                    print(f"{titulo}, {genero}, {isbn}, {editoria} ")
                    val=True
        return val
    
    def buscar_libro_editorial(self):
        val=False
        entrada=input("Ingrese la editorial del libro: ").lower()
        for x in self.lista_libros:
            if x.get_editorial().lower() ==  entrada:
                print("Se encontro una coincidencia")
                id,titulo,genero,isbn,_,_=x.get_attributes()
                print(f"{id}, {titulo}, {genero}, {isbn}, ",end="")
                x.mostrar_autores()
                val=True
        return val
    
    def buscar_libro_genero(self):
        val=False
        entrada=input("Ingrese el genero del libro: ").lower()
        for x in self.lista_libros:
            if x.get_genero().lower() ==  entrada:
                print("Se encontro una coincidencia")
                id,titulo,_,isbn,editorial,_=x.get_attributes()
                print(f"{id}, {titulo}, {isbn}, {editorial}, ",end="")
                x.mostrar_autores()
                val= True
        return val
    def buscar_libros_num_autor(self):
        print("Buscar libros por el número de autores")
        num_autor=int(input("Ingrese la cantidad de autores: "))
        for x in self.lista_libros:
            # print(len(x.get_autores()))
            if len(x.get_autores())==num_autor:
                id,titulo,genero,isbn,editorial,_=x.get_attributes()
                print(f"{id}, {titulo}, {genero}, {isbn}, {editorial}, ",end="")
                x.mostrar_autores()

    def editar_libro(self):
        id_libro=int(input("Ingrese el id del libro a modificar: "))
        for x in self.lista_libros:
            # print(type(x.get_id()))
            if int(x.get_id())==id_libro:
                id,titulo,genero,isbn,editorial,autor=x.get_attributes()
                print(f"{id}, {titulo}, {genero}, {isbn}, {editorial}, ",end="")
                x.mostrar_autores()
                indice=self.lista_libros.index(x)
                self.lista_libros.remove(x)
                print("Las opciones a modificar son: ")
                print("titulo\ngenero\nisbn\neditorial\nautor")
                modif=input("Que desea modificar?: ").lower()
                while(modif not in ["titulo","genero","isbn","editorial","autor"]):
                    modif=input("Opcion no valida, vuelve a intentar: ")
                if modif=='id':
                        print("No se puede modificar el id")
                elif modif=='titulo':
                    mod_title=input("Ingrese el nuevo titulo: ").title()
                    titulo=mod_title
                    x.set_attributes(id,mod_title,genero,isbn,editorial,autor)
                elif modif=='genero':
                    mod_genero=input("Ingrese el nuevo genero: ")
                    genero=mod_genero
                    x.set_attributes(id,titulo,mod_genero,isbn,editorial,autor)
                elif modif=='isbn':
                    mod_isbn=input("Ingrese el nuevo isbn: ")
                    isbn=mod_isbn
                    x.set_attributes(id,titulo,genero,mod_isbn,editorial,autor)
                elif modif=='editorial':
                    mod_edi=input("Ingrese la nueva editorial: ")
                    editorial=mod_edi
                    x.set_attributes(id,titulo,genero,isbn,mod_edi,autor)
                elif modif=='autor':
                    number=int(input("Cuantos desea agregar: "))
                    autor=[]
                    for i in range(number):
                        mod_autor=input("Ingrese el autor: ")
                        autor.append(mod_autor)
                    x.set_attributes(id,titulo,genero,isbn,editorial,autor)
                print("Atributos cambiados....")

                id1,titulo1,genero1,isbn1,editorial1,autor1=x.get_attributes()
                print(f"{id1}, {titulo1}, {genero1}, {isbn1}, {editorial1}, ",end="")
                x.mostrar_autores()
                self.lista_libros.insert(indice,x)
    def guardar_libros(self):
        print("Guardar libros (.CSV o .txt)")
        mi_archivo=open('biblioteca.csv','w',newline='')
        with mi_archivo:
            escritura = csv.writer(mi_archivo)
            escritura.writerows([["ID,TITULO, GENERO, ISBN, EDITORIAL, AUTORES"]])
            for lib in self.lista_libros:
                id,titulo,genero,isbn,editorial,autor=lib.get_attributes()
                mi_dato=[[id,titulo, genero, isbn, editorial, autor]]
                escritura.writerows(mi_dato)
            print("¡Completado!")

               
                
                
                    


    
    

libro=Sistema_libros()
libro.leer_archivo('biblioteca.csv')
# libro.agregar_libro()
# libro.eliminar_libro()
# libro.buscar_libro()
# libro.ordenar_libros()
libro.buscar_libros_autor()
# libro.buscar_libro_editorial()
# libro.buscar_libro_genero()
libro.buscar_libros_num_autor()
# libro.editar_libro()
libro.guardar_libros()
libro.listar_libros()
