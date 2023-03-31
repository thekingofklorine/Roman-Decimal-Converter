letterToNumberDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def convertToNumber(x):
    if x not in letterToNumberDict.keys():
        return float("inf")
    else:
        return letterToNumberDict.get(x)


def checkInputType(x):
    if x == "quit":
        numberType = "q"
    elif x.isnumeric():
        numberType = "d"
    elif x.isalpha():
        x = x.upper()
        numberType = "r"
    else:  # bad input
        numberType = "z"
    return numberType


def romanToDec(number):
    total = 0
    numberList = [convertToNumber(x) for x in number]
    if float("inf") in numberList:
        print("the number is too big")
        return float("inf")
    total += numberList[-1]  # add in the first number and set the prev
    prev = numberList[-1]
    for i in range(len(numberList) - 2, -1, -1):
        if prev > numberList[i]:  # we have a larger number before
            total -= numberList[i]  # subtract out this number (IV = 1,5 = 5 -  = 4)
            prev = numberList[i]  # change our prev num
        else:
            total += numberList[i]  # add it on
            prev = numberList[i]  # change our prev num
    if total > 3999:
        print("the number must be less then 4000")
        return float("inf")
    return total


def decToRoman(number):
    total = []
    if number >= 1000:
        y = number // 1000
        number = number % 1000
        for _ in range(y):
            total.append("M")
    if number >= 900:
        y = number // 900
        number = number % 900
        for _ in range(y):
            total.append("CM")
    if number >= 500:
        y = number // 500
        number = number % 500
        for _ in range(y):
            total.append("D")
    if number >= 400:
        y = number // 400
        number = number % 400
        for _ in range(y):
            total.append("CD")
    if number >= 100:
        y = number // 100
        number = number % 100
        for _ in range(y):
            total.append("C")
    if number >= 90:
        y = number // 90
        number = number % 90
        for _ in range(y):
            total.append("XC")
    if number >= 50:
        y = number // 50
        number = number % 50
        for _ in range(y):
            total.append("L")
    if number >= 40:
        y = number // 40
        number = number % 40
        for _ in range(y):
            total.append("XL")
    if number >= 10:
        y = number // 10
        number = number % 10
        for _ in range(y):
            total.append("X")
    if number >= 9:
        y = number // 9
        number = number % 9
        for _ in range(y):
            total.append("IX")
    if number >= 5:
        y = number // 5
        number = number % 5
        for _ in range(y):
            total.append("V")
    if number >= 4:
        y = number // 4
        number = number % 4
        for _ in range(y):
            total.append("IV")
    if number >= 1:
        y = number // 1
        for _ in range(y):
            total.append("I")
    return total


print(
    "Welcome the the Roman Numeral to Decimal conversion Calculator, it goes both ways! Type either a roman numeral or a decimal number smaller then 3999 and hit enter. type quit and hit enter when finished"
)
while True:
    print("Please type in your number")
    x = input()
    numberType = checkInputType(x)
    if numberType == "q":
        print("quitting...")
        break
    if numberType == "z":
        print(
            "make sure you either a roman or decimal number and nothing else"
        )  # bad input detected
        continue
    if numberType == "r":  # do roman to decimal
        total = romanToDec(x)
        if total != float("inf"):
            test = decToRoman(total)
            if "".join(test) == x:  # check if x is a legal roman numeral
                print("The decimal equivalent is: " + str(total))
            else:
                print("not a valid roman numeral")
    else:  # decimal to roman
        x = int(x)
        if x > 3999:
            print("the number must be less then 4000")
            continue
        total = decToRoman(x)
        myString = "".join(total)
        print("The roman equivalent is: " + myString)
