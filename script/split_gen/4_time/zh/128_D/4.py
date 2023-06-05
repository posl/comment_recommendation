def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(K+1):
        for l in range(i+1):
            r = i - l
            now = V[:l] + V[N-r:]
            now.sort()
            now = sum(now[max(0, len(now)-K):])
            ans = max(ans, now)
    print(ans)
