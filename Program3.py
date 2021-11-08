def getMoneynPrice():
    _money = int(input("How much is your money? \n> "))
    _aplPrice = int(input("How much is the price of apple per piece? \n> "))
    return _money, _aplPrice

def getAplQuant (money_, aplPrice_):
    _aplQuant = money_ // aplPrice_
    return _aplQuant

def getTotal(aplQuant_, aplPrice_):
    _total = aplQuant_ * aplPrice_
    return _total

def getChange(_money_, total_):
    _change = _money_ - total_
    return _change

def display(aplQuantF, changeF):
    print(f"You can buy {aplQuantF} apple/s and your change is {changeF} pesos.")

money, aplPrice = getMoneynPrice()
aplQuant = getAplQuant(money, aplPrice)
total = getTotal(aplQuant, aplPrice)
change = getChange(money, total)

display(aplQuant, change)