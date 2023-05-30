def solve():
    N = int(input())
    if N % 2 == 0:
        return N // 2
    else:
        return N // 2 + 1
print(solve())
