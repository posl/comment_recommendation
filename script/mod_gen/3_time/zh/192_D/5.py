def solve(x,m):
    if len(x) == 1:
        if int(x) <= m:
            return 1
        else:
            return 0
    d = max([int(i) for i in x])
    res = 0
    for i in range(d+1, 11):
        res += solve(x,i,m)
    return res
x = input()
m = int(input())
print(solve(x,m))
