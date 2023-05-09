def main():
    n, k = map(int, input().split())
    ans = n % k
    if ans > k:
        ans = k - ans
    print(ans)
