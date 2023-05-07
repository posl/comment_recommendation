def f(A, B):
    if A % 2 == 0:
        if B % 2 == 0:
            return A ^ B
        else:
            return A ^ B ^ 1
    else:
        if B % 2 == 0:
            return A ^ (B ^ 1)
        else:
            return A ^ (B ^ 1) ^ 1
a, b = map(int, input().split())
print(f(a, b))
