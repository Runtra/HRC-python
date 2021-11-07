from collections import Counter

class box():
    def __init__(self, money_dict={}):
        self.validValues = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
        if money_dict != {}:
            for key in money_dict:
                if key not in self.validValues:
                    raise ValueError(f"Denominacion \"{key}\" no permitida.")
        
        self.moneyDict = money_dict


    def __str__(self):
        subtotal = 0
        for key in self.moneyDict:
            subtotal += key * self.moneyDict[key]

        return f"Caja {self.moneyDict}  total: {subtotal} pesos"

    def __add__(self, other):
        tempDict = dict()
        if isinstance(other, box):
            tempDict = other.moneyDict

        elif isinstance(other, type(dict())):
            if other != {}:
                for key in other:
                    if key not in self.validValues:
                        raise ValueError(f"Denominacion \"{key}\" no permitida.")
                tempDict = other
        else:
            raise Exception("A una caja solo se le puede sumar otra caja o un diccionario.")

        tempDict = dict( Counter(tempDict) + Counter(self.moneyDict) )
        tempBox = box()
        tempBox.moneyDict = tempDict
        
        return tempBox

    def __sub__(self,other):
        tempDict = dict()
        if isinstance(other, box):
            tempDict = other.moneyDict

        elif isinstance(other, type(dict())):
            if other != {}:
                for key in other:
                    if key not in self.validValues:
                        raise ValueError(f"Denominacion \"{key}\" no permitida.")
                tempDict = other
        else:
            raise Exception("A una caja solo se le puede restar otra caja o un diccionario.")
        
        for key in tempDict:
            if key in self.moneyDict:
                if self.moneyDict[key] < tempDict[key]:
                    raise ValueError(f"No hay suficientes billetes de denominacion \"{key}\".")
            else:
                    raise ValueError(f"No hay suficientes billetes de denominacion \"{key}\".")

        tempDict = dict( Counter(self.moneyDict) - Counter(tempDict) )
        tempBox = box()
        tempBox.moneyDict = tempDict
        
        return tempBox
