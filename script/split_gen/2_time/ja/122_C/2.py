def main():
    # 入力
    N, Q = map(int, input().split())
    S = input()
    l = []
    r = []
    for i in range(Q):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    # 累積和
    ac = [0] * (N + 1)
    for i in range(N):
        if S[i] == 'A' and S[i + 1] == 'C':
            ac[i + 1] = ac[i] + 1
        else:
            ac[i + 1] = ac[i]
    # 出力
    for i in range(Q):
        print(ac[r[i] - 1] - ac[l[i] - 1])
