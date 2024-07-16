from datetime import date

databaseUsers = []
guia = {}

class Operacion:
    def __init__(self, origen, destino, valor, fecha):
        self.origen = origen
        self.destino = destino
        self.valor = valor
        self.fecha = fecha

class CuentaUsuario:
    def __init__(self, numero, nombre, saldo, numerosContacto):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.numerosContacto = numerosContacto
        self.historial = []
        self.crearCuenta(numero, nombre, saldo, numerosContacto)
    
    def crearCuenta(self, numero, nombre, saldo, numerosContacto):
        guia[numero] = CuentaUsuario(numero, nombre, saldo, numerosContacto)
    
    def pagar(self, destino, valor):
        # 1. Destino esta en contactos
        # 2. Valor <= saldo
        if destino not in self.numerosContacto:
            return False
        if valor > self.saldo:
            return False
        self.saldo -= valor
        op = Operacion(self.numero, destino, valor, date.today)
        self.historial.append(op)

        if destino != self.numero:
            des = guia[destino]
            des.historial.append(op)
        
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