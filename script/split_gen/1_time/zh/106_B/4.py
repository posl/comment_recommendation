def findDivisor(num):
    divisor = 0
    for i in range(1,int(num**0.5)+1):
        if num % i == 0:
            if num / i == i:
                divisor += 1
            else:
                divisor += 2
    return divisor
