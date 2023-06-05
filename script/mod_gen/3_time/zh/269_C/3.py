def solve(n):
    if n == 0:
        print(0)
        return
    elif n == 1:
        print(0)
        print(1)
        return
    else:
        solve(n-1)
        for i in range(1,n):
            print(n-i)
        solve(n-1)
n = int(input())
solve(n)
