def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n-k+1):
        ans = max(ans, sum(p[i:i+k]))
    print(ans)
