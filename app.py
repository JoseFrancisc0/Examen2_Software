from datetime import date

databaseUsers = []
guia = {}

class Operacion:
    def __init__(self, origen, destino, valor, fecha):
        self.origen = origen
        self.destino = destino
        self.valor = valor
        self.fecha = fecha

    def __str__(self):
        return(f"origen={self.origen}, destino={self.destino}, "
                f"valor={self.valor}, fecha={self.fecha}")

class CuentaUsuario:
    def __init__(self, numero, nombre, saldo, numerosContacto):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.numerosContacto = numerosContacto
        self.historial = []
        self.crearCuenta()
    
    def crearCuenta(self):
        guia[self.numero] = self
    
    def pagar(self, destino, valor):
        # 1. Destino esta en contactos
        # 2. Valor <= saldo
        if destino.numero not in self.numerosContacto:
            return False
        if valor > self.saldo:
            return False
        self.saldo = self.saldo - valor
        op = Operacion(self, destino, valor, date.today)
        self.historial.append(op)
        destino.historial.append(op)
        
        return True

    def historialOperaciones(self):
        print("Saldo de ", self.nombre, ": ", self.saldo)
        print("Operaciones de ", self.nombre)
        for op in self.historial:
            if op.origen == self.numero:
                other = guia[op.destino.numero]
                print("Pago realizado de ", op.valor, " a ", other.nombre)
            if op.destino == self.numero:
                other = guia[op.origen.numero]
                print("Pago recibido de ", op.valor, " de ", other.nombre)

    def contactos(self):
        for n in self.numerosContacto:
            c = guia[n]
            print(c.numero, ": ", c.nombre)

    def __str__(self):
        return(f"numero={self.numero}, nombre={self.nombre}, "
                f"saldo={self.saldo}, numerosContacto={self.numerosContacto}")

luisa = CuentaUsuario(123, "Luisa", 400, [456])
andrea = CuentaUsuario(456, "Andrea", 300, [123])

print(luisa)
luisa.pagar(andrea, 200)
print(luisa)

