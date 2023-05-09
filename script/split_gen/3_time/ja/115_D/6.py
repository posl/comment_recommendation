def solve(n, x):
    if n == 0:
        return 1 if x >= 1 else 0
    layer = 2**(n+2) - 3
    if x <= 1:
        return 0
    elif x == 2:
        return 1
    elif x <= layer:
        return solve(n-1, x-2)
    elif x == layer+1:
        return 2**(n+1) - 3
    elif x <= layer+2:
        return 2**(n+1) - 3 + 1
    elif x <= layer*2:
        return 2**(n+1) - 3 + solve(n-1, x-layer-2)
    else:
        return 2**(n+2) - 3
