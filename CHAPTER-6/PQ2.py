def factorialOfNum(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    return fact

factorialOfNum(5)


#USD TO INR

def CurrencyConverter(amount):
    convert = amount * 94.8
    print(convert)
    return convert


CurrencyConverter(5)