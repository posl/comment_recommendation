def main():
    N, K = map(int, input().split())
    ans = 0
    while N > 0:
        ans += 1
        N //= K
    print(ans)
