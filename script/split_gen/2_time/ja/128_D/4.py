def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K)+1):
        for j in range(min(N-i, K-i)+1):
            tmp = sorted(V[:i]+V[N-j:])
            tmp = tmp[:K-i-j]
            tmp = sum(tmp)
            ans = max(ans, tmp)
    print(ans)
