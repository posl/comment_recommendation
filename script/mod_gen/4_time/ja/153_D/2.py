def solve(H):
    if H == 1:
        return 1
    else:
        return 1 + 2*solve(H//2)
H = int(input())
print(solve(H))
