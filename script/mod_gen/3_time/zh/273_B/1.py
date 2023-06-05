def problem273_b(x, k):
    if k == 0:
        return x
    else:
        return round(x, -k)
x, k = map(int, input().split())
print(problem273_b(x, k))
