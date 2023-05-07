import csv
listamailscorrectos =[]
class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __password = ''
    def __init__(self,idCuenta, dominio, tipoDominio, password):
        self.__idCuenta= idCuenta
        self.__dominio= dominio
        self.__tipoDominio= tipoDominio
        self.__password = password

    def retornaEmail(self):
        return '{}@{}.{}'.format(self.__idCuenta,self.__dominio,self.__tipoDominio)
    
    def modificarContraseña(self):
        c= input('Contraseña actual: ')
        if c==self.__password:
            self.__password= input('Contraseña nueva: ')
            print ('Su contraseña ha sido cambiada ')
        else:
            print ('contraseña incorrecta')    
        
    def obtenerEmail(self,e):
        l = e.split("@", 1)
        l2 = l[1].split(".", 1)
        self.__idCuenta = l[0]
        self.__dominio = l2[0]
        self.__tipoDominio = l2[1] if len(l2) > 1 else ''
        print('{}'.format(self.__idCuenta))
        print('{}'.format(self.__dominio))
        print('{}'.format(self.__tipoDominio))

    def getdominio (self):
        return self.__dominio

    def leermails (self):
        archivo = open ('direcciones.csv')
        reader = csv.reader (archivo, delimiter = ',')
        for fila in reader :
            if '@' in fila[0] and '.' in fila[0]:
                emails = Email('idCuenta', 'dominio', 'tipoDominio', 'password')
                print("Para {}".format(fila))
                emails.obtenerEmail(fila[0])
                listamailscorrectos.append(emails)
            else:
                print("El mail {} es invalido" .format(fila[0]))
        dominio = str(input("Ingrese dominio a buscar "))
        c=0
        for emails in listamailscorrectos:
            if dominio == emails.getdominio():
                c+=1
        print("Hay {} direcciones de email con el dominio {}" .format(c,dominio))
        return listamailscorrectos

