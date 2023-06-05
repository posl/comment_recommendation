def f(k):
    if k % 2 == 0 or k % 5 == 0:
        return -1
    a = 7
    for i in range(1, k + 1):
        if a % k == 0:
            return i
        a = a * 10 + 7
    return -1

if __name__ == '__main__':
    f()