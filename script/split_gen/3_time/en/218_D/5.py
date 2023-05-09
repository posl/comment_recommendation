def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x = sorted(x)
    y = sorted(y)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += (j - i) * (N - j) * (j - i - 1) * (N - j - 1)
    print(ans // 4)
