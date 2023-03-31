
def convertToNumber(x):
    if x == "I":
        return 1
    elif x == "V":
        return 5
    elif x == "X":
        return 10
    elif x == "L":
        return 50
    elif x == "C":
        return 100
    elif x == "D":
        return 500
    elif x == "M":
        return 1000   
    else:
        return float('inf')


print("Welcome the the Roman Numeral to Decimal conversion Calculator, it goes both ways! Type either a roman numeral or a decimal number smaller then 3999 and hit enter. type quit and hit enter when finished")

while(True):
    print("Please type in your number")
    x = input()
    if(x == "quit"):
        print("quitting...")
        break
    if(x.isnumeric()):
        numberType = "d"
    elif(x.isalpha()):
        x = x.upper()
        numberType = "r"
    else:
        print("make sure you either a roman or decimal number and nothing else")    #bad inputs
        continue
        
    number = x
    if(numberType == "r"):  #do roman to decimal
        total = 0
        letterList = [i for i in number]
        numberList = [convertToNumber(x) for x in letterList]
        if(float('inf') in numberList):
            print("the number is too big")
            continue    
        total += numberList[-1]     #add in the first number and set the prev
        prev = numberList[-1]
        for i in range(len(numberList) - 2, -1, -1):
            if(prev > numberList[i]):   #we have a larger number before 
                total -= numberList[i]  #subtract out this number (IV = 1,5 = 5 -  = 4)
                prev = numberList[i]    #change our prev num
            else:
                total += numberList[i]  #add it on
                prev = numberList[i]    #change our prev num
        if(total > 3900):
            print("the number must be less then 3999")
            continue
        print("The decimal equivalent is: " + str(total))
    elif(numberType == "d"):   #decimal to roman
        number = int(number)
        if(number > 3900):
            print("the number must be less then 3999")
            continue
        total = []
        if(number >= 1000):
            y = number // 1000
            number = number % 1000
            for i in range(y):
                total.append("M")
        if(number >= 100):
            y = number // 900
            number = number % 900
            for i in range(y):
                total.append("CM")
        if(number >= 100):
            y = number // 500
            number = number % 500
            for i in range(y):
                total.append("D")
        if(number >= 100):
            y = number // 400
            number = number % 400
            for i in range(y):
                total.append("CD")
        if(number >= 100):
            y = number // 100
            number = number % 100
            for i in range(y):
                total.append("C")
        if(number >= 10):
            y = number // 90
            number = number % 90
            for i in range(y):
                total.append("XC")
        if(number >= 10):
            y = number // 50
            number = number % 50
            for i in range(y):
                total.append("L")
        if(number >= 10):
            y = number // 40
            number = number % 40
            for i in range(y):
                total.append("XL")
        if(number >= 10):
            y = number // 10
            number = number % 10
            for i in range(y):
                total.append("X")
        if(number >= 1):
            y = number // 9
            number = number % 9
            for i in range(y):
                total.append("IX")
        if(number >= 1):
            y = number // 5
            number = number % 5
            for i in range(y):
                total.append("V")
        if(number >= 1):
            y = number // 4
            number = number % 4
            for i in range(y):
                total.append("IV")
        if(number >= 1):
            y = number // 1
            for i in range(y):
                total.append("I")
        myString = ''.join(total)        
        print("The roman equivalent is: " + myString)
    else:   
        print("make sure you place r or d after your number")   #if the letter is not r or d    


