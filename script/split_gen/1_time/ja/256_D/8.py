def main():
    N = int(input())
    LR = [list(map(int,input().split())) for i in range(N)]
    LR.sort(key=lambda x:x[0])
    ans = []
    l,r = LR[0]
    for i in range(1,N):
        if r >= LR[i][0]:
            r = max(r,LR[i][1])
        else:
            ans.append([l,r])
            l,r = LR[i]
    ans.append([l,r])
    for a in ans:
        print(*a)
