# 이 방법은 너무 느림

def square(digits):
    if digits == 0:
        return 1

    returnValue = 1
    for _ in range(0, digits-1):
        returnValue = returnValue * 10

    return returnValue

def seperate(target):
    calcNum = target
    returnValue = 0

    while(True):
        returnValue = calcNum%10 + returnValue
        calcNum = calcNum//10
        if calcNum == 0:
            break

    return returnValue

inputNumber = int(input())
digits = 0
calcNum = inputNumber

while(True):
    calcNum = calcNum//10
    if calcNum == 0:
        break
    digits = digits + 1

startNum = square(digits)

for number in range(startNum, inputNumber+1):
    result = number + seperate(number)
    if result == inputNumber:
        print(number)
        break
    elif number == inputNumber:
        print(0) 

