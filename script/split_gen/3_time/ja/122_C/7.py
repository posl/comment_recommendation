def main():
    # 1行目を取得
    nq = input().split()
    n = int(nq[0])
    q = int(nq[1])
    # 2行目を取得
    s = input()
    # 3行目以降を取得
    lr = [list(map(int, input().split())) for i in range(q)]
    # 3行目以降を取得
    #lr = [list(map(int, input().split())) for i in range(q)]
    #print(nq)
    #print(n)
    #print(q)
    #print(s)
    #print(lr)
    
    # 累積和のリストを作成
    ac_list = [0] * (n+1)
    for i in range(n-1):
        if s[i] == 'A' and s[i+1] == 'C':
            ac_list[i+2] = ac_list[i+1] + 1
        else:
            ac_list[i+2] = ac_list[i+1]
    #print(ac_list)
    
    # 各問に対してACの数を出力
    for i in range(q):
        print(ac_list[lr[i][1]] - ac_list[lr[i][0]])
