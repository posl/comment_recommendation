def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for i in range(A)]
    T = [int(input()) for i in range(B)]
    X = [int(input()) for i in range(Q)]
    for x in X:
        s = 0
        t = 0
        while s < A and S[s] < x:
            s += 1
        while t < B and T[t] < x:
            t += 1
        ans = 10**11
        for s1 in [s-1, s]:
            for t1 in [t-1, t]:
                if s1 < 0 or s1 >= A or t1 < 0 or t1 >= B:
                    continue
                d1 = abs(S[s1] - x) + abs(T[t1] - S[s1])
                d2 = abs(T[t1] - x) + abs(S[s1] - T[t1])
                ans = min(ans, d1, d2)
        print(ans)

if __name__ == '__main__':
    main()