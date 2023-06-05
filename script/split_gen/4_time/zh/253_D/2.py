def solve(num, a, b):
    sum = 0
    for i in range(1, num+1):
        if i % a != 0 and i % b != 0:
            sum += i
    return sum
