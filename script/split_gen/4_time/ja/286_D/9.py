def check_payment(n, x, a, b):
    if n == 1:
        if x % a[0] == 0 and x / a[0] <= b[0]:
            return True
        else:
            return False
    else:
        for i in range(b[0]+1):
            if x - a[0] * i < 0:
                break
            elif x - a[0] * i == 0:
                return True
            else:
                if check_payment(n-1, x - a[0] * i, a[1:], b[1:]):
                    return True
        return False
n, x = map(int, input().split())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
