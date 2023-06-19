def main():
    n, m, q = map(int, input().split())
    abcd = []
    for i in range(q):
        abcd.append(list(map(int, input().split())))
    a = [1] * n
    def dfs(i):
        if i == n:
            return
        for j in range(a[i - 1], m + 1):
            a[i] = j
            dfs(i + 1)
            print(a)
    dfs(1)
    print(a)
main()
