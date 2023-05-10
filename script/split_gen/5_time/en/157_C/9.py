def main():
    N,M = map(int,input().split())
    s_c = [list(map(int,input().split())) for _ in range(M)]
    ans = [-1]*N
    for i in range(M):
        if ans[s_c[i][0]-1] == -1:
            ans[s_c[i][0]-1] = s_c[i][1]
        else:
            if ans[s_c[i][0]-1] != s_c[i][1]:
                print(-1)
                exit()
    if N != 1 and ans[0] == 0:
        print(-1)
        exit()
    if N != 1 and ans[0] == -1:
        ans[0] = 1
    elif N != 1 and ans[0] == -1:
        ans[0] = 0
    for i in range(N):
        if ans[i] == -1:
            ans[i] = 0
    print(*ans,sep="")
main()
