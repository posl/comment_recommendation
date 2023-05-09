def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [0] * (N-K+1)
    ans[0] = min(P[:K])
    for i in range(K, N):
        ans[i-K+1] = max(P[i-K+1:i+1])
    print('
'.join(map(str, ans)))

if __name__ == '__main__':
    main()