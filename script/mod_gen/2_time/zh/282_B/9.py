def main():
    N,M = map(int, input().split())
    S = []
    for i in range(N):
        S.append(list(input()))
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            flag = True
            for k in range(M):
                if S[i][k] == 'x' and S[j][k] == 'x':
                    flag = False
                    break
            if flag:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()