def solve(r1, c1, r2, c2):
    if r1 == r2 and c1 == c2:
        return 0
    elif abs(r1 - r2) + abs(c1 - c2) <= 3:
        return 1
    elif (r1 + c1) % 2 == (r2 + c2) % 2:
        return 2
    elif abs((r1 + c1) - (r2 + c2)) <= 3:
        return 2
    elif abs((r1 - c1) - (r2 - c2)) <= 3:
        return 2
    else:
        return 3
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
print(solve(r1, c1, r2, c2))
