def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    ans = []
    for i in range(N):
        if i == 0:
            l, r = LR[i][0], LR[i][1]
            continue
        if LR[i][0] > r:
            ans.append([l, r])
            l, r = LR[i][0], LR[i][1]
        else:
            r = max(r, LR[i][1])
    ans.append([l, r])
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

if __name__ == '__main__':
    main()