def f(a, b, k):
    if a == 0:
        return 'b' * b
    elif b == 0:
        return 'a' * a
    elif k <= 1:
        return 'a' * a + 'b' * b
    elif k <= a * b:
        return 'a' * (k // b) + 'b' * (k % b)
    else:
        return 'b' + f(a - 1, b, k - b)

if __name__ == '__main__':
    f()