def solve(l):
    if l % 2 == 0:
        return 0
    else:
        return 2**(l//2)
l = int(input())
print(solve(l))
