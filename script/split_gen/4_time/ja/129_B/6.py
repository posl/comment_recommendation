def main():
    n = int(input())
    w = list(map(int, input().split()))
    ans = 1000000000000
    for i in range(n-1):
        ans = min(ans, abs(sum(w[:i+1]) - sum(w[i+1:])))
    print(ans)
