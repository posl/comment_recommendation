def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    LR.sort(key=lambda x: x[1])
    ans = []
    l = 0
    r = 0
    for i in range(N):
        if r < LR[i][0]:
            ans.append([l, r])
            l = LR[i][0]
            r = LR[i][1]
        else:
            r = max(r, LR[i][1])
    ans.append([l, r])
    ans.pop(0)
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
