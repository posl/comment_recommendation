def f(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    return sum

if __name__ == '__main__':
    f()