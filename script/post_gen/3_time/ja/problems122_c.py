Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    S = input()
    lr = [list(map(int, input().split())) for i in range(Q)]
    #print(N, Q)
    #print(S)
    #print(lr)
    #ACの個数を数える
    ac = [0] * (N + 1)
    for i in range(N):
        if S[i:i+2] == "AC":
            ac[i+1] = ac[i] + 1
        else:
            ac[i+1] = ac[i]
    for i in range(Q):
        print(ac[lr[i][1]-1] - ac[lr[i][0]-1])

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * (N + 1)
    for i in range(N - 1):
        if S[i] == "A" and S[i + 1] == "C":
            l[i + 2] = l[i + 1] + 1
        else:
            l[i + 2] = l[i + 1]
    for _ in range(Q):
        x, y = map(int, input().split())
        print(l[y] - l[x])

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * N
    for i in range(N - 1):
        if S[i:i + 2] == "AC":
            l[i + 1] = l[i] + 1
        else:
            l[i + 1] = l[i]
    for i in range(Q):
        li, ri = map(int, input().split())
        print(l[ri - 1] - l[li - 1])

=======
Suggestion 5

def main():
    n, q = map(int, input().split())
    s = input()
    l = [0] * n
    for i in range(1, n):
        if s[i-1:i+1] == 'AC':
            l[i] = l[i-1] + 1
        else:
            l[i] = l[i-1]
    for _ in range(q):
        a, b = map(int, input().split())
        print(l[b-1] - l[a-1])

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    S = input()
    LR = [list(map(int, input().split())) for _ in range(Q)]

    #ACの出現回数を数える
    AC_count = 0
    AC_list = [0] * N
    for i in range(N-1):
        if S[i:i+2] == "AC":
            AC_count += 1
        AC_list[i+1] = AC_count

    #出力
    for l, r in LR:
        print(AC_list[r-1] - AC_list[l-1])

=======
Suggestion 7

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

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    S = input()
    LR = [list(map(int, input().split())) for _ in range(Q)]

    # 1. 入力を受け取る
    # 2. Sの各文字を順番に見ていって、ACとなる文字列の数を数える
    # 3. 累積和をとっておく
    # 4. LRの各値で累積和をとる
    # 5. 累積和の差分をとる

    # 2. Sの各文字を順番に見ていって、ACとなる文字列の数を数える
    # 3. 累積和をとっておく
    # 4. LRの各値で累積和をとる
    # 5. 累積和の差分をとる
    # 2. Sの各文字を順番に見ていって、ACとなる文字列の数を数える
    # 3. 累積和をとっておく
    # 4. LRの各値で累積和をとる
    # 5. 累積和の差分をとる

    # 2. Sの各文字を順番に見ていって、ACとなる文字列の数を数える
    # 3. 累積和をとっておく
    # 4. LRの各値で累積和をとる
    # 5. 累積和の差分をとる

    # 2. Sの各文字を順番に見ていって、ACとなる文字列の数を数える
    # 3. 累積和をとっておく
    # 4. LRの各値で累積和をとる
    # 5. 累積和の差分をと

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    S = input()
    #print(N, Q, S)
    #print(len(S))
    #print(S[0])
    #print(S[0:1])
    #print(S[0:2])
    #print(S[0:3])
    #print(S[0:4])
    #print(S[0:5])
    #print(S[0:6])
    #print(S[0:7])
    #print(S[0:8])
    #print(S[0:9])

    #print(S[1:2])
    #print(S[1:3])
    #print(S[1:4])
    #print(S[1:5])
    #print(S[1:6])
    #print(S[1:7])
    #print(S[1:8])
    #print(S[1:9])

    #print(S[2:3])
    #print(S[2:4])
    #print(S[2:5])
    #print(S[2:6])
    #print(S[2:7])
    #print(S[2:8])
    #print(S[2:9])

    #print(S[3:4])
    #print(S[3:5])
    #print(S[3:6])
    #print(S[3:7])
    #print(S[3:8])
    #print(S[3:9])

    #print(S[4:5])
    #print(S[4:6])
    #print(S[4:7])
    #print(S[4:8])
    #print(S[4:9])

    #print(S[5:6])
    #print(S[5:7])
    #print(S[5:8])
    #print(S[5:9])

    #print(S[6:7])
    #print(S[6:8])
    #print(S[6:9])

    #print(S[7:8])
    #print(S[7:9])

    #print(S[8:9])

    #print(S[0:1])
    #print(S[1:2])
    #print(S[2:3])
    #print(S[3:4])
    #print(S[4:5])
    #print(S[5:6])
