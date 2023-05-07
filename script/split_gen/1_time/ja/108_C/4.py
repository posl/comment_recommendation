def main():
    n,k = map(int,input().split())
    ans = 0
    if k % 2 == 0:
        ans += ((n - k // 2) // k + 1) ** 3
        ans += ((n - k) // k + 1) ** 3
    else:
        ans += (n // k + 1) ** 3
    print(ans)
