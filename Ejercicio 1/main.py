from email import Email
if __name__ == '__main__':
    print('Ingrese su nombre y direccion de email')

    persona= input('Nombre: ')
    
    unMail = Email(input('ID de cuenta: '),input('Dominio: '),input('Tipo de Dominio: '),input('Contraseña: '))
    
    print('Estimado {} te enviaremos tus mensajes a la direccion {}'.format(persona,unMail.retornaEmail()))
    unMail.modificarContraseña()

    e = (input('Ingrese direccion de mail '))
    Mail2 = unMail.obtenerEmail(e)

    otromail = Email('idCuenta', 'dominio', 'tipoDominio', 'contraseña')
    print ("Lista de emails: {}".format(otromail.leermails()))



    