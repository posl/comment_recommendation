def main():
    N = int(input())
    LR = [list(map(int, input().split())) for i in range(N)]
    LR.sort()
    ans = []
    ans.append(LR[0])
    for i in range(1, N):
        if ans[-1][1] >= LR[i][1]:
            continue
        elif ans[-1][1] >= LR[i][0]:
            ans[-1][1] = LR[i][1]
        else:
            ans.append(LR[i])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
