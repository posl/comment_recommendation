def main():
    n, m = map(int, input().split())
    cake = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    for i in range(2 ** 3):
        tmp = 0
        for j in range(n):
            tmp += max([cake[j][k] * (-1) ** ((i >> k) & 1) for k in range(3)])
        ans = max(ans, tmp)
    print(ans)
