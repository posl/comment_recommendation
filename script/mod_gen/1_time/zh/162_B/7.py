def FizzBuzz(n):
    sum = 0
    for i in range(1, n+1):
        if (i % 3 == 0) and (i % 5 == 0):
            sum += 0
        elif i % 3 == 0:
            sum += 0
        elif i % 5 == 0:
            sum += 0
        else:
            sum += i
    return sum
n = int(input())
print(FizzBuzz(n))
