def solve(n, m, a, b):
    if m > n:
        return False
    if m == 1:
        if b[0] in a:
            return True
        else:
            return False
    else:
        for i in range(n):
            for j in range(m):
                if a[i] == b[j]:
                    return True
        return False
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
