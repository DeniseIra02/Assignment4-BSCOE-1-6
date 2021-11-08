def getMoneynPrice():
    _money = int(input("How much is your money? \n> "))
    _aplPrice = int(input("How much is the price of apple per piece? \n> "))
    return _money, _aplPrice

def getAplQuant (money_, aplPrice_):
    _aplQuant = money_ // aplPrice_
    return _aplQuant