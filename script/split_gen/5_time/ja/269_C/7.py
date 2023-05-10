def solve():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = []
    for i in range(1, 60):
        if n & (1 << i):
            ans.append(i)
    ans.append(0)
    ans.sort()
    for i in ans:
        print(1 << i)
