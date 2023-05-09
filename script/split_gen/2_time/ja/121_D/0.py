def f(x):
    if x % 2 == 0:
        if x % 4 == 0:
            return x
        else:
            return 1 ^ x
    else:
        if (x+1) % 4 == 0:
            return 0
        else:
            return 1
A, B = map(int, input().split())
print(f(B) ^ f(A-1))
