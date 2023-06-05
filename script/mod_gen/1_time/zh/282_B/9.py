def main():
    N, M = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ok = True
            for k in range(M):
                if S[i][k] == 'x' and S[j][k] == 'x':
                    ok = False
            if ok:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()