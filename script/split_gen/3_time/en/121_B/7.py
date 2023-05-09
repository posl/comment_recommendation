def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        if sum([a[i][j] * b[j] for j in range(m)]) + c > 0:
            ans += 1
    print(ans)
