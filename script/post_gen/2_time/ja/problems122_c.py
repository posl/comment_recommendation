Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    S = input()
    l = []
    r = []
    for i in range(Q):
        l_, r_ = map(int, input().split())
        l.append(l_)
        r.append(r_)

    # print(N, Q)
    # print(S)
    # print(l)
    # print(r)

    # Sの1文字目からi文字目までにACが何個あるかを記録する配列
    S_ac = [0] * (N + 1)

    # Sの1文字目からi文字目までにACが何個あるかを記録する
    for i in range(1, N):
        if S[i - 1] == 'A' and S[i] == 'C':
            S_ac[i + 1] = S_ac[i] + 1
        else:
            S_ac[i + 1] = S_ac[i]

    # print(S_ac)

    # Sのl文字目からr文字目までにACが何個あるかを出力する
    for i in range(Q):
        print(S_ac[r[i]] - S_ac[l[i]])

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    S = input()
    LR = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, Q)
    #print(S)
    #print(LR)
    #print("")

    #ACの数を数える
    count = 0
    for i in range(N-1):
        if S[i:i+2] == "AC":
            count += 1
    #print(count)

    #ACの数を数える
    for i in range(Q):
        l = LR[i][0]
        r = LR[i][1]
        #print(l, r)
        count = 0
        for j in range(l-1, r-1):
            if S[j:j+2] == "AC":
                count += 1
        print(count)

=======
Suggestion 3

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

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    S = input()
    LR = [list(map(int, input().split())) for _ in range(Q)]
    AC = [0] * N
    for i in range(N-1):
        if S[i:i+2] == 'AC':
            AC[i+1] = 1
    AC_sum = [0] * (N+1)
    for i in range(N):
        AC_sum[i+1] = AC_sum[i] + AC[i]
    for l, r in LR:
        print(AC_sum[r-1] - AC_sum[l-1])

=======
Suggestion 5

def main():
    # 入力
    N, Q = map(int, input().split())
    S = input()
    l_r = [list(map(int, input().split())) for _ in range(Q)]

    # 前処理
    # 1文字目から順に、ACが何個現れたかを記録していく
    # 例: S = ACACTACG
    #     ac = [0, 0, 1, 1, 1, 2, 2, 2]
    ac = [0]
    for i in range(1, N):
        if S[i - 1] == "A" and S[i] == "C":
            ac.append(ac[i - 1] + 1)
        else:
            ac.append(ac[i - 1])

    # 出力
    for l, r in l_r:
        print(ac[r - 1] - ac[l - 1])

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    S = input()
    s = [0] * (N+1)
    for i in range(N):
        s[i+1] = s[i] + (S[i:i+2] == 'AC')
    for _ in range(Q):
        l, r = map(int, input().split())
        print(s[r-1] - s[l-1])

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    S = input()
    LR = [list(map(int, input().split())) for _ in range(Q)]

    # 累積和
    # 1文字目からi文字目までにACが何回現れるか
    # AC が現れたら1を加算していく
    # ただし、S[i-1]とS[i]がACでない場合は0を加算
    # 例：ACACTACG
    # 0 1 1 2 2 3 3 3
    # 1文字目から1文字目までにACが何回現れるか
    # AC が現れたら1を加算していく
    # ただし、S[i-1]とS[i]がACでない場合は0を加算
    # 例：ACACTACG
    # 0 0 1 1 2 2 3 3
    # 1文字目から2文字目までにACが何回現れるか
    # AC が現れたら1を加算していく
    # ただし、S[i-1]とS[i]がACでない場合は0を加算
    # 例：ACACTACG
    # 0 0 0 1 1 2 2 3
    # 1文字目から3文字目までにACが何回現れるか
    # AC が現れたら1を加算していく
    # ただし、S[i-1]とS[i]がACでない場合は0を加算
    # 例：ACACTACG
    # 0 0 0 0 1 1 2 2
    # 1文字目から4文字目までにACが何回現れるか
    # AC が現れたら1を加算していく
    # ただし、S[i-1]とS[i]がACでない場

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    S = input()
    LR = [list(map(int, input().split())) for _ in range(Q)]

    # ACを含む部分文字列の数を数える
    # 例：ACACTACG
    # AC: 1
    # ACA: 1
    # ACAC: 1
    # ACACT: 1
    # ACACTA: 1
    # ACACTAC: 2
    # ACACTACG: 2
    # つまり、ACの数を数える
    c = 0
    ac = []
    for s in S:
        if s == 'A':
            c += 1
        elif s == 'C' and c > 0:
            c -= 1
            ac.append(1)
        else:
            c = 0
    ac.append(0)
    ac.append(0)

    # 例：ACACTACG
    # AC: 1
    # ACA: 1
    # ACAC: 1
    # ACACT: 1
    # ACACTA: 1
    # ACACTAC: 2
    # ACACTACG: 2
    # つまり、ACの数を数える
    # ここで足し合わせていく
    # AC: 1
    # ACA: 1
    # ACAC: 1
    # ACACT: 2
    # ACACTA: 3
    # ACACTAC: 5
    # ACACTACG: 7
    for i in range(1, len(ac)):
        ac[i] += ac[i-1]

    # 例：ACACTACG
    # AC: 1
    # ACA: 1
    # ACAC: 1
    # ACACT: 2
    # ACACTA: 3
    # ACACTAC: 5
    # ACACTACG: 7
    # つまり、ACの数を数える
    # ここで足し合わせていく
    # AC: 1
    # ACA

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    S = input()
    #ACの数を数える
    cnt = [0 for i in range(N+1)]
    for i in range(N-1):
        if S[i] + S[i+1] == "AC":
            cnt[i+1] = cnt[i] + 1
        else:
            cnt[i+1] = cnt[i]
    #print(cnt)
    for i in range(Q):
        l, r = map(int, input().split())
        print(cnt[r-1] - cnt[l-1])
