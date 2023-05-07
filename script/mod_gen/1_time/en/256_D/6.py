def main():
    N = int(input())
    LR = []
    for i in range(N):
        LR.append(list(map(int, input().split())))
    LR.sort(key=lambda x: x[0])
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

if __name__ == '__main__':
    main()