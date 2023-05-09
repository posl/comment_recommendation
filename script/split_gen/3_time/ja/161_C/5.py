def main():
    n,k = map(int, input().split())
    ans = n % k
    ans = min(ans, abs(ans-k))
    print(ans)
