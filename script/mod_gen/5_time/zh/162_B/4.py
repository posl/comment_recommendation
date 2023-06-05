def fizz_buzz(n):
    s = 0
    for i in range(1, n+1):
        if i % 15 == 0:
            s += 0
        elif i % 3 == 0:
            s += i
        elif i % 5 == 0:
            s += i
        else:
            s += i
    return s

if __name__ == '__main__':
    fizz_buzz()