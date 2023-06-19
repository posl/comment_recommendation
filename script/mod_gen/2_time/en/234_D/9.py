def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [x-K for x in P]
    P = [max(0, x) for x in P]
    s = sum(P[:K])
    print(s)
    for i in range(N-K):
        s = s + P[K+i] - P[i]
        print(s)
main()
