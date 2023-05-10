def main():
    n, m = map(int, input().split())
    a_b = [list(map(int, input().split())) for _ in range(n)]
    a_b.sort()
    ans = 0
    for i in range(n):
        if m <= a_b[i][1]:
            ans += a_b[i][0] * m
            break
        else:
            ans += a_b[i][0] * a_b[i][1]
            m -= a_b[i][1]
    print(ans)
