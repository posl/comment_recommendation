def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(n - k + 1):
        l = x[i]
        r = x[i + k - 1]
        ans = min(ans, min(abs(l), abs(r)) + r - l)
    print(ans)
