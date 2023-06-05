def main():
    n, k = map(int, input().split())
    ans = 0
    for a in range(1, n+1):
        if a % k == 0:
            ans += n // k
        elif k % 2 == 0 and a % (k // 2) == k // 2:
            ans += (n - k // 2) // k + 1
    print(ans)
