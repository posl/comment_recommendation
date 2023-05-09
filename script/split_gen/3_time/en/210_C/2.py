def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, len(set(c[i:i+K])))
    print(ans)
