def main():
    N,M = map(int,input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            flag = True
            for k in range(M):
                if S[i][k] == "o" or S[j][k] == "o":
                    pass
                else:
                    flag = False
            if flag:
                ans += 1
    print(ans)
main()
