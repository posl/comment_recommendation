def solve():
    N = input()
    if len(N) == 2:
        return int(N[0]) * int(N[1])
    else:
        def dfs(i, a, b):
            if i == len(N):
                return a * b
            if N[i] == '0':
                return dfs(i + 1, a * 10, b)
            else:
                return max(dfs(i + 1, a * 10 + int(N[i]), b), dfs(i + 1, a, b * 10 + int(N[i])))
        return dfs(0, 0, 0)
print(solve())

if __name__ == '__main__':
    solve()