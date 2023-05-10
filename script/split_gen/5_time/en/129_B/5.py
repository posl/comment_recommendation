def main():
    n = int(input())
    w = list(map(int, input().split()))
    ans = 10000000000
    for i in range(n):
        ans = min(ans, abs(sum(w[:i+1]) - sum(w[i+1:])))
    print(ans)
