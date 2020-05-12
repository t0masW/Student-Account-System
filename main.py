StudentData = open("DataList1.csv","r")
FoodData = open("DataList2.csv","r")

def getFootData(fileName):
    Item = []
    Cost = []
    for lines in fileName:
        lines = lines.rstrip()
        lines = lines.split(",")
        item = lines[0]
        cost = lines[1]
        Item.append(item)
        Cost.append(cost)
    return Item, Cost

def getStudentData(fileName):
    Codes = []
    Balence = []
    fName = []
    sName = []
    for lines in fileName:
        lines = lines.rstrip()
        lines = lines.split(",")
        StudentCode = lines[0]
        FirstName = lines[1]
        LastName = lines[2]
        Amount = (lines[3])
        Codes.append(StudentCode)
        Balence.append(Amount)
        fName.append(FirstName)
        sName.append(LastName)
    return Codes, Balence, fName, sName

def getBalence():
    Code = input("\nPlease enter your Student Code:\t")
    for i in range (len(Codes)):
        Position = 0.1
        if Code == Codes[i]:
            Position = int(i)
            break
    if Position == 0.1:
        print("\nINCORRECT!\n")
        x = input("Type 'X' to try again\t")
        if x == 'X':
            getBalence()
        elif x != 'X':
            exit()
    else:
        print("welcome "+fName[Position])
        print("Your current balence is: £"+Balence[Position])
        return Position

def menu(Position):
    Option = input("\nTo TOP-UP your balence, type 'T'\t\tTo PURCHASE an item, type 'P'\t\tTo EXIT an item, type 'X'\nINPUT:\t")
    if Option == 'T':
        TopUp(Position)
    elif Option == 'P':
        PurchaseItem(Position)
    elif Option == 'X':
        return
    else:
        print("INVALID INPUT TRY AGAIN\n")
        menu(Position)
    return

def TopUp(Position):
    print("\nYou Balence is:\t£%.2f" % round(float(Balence[Position]), 2))
    value = input("Top-Up OPTIONS: \n- 10p\n- 20p\n- 50p\n- £1\n- £2\n- £5\n- £10\n- £20\nType 'X' to stop adding/cancel\nI WANT TO ADD:\t")
    if value in TopUpValues:
        if value[0] == "£":
            amount = value[1:]
            print(amount)
            Balence[Position] = float(Balence[Position]) + float(amount)
            NewBalence = ("%.2f" % round(Balence[Position], 2))
            print("Your NEW Balence will be: £" + NewBalence)
            TopUp(Position)
        else:
            amount = "0."+str(value[:2])
            Balence[Position] = float(Balence[Position]) + float(amount)
            NewBalence = ("%.2f" % round(Balence[Position], 2))
            print("Your NEW Balence will be: £"+NewBalence)
            TopUp(Position)
    elif value == 'X':
        print("\nYou NEW Balence will be: £%.2f" % round(float(Balence[Position]), 2))
    else:
        print("INVALID INPUT TRY AGAIN\n")
        TopUp(Position)

def loop(Basket,total,Position):
    print(("\nThe options are:\n\nFOOD\tCOST"))
    for i in range (len(Item)):
        print(str(i)+"."+Item[i]+"\t£"+Cost[i])
    x = input("\nSelect one number at a time OR type 'X' to EXIT: ")
    if x == 'X':
        return Basket, total
    elif x not in FoodValues:
        print("\nINVALID INPUT TRY AGAIN")
        loop(Basket, total, Position)
    order = FoodItems.get(x)
    order = order.split(",")
    price = float(order[1])
    total += price
    Basket.append(order)
    print("\nYour basket is worth","$%.2f" % round(total, 2),"and contains:")
    for j in range (len(Basket)):
        print(Basket[j][0]+" - £"+Basket[j][1])
    if total > float(Balence[Position]):
        print("\nNot enough funds for this transaction!!\n")
        total -= price
        print("Your basket is currently worth","%.2f" % round(total, 2))
        del Basket[-1]
        loop(Basket,total,Position)
        return Basket, total
    loop(Basket,total,Position)
    return Basket, total

def PurchaseItem(Position):
    total = 0
    Basket = []
    b,t= loop(Basket, total,Position)
    Balence[Position] = float(Balence[Position]) - float(t)
    NewBalence = ("%.2f" % round(Balence[Position], 2))
    print("Your Balence IS:\t£" + NewBalence)
    return

FoodItems = {
    "0":"Pizza slice,1.20",
    "1":"Pasta pot,1.50",
    "2":"Main meal,2.80",
    "3":"Panini,1.50",
    "4":"Sandwich,1.70",
    "5":"Premium Sandwich,2.10",
    "6":"Sausage Roll,1.10",
    "7":"Salad,1.60",
    "8":"Dessert,1.00",
    "9":"Jacket potato,1.00"
}

def main_loop():
    Position = getBalence()
    menu(Position)

FoodValues = ["0","1","2","3","4","5","6","7","8","9"]
TopUpValues = ["10p", "20p", "50p", "£1", "£2", "£5", "£10", "£20"]
Item, Cost = getFootData(FoodData)
Codes, Balence, fName, sName = getStudentData(StudentData)
while True:
    main_loop()
StudentData.close()
FoodData.close()