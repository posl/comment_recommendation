def dfs(n, m, A):
    if n == 0:
        print(" ".join(map(str, A)))
    else:
        for i in range(1, m + 1):
            if len(A) > 0 and A[-1] > i:
                continue
            A.append(i)
            dfs(n - 1, m, A)
            A.pop()
