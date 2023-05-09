def main():
    N, Q = map(int, input().split())
    S = input()
    LR = [list(map(int, input().split())) for _ in range(Q)]
    #累積和
    #ACを数える
    #ACの数を格納するリスト
    ac = [0] * (N + 1)
    for i in range(1, N):
        if S[i - 1] == "A" and S[i] == "C":
            ac[i] = ac[i - 1] + 1
        else:
            ac[i] = ac[i - 1]
    #問題を解く
    for l, r in LR:
        print(ac[r - 1] - ac[l - 1])

if __name__ == '__main__':
    main()