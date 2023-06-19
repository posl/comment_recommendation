def countDivisors(num):
    count = 0
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            count += 2
    return count
