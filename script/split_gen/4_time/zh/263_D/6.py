def solve(a, l, r):
    n = len(a)
    if n == 1:
        return a[0]
    elif n == 2:
        return min(a[0] * l + a[1] * r, (a[0] + a[1]) * l)
    else:
        return min(a[0] * l + a[1] * r + sum(a[2:]) * r, (a[0] + a[1]) * l + sum(a[2:]) * r, a[0] * l + (a[1] + sum(a[2:])) * r, (a[0] + a[1]) * l + (sum(a[2:])) * r, a[0] * l + a[1] * r + sum(a[2:]) * l, (a[0] + a[1]) * l + sum(a[2:]) * l, a[0] * l + (a[1] + sum(a[2:])) * l, (a[0] + a[1]) * l + (sum(a[2:])) * l)
n, l, r = map(int, input().split())
a = list(map(int, input().split()))
print(solve(a, l, r))
