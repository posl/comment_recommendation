def solve(a, b, k):
    if k == 0:
        return 'a' * a + 'b' * b
    elif a == 0:
        return 'b' + 'a' * a + 'b' * b
    elif b == 0:
        return 'a' + 'a' * a + 'b' * b
    elif k <= combi(a + b - 1, a - 1):
        return 'a' + solve(a - 1, b, k)
    else:
        return 'b' + solve(a, b - 1, k - combi(a + b - 1, a - 1))
