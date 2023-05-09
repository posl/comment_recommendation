def main():
    n, m = map(int, input().split())
    cake = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(2**3):
        tmp = 0
        for j in range(n):
            sum = 0
            for k in range(3):
                if i >> k & 1:
                    sum += cake[j][k]
                else:
                    sum -= cake[j][k]
            tmp += abs(sum)
        ans = max(ans, tmp)
    print(ans)
