def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    # print(N, K)
    # print(P)
    # print(sorted(P))
    # print(sorted(P)[K-1])
    for i in range(N-K+1):
        print(sorted(P[i:i+K])[K-1])

if __name__ == '__main__':
    solve()