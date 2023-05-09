def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    S.append(10**20)
    S.append(-10**20)
    T.append(10**20)
    T.append(-10**20)
    S.sort()
    T.sort()
    for x in X:
        s = S[bisect.bisect_left(S, x)]
        t = T[bisect.bisect_left(T, x)]
        ans = 10**20
        for si in [s-1, s]:
            for ti in [t-1, t]:
                ans = min(ans, abs(x-si)+abs(si-ti), abs(x-ti)+abs(si-ti))
        print(ans)

if __name__ == '__main__':
    main()