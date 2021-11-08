from collections import Counter

class box():
    def __init__(self, money_dict={}):
        self.validValues = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
        if money_dict != {}:
            for key in money_dict:
                if key not in self.validValues:
                    raise ValueError(f"Denominacion \"{key}\" no permitida.")
                if type(money_dict[key]) != type(int()):
                    raise ValueError(f"Solo se puede tener una cantidad entera de billetes. Cantidad invalida: {money_dict[key]} billetes de {key} pesos.")
                if money_dict[key] < 0:
                    raise ValueError(f"Solo se puede tener una cantidad positiva de billetes. Cantidad invalida: {money_dict[key]} billetes de {key} pesos.")
        
        self.moneyDict = money_dict

    def add(self, value):
        self.moneyDict = self + value

        subtotal = 0
        for key in self.moneyDict:
            subtotal += key * self.moneyDict[key]

        print(f"Pesos agregados: {subtotal} pesos")

        return self.moneyDict

    def substract(self, value):
        self.moneyDict = self - value

        subtotal = 0
        for key in self.moneyDict:
            subtotal += key * self.moneyDict[key]

        print(f"Pesos removidos: {subtotal} pesos")

        return self.moneyDict

    def __str__(self):
        subtotal = 0
        for key in self.moneyDict:
            subtotal += key * self.moneyDict[key]

        return f"Caja {self.moneyDict}  total: {subtotal} pesos"

    def __add__(self, other):
        """Al sumarle a una caja un diccionario u otra caja, se devuelve un diccionario.
        Esto esta pensado para que se le tenga que asignar el valor de la suma al moneyDict de una caja en vez de reasignar el objeto entero."""
        tempDict = dict()
        if isinstance(other, box):
            if other.moneyDict != {}:
                tempDict = other.moneyDict
            else:
                return self.moneyDict

        elif isinstance(other, type(dict())):
            if other != {}:
                for key in other:
                    if key not in self.validValues:
                        raise ValueError(f"Denominacion \"{key}\" no permitida.")
                tempDict = other
            else:
                return self.moneyDict

        else:
            raise Exception("A una caja solo se le puede sumar otra caja o un diccionario.")

        tempDict = dict( Counter(tempDict) + Counter(self.moneyDict) )
        #tempBox = box()
        #tempBox.moneyDict = tempDict
        
        return tempDict

    def __sub__(self,other):
        """Al restarle a una caja un diccionario u otra caja, se devuelve un diccionario.
        Esto esta pensado para que se le tenga que asignar el valor de la suma al moneyDict de una caja en vez de reasignar el objeto entero."""
        tempDict = dict()
        if isinstance(other, box):
            if other.moneyDict != {}:
                tempDict = other.moneyDict
            else:
                return self.moneyDict

        elif isinstance(other, type(dict())):
            if other != {}:
                #for key in other:
                #    if key not in self.validValues:
                #        raise ValueError(f"Denominacion \"{key}\" no permitida.")
                tempDict = box(other).moneyDict
            else:
                return self.moneyDict
        else:
            raise ValueError("A una caja solo se le puede restar otra caja o un diccionario.")
        
        for key in tempDict:
            if key in self.moneyDict:
                if self.moneyDict[key] < tempDict[key]:
                    raise ValueError(f"No hay suficientes billetes de denominacion \"{key}\".")
            else:
                    raise ValueError(f"No hay suficientes billetes de denominacion \"{key}\".")

        tempDict = dict( Counter(self.moneyDict) - Counter(tempDict) )
        #tempBox = box()
        #tempBox.moneyDict = tempDict
        
        return tempDict
