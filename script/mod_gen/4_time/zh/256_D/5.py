def solve():
    n = int(input())
    LR = []
    for i in range(n):
        LR.append(list(map(int,input().split())))
    LR.sort(key=lambda x:x[0])
    ans = []
    ans.append(LR[0][0])
    ans.append(LR[0][1])
    for i in range(1,n):
        if LR[i][0] <= ans[-1] and ans[-1] < LR[i][1]:
            ans[-1] = LR[i][1]
        elif LR[i][0] > ans[-1]:
            ans.append(LR[i][0])
            ans.append(LR[i][1])
    for i in range(0,len(ans),2):
        print(ans[i],ans[i+1])

if __name__ == '__main__':
    solve()