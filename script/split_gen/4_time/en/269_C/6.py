def solve(n):
    if n == 0:
        print(0)
        return
    print(0)
    for i in range(1, 60):
        if n & (1 << i):
            print(1 << i)
    print(n)
n = int(input())
solve(n)
