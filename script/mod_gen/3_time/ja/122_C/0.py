def main():
    N, Q = map(int, input().split())
    S = input()
    l = []
    r = []
    for i in range(Q):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    # ACの数を数える
    ac_count = [0]
    for i in range(N-1):
        if S[i] == 'A' and S[i+1] == 'C':
            ac_count.append(ac_count[i] + 1)
        else:
            ac_count.append(ac_count[i])
    # 累積和を計算する
    ac_cumsum = [0]
    for i in range(N):
        ac_cumsum.append(ac_cumsum[i] + ac_count[i])
    for i in range(Q):
        print(ac_cumsum[r[i]] - ac_cumsum[l[i]-1])

if __name__ == '__main__':
    main()