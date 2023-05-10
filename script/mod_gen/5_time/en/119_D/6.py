def main():
    [A, B, Q] = [int(x) for x in input().rstrip().split()]
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    for x in X:
        sl = 0
        sr = 0
        tl = 0
        tr = 0
        while sl < A and S[sl] < x:
            sl += 1
        if sl > 0:
            sr = sl - 1
        else:
            sr = sl
        while tl < B and T[tl] < x:
            tl += 1
        if tl > 0:
            tr = tl - 1
        else:
            tr = tl
        ans = 10 ** 10
        for s in [S[sr], S[sl]]:
            for t in [T[tr], T[tl]]:
                ans = min(ans, abs(s - x) + abs(t - s))
                ans = min(ans, abs(t - x) + abs(s - t))
        print(ans)
main()

if __name__ == '__main__':
    main()