def solution():
    A, B = map(int, input().split())
    if B == 1:
        return 0
    else:
        return (B - 1 + A - 2) // (A - 1)
print(solution())
