def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 1
    if (n-1)%(k-1) != 0:
        ans += 1
    ans += (n-1)//(k-1)
    print(ans)
