def fizzbuzz(n):
    a = 0
    for i in range(1, n+1):
        if i % 15 == 0:
            continue
        elif i % 3 == 0:
            continue
        elif i % 5 == 0:
            continue
        else:
            a += i
    return a

if __name__ == '__main__':
    fizzbuzz()