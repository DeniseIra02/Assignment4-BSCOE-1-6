def getAplOrng():
    _apl = int(input("How many apple do you want to buy? \n> "))
    _orng = int(input("How many orange do you want to buy? \n> "))
    return _apl, _orng

def getAplOrngPriceTotal(quantApl, quantOrng):
    _aplPrice = quantApl * 20 
    _orngPrice = quantOrng * 25 
    overallTtl = _aplPrice + _orngPrice
    return overallTtl

def display(totalF):
    print(f"The total amount is {totalF} pesos.")

aplQuant, orngQuant = getAplOrng()
total = getAplOrngPriceTotal(aplQuant, orngQuant)

display(total)