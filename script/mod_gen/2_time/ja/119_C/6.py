def main():
    n, a, b, c = map(int, input().split())
    l = [int(input()) for i in range(n)]
    def dfs(i, a, b, c):
        if i == n:
            return abs(a-a) + abs(b-b) + abs(c-c) - 30 if min(a, b, c) > 0 else 10**9
        ret0 = dfs(i+1, a, b, c)
        ret1 = dfs(i+1, a+l[i], b, c) + 10 if a else 10**9
        ret2 = dfs(i+1, a, b+l[i], c) + 10 if b else 10**9
        ret3 = dfs(i+1, a, b, c+l[i]) + 10 if c else 10**9
        return min(ret0, ret1, ret2, ret3)
    print(dfs(0, 0, 0, 0))

if __name__ == '__main__':
    main()