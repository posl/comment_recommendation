def solve(n, m):
    if n == 0:
        return
    for i in range(1, m+1):
        if n == 1:
            print(i)
        else:
            for j in solve(n-1, m):
                if i < j[0]:
                    print(i, *j)
