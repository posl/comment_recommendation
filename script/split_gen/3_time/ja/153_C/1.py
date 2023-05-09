def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    ans = 0
    for i in range(N-K):
        ans += H[i]
    print(ans)
