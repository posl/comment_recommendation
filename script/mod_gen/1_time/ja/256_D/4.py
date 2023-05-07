def main():
    N = int(input())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    LR = list(zip(L, R))
    LR.sort(key=lambda x: x[0])
    ans = []
    ans.append(LR[0])
    for i in range(1, N):
        if ans[-1][1] < LR[i][0]:
            ans.append(LR[i])
        else:
            ans[-1] = (ans[-1][0], max(ans[-1][1], LR[i][1]))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])

if __name__ == '__main__':
    main()