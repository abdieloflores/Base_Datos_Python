import pymysql

_host='localhost'
_user='root'
_password='gafo951101'
_db='PuntoVenta'

#INSERTAR
def insertVendedor(a,b,c):

    try:
        conexion = pymysql.connect(host=_host,user=_user,password=_password,db=_db)
        try:
            with conexion.cursor() as cursor:
                insertar = (
                "INSERT INTO Vendedores (v_Usuario,v_Contrasena,v_Nombre)"
                "VALUES(%s,%s,%s)"
                )
                datos = (a,b,c)
                cursor.execute(insertar,datos)
            conexion.commit()
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)

#CONSULTAR
def consultarVendedor():
    try:
        conexion = pymysql.connect(host=_host,user=_user,password=_password,db=_db)
        try:
            with conexion.cursor() as cursor:
                # En este caso no necesitamos limpiar ningún dato
                cursor.execute("SELECT v_Id, v_Usuario, v_Contrasena,v_Nombre FROM Vendedores;")
    
                # Con fetchall traemos todas las filas
                vendedores = cursor.fetchall()
    
                # Recorrer e imprimir
                for vendedor in vendedores:
                    print(vendedor)
        finally:
            conexion.close()
        
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)

#ACTUALIZAR
def actualizarVendedor(a,b,c,num):
    
    try:
        conexion = pymysql.connect(host=_host,user=_user,password=_password,db=_db)
        try:
            with conexion.cursor() as cursor:
                
                consulta = (
                    "UPDATE `Vendedores`"
                    "SET"
                    "`v_Usuario`= %s,"
                    "`v_Contrasena`= %s,"
                    "`v_Nombre`= %s "
                    "WHERE"
                    "(`v_Id`= %s)"
                    )
                cursor.execute(consulta, (a,b,c, num))
                
            conexion.commit()
        finally:
            conexion.close()
        
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)

def borrarVendedor(a):
    try:
        conexion = pymysql.connect(host=_host,user=_user,password=_password,db=_db)
        try:
            with conexion.cursor() as cursor:
                
                consulta = "DELETE FROM Vendedores WHERE v_Id = %s;"
                cursor.execute(consulta, (a))
            conexion.commit()
        finally:
            conexion.close()   
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)

print("NUEVO VENDEDOR EN BASE DE DATOS\n")
c = input("Ingrese su nombre: ")
a = input("Ingrese Usuario: ")
b = input("Ingrese Contraseña: ")

insertVendedor(a,b,c)
print("\n\n+++++++++++++++++++++++++++++++++++++\n\n\n")
consultarVendedor()

print("\n\n\nACTUALIZAR VENDEDOR EN BASE DE DATOS\n")
num = input("Numero de registro a actualizar: ")
c = input("Ingrese su nombre: ")
a = input("Ingrese Usuario: ")
b = input("Ingrese Contraseña: ")

actualizarVendedor(a,b,c,num)
consultarVendedor()

print("\n\n\nBORRAR VENDEDOR EN BASE DE DATOS\n")
num = input("Numero de registro a BORRAR: ")

borrarVendedor(num)
consultarVendedor()