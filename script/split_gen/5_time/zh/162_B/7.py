def FizzBuzz(N):
    sum = 0
    for i in range(1, N+1):
        if i%3 == 0 and i%5 == 0:
            sum += i
        elif i%3 == 0:
            sum += i
        elif i%5 == 0:
            sum += i
    return sum
