def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(n - k + 1):
        if x[i] < 0 and x[i + k - 1] < 0:
            ans = min(ans, -x[i])
        elif x[i] < 0 and x[i + k - 1] >= 0:
            ans = min(ans, -x[i] * 2 + x[i + k - 1])
        else:
            ans = min(ans, x[i + k - 1])
    print(ans)
