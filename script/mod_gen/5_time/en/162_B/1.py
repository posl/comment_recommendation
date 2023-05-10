def fizzbuzz(n):
    sum = 0
    for i in range(1, n+1):
        if i % 15 == 0:
            continue
        elif i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

if __name__ == '__main__':
    fizzbuzz()