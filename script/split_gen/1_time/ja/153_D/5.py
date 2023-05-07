def solve(h):
    if h == 1:
        return 1
    else:
        return 1 + 2 * solve(h//2)
h = int(input())
print(solve(h))
