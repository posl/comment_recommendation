def main():
    N = int(input())
    LR = [list(map(int,input().split())) for i in range(N)]
    LR.sort(key=lambda x:x[0])
    ans = []
    ans.append(LR[0])
    for i in range(1,N):
        if ans[-1][1] < LR[i][0]:
            ans.append(LR[i])
        elif ans[-1][1] < LR[i][1]:
            ans[-1][1] = LR[i][1]
    for i in range(len(ans)):
        print(*ans[i])
