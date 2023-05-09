def main():
    N, M = map(int, input().split())
    S = []
    P = []
    for _ in range(M):
        s = list(map(int, input().split()))
        S.append(s[1:])
        P.append(s[0])
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            c = 0
            for k in S[j]:
                if (i >> (k-1)) & 1:
                    c += 1
            if c % 2 != P[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()