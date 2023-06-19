def f(i, j):
    if i == 0 and j == 0:
        return 1
    elif i == 0 or j < 3:
        return 0
    else:
        return f(i-1, j) + f(i, j-1)
S = int(input())
print(f(S, S) % 1000000007)
