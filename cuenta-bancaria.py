
class Cuentabancaria:
    listadecuentas = []
    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        Cuentabancaria.listadecuentas.append(self)
#ATRIBUTOS


        #METODOS
    
    def deposito(self, amount):
        self.balance += amount
        print(f"se ha depositado {amount} en la cuenta bancaria")
        return self
    
    def retiro(self, amount):
        if self.balance < amount:
            print("Fondos insuficientes")
            self.balance -= 5
    
        self.balance -= amount
        print(f"se ha hecho un retiro de {amount} de la cuenta bancaria")
        return self
    
    def mostrar_info_cuenta (self):
        print(f"el balance de la cuenta de es  {self.balance}\n")
        return self

    def generar_interes(self):
        if self.balance > 0:
            interes = self.tasa_interes*self.balance
            self.balance = self.balance + interes
            print(f"se ha cargado un interes del {self.tasa_interes}%")
        return self

    def print_instancias(self):
        print(self.deposito)
        print(self.retiro)
        print(self.generar_interes)
        print(self.mostrar_info_cuenta)
        return self
    
    

#INSTANCIAS
cuenta1 = Cuentabancaria(0.05, 0).deposito(1000).deposito(2000).deposito(3000).retiro(5000).generar_interes().mostrar_info_cuenta()
cuenta2 = Cuentabancaria(0.1, 0).deposito(5000).deposito(8000).retiro(1000).retiro(1500).retiro(2000).retiro(1200).generar_interes().mostrar_info_cuenta()
# print(cuenta1.balance)



# class Usuario:

#     def __init__(self, nombre, email):
#         self.nombre = nombre
#         self.email = email
#         # self.cuenta = Cuentabancaria(tasa_interes=0.01, balance=0)
#         self.cuentas = []

#     def crear_cuentas(self, tipo_cuenta, tasa_interes, balance):
#         self.cuentas.append(Cuentabancaria(tasa_interes=0.01, balance=0))
#         print(f"Se ha creado exitosamente una nueva cuenta de tipo {tipo_cuenta} a nombre de {self.nombre}, su saldo es de {balance} con tasa de interes del {tasa_interes}%")

#     def hacer_deposito(self, tipo_cuenta, amount):
#         for cuenta in self.cuentas:
#             if cuenta.tipo_cuenta == tipo_cuenta:
#                 cuenta.deposito(amount)
#                 print(f"Se ha depositado {amount} en la {tipo_cuenta} de {self.nombre}, su balance es de {cuenta.balance}")
#                 return self

#     # def hacer_retiro(self, tipo_cuenta, amount):
#     #     for cuenta in self.cuentas:
#     #         if cuenta.tipo_cuenta == tipo_cuenta:
#     #             cuenta.retiro(amount)
#     #             print(f"Se ha hecho un retiro de la {tipo_cuenta} de {self.nombre}, por un monto de ${amount}. El balance de la cuenta es de {cuenta.balance}")
#     #             return self

    
#     def transferencia(self, amount, user):
#         self.cuenta.retiro(amount)
#         user.cuenta.deposito(amount)
#         self.cuenta.mostrar_info_cuenta()
#         user.cuenta.mostrar_info_cuenta()
#         return self


#     # def hacer_deposito(self, amount):
#     #     self.cuenta.deposito(amount)
#     #     print(f"{self.nombre} se deposito {amount} , el balance es {self.cuenta.balance}")
#     #     return self


# xavi = Usuario("xavier isai", "kkck@msn.com")
# xavi.crear_cuentas("Cuenta_ahorro", 0.1, 500)
# xavi.crear_cuentas("Cuenta_vista", 0.1, 800)
# # xavi.hacer_retiro("Cuenta_ahorro", 100)


# # mike = Usuario("MIKE", "asdasde@gmail.com")
# # mike.cuenta.mostrar_info_cuenta()

# # toby = Usuario("toby", "asd@gmail.com")
# # toby.cuenta.deposito(5000).mostrar_info_cuenta()
# # toby.transferencia(2000, mike)
# # print(Cuentabancaria.listadecuentas)
# # toby.hacer_deposito(5000)



# # class CuentaVitalicia(Cuentabancaria):
# #     def __init__(self, tasa_interes, balance):
# #         super().__init__(tasa_interes, balance)
# #         self.cuenta_ira = cuenta_ira
        


