def dfs(a, n, m):
    if len(a) == n:
        print(' '.join(map(str, a)))
        return
    for i in range(1, m+1):
        if not a or a[-1] < i:
            a.append(i)
            dfs(a, n, m)
            a.pop()
n, m = map(int, input().split())
dfs([], n, m)
This is a sample program to print all strictly increasing integer sequences of length N where all elements are between 1 and M (inclusive), in lexicographically ascending order.
