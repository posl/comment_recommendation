def main():
    N = int(input())
    LR = []
    for i in range(N):
        L, R = map(int, input().split())
        LR.append([L, R])
    LR.sort()
    ans = []
    ans.append(LR[0])
    for i in range(1, N):
        if ans[-1][1] >= LR[i][0]:
            ans[-1][1] = max(ans[-1][1], LR[i][1])
        else:
            ans.append(LR[i])
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

if __name__ == '__main__':
    main()