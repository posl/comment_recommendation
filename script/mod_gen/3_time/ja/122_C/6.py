def main():
    #入力
    N, Q = map(int, input().split())
    S = input()
    l_r = [list(map(int, input().split())) for _ in range(Q)]
    #ACの数を数える
    ac_cnt = 0
    ac_list = []
    for i in range(N-1):
        if S[i] == "A" and S[i+1] == "C":
            ac_cnt += 1
        ac_list.append(ac_cnt)
    #出力
    for l, r in l_r:
        print(ac_list[r-1] - ac_list[l-1])

if __name__ == '__main__':
    main()