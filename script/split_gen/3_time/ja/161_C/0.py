def main():
    n, k = map(int, input().split())
    ans = n % k
    ans = min(ans, k - ans)
    print(ans)
