def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        if i == 0:
            ans = len(set(c[i:i+K]))
        else:
            if c[i-1] == c[i+K-1]:
                ans = max(ans, ans)
            else:
                ans = max(ans, len(set(c[i:i+K])))
    print(ans)
