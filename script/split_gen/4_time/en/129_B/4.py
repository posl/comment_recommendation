def main():
    n = int(input())
    w = list(map(int, input().split()))
    ans = 100000
    for i in range(n):
        ans = min(ans, abs(sum(w[:i]) - sum(w[i:])))
    print(ans)
