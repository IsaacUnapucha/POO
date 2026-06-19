class CajaRegistradora:

    #ATRIBUTOS DE CLASE O GLOBALES
    ventas_totales_empresas = 0.0
    cajas_registradoras = 0

    def __init__(self, numero_caja, nombre_cajero):
        self.__numero_caja = numero_caja
        self.__nombre_cajero = nombre_cajero
        self.__recaudacion = 0.0

        #ACTUALIZA EL CONTADOR GLOBAL AL NACER OBJETO
        CajaRegistradora.cajas_registradoras +=1


    @property
    def numero_caja(self):
        return self.__numero_caja
    
    
    @property
    def nombre_cajero(self):
        return self.__nombre_cajero
    
    
    @property
    def recaudacion (self):
        return self.__recaudacion
    

    @nombre_cajero.setter
    def nombre_cajero(self, nuevo_nombre):

        #isintance permite que una instancia cumpla ciertas condiciones 

        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip () != "":
            self.__nombre_cajero = nuevo_nombre
            print (f"Cambio de turno: El nuevo cajero es {self.__nombre_cajero}")

        else:
            print("El nombre del cajero no puede estar vacio")


    def __str__(self):
        return f"Caja {self.numero_caja} / Cajero: {self.nombre_cajero} / Recaudacion de turno ${self.recaudacion}"
    
    def cobrar_venta (self, monto):

        if monto > 0:
            self.__recaudacion += monto
            CajaRegistradora.ventas_totales_empresas += monto

            print(f"Venta de {monto:.2f} registradora de caja {self.numero_caja}")

        else:
            print ("Error: El monto de venta es invalido ")


#METODO DE CLASE
    @classmethod
    def reporte_global(cls):
        print ("="*45)
        print("REPORTE GERENCIAL DEL SUPERMERCADO")
        print(f"Cajas Operativas Actualmente: {cls.cajas_registradoras}")
        print(f"Ingresos Totales Acumulados: {cls.ventas_totales_empresas:.2f}")
        print("="*45)





CajaRegistradora.reporte_global()

caja1 =CajaRegistradora(1, "Ana")
caja2 =CajaRegistradora(2,"Luis")

caja1.cobrar_venta(50)
caja2.cobrar_venta(100)
caja1.cobrar_venta(20)

caja1.nombre_cajero = ""

print("------ESTADO INDIVIDUAL DE CAJAS-----")
print(caja1)
print(caja2)


CajaRegistradora.reporte_global()







