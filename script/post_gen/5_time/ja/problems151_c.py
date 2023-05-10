Synthesizing 10/10 solutions

=======
Suggestion 1

def problems151_c():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        pi, si = input().split()
        pi = int(pi)
        if s[pi - 1] == 0:
            if si == "AC":
                p[pi - 1] += 1
            else:
                s[pi - 1] += 1
        else:
            continue
    print(sum(p), sum(s))

=======
Suggestion 2

def calc_penalty(penalty_list):
    penalty = 0
    for i in range(len(penalty_list)):
        penalty += penalty_list[i]
    return penalty

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    ac = [False] * n
    wa = [0] * n
    ac_count = 0
    wa_count = 0
    for i in range(m):
        p, s = input().split()
        p = int(p) - 1
        if ac[p]:
            continue
        if s == "AC":
            ac[p] = True
            ac_count += 1
            wa_count += wa[p]
        else:
            wa[p] += 1
    print(ac_count, wa_count)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for i in range(m):
        p_, s_ = input().split()
        p_ = int(p_) - 1
        p[p_] += 1
        s[p_] = s_
    ac = 0
    wa = 0
    for i in range(n):
        if p[i] == 0:
            continue
        if s[i] == 'AC':
            ac += 1
            wa += p[i] - 1
    print(ac, wa)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    p = [0] * n
    s = [0] * n
    for _ in range(m):
        pi, si = input().split()
        pi = int(pi) - 1
        if s[pi] == 0 and si == 'AC':
            s[pi] = 1
        elif s[pi] == 0 and si == 'WA':
            p[pi] += 1

    print(sum(s), sum([p[i] * s[i] for i in range(n)]))

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    p = [0] * (n + 1)
    s = [0] * (n + 1)
    for i in range(m):
        x, y = input().split()
        x = int(x)
        if s[x] == 0:
            s[x] = y
            if s[x] == "AC":
                p[x] = 1
            else:
                p[x] = 0
    print(sum(p), s.count("WA") - sum(p))

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())

    # 問題数分のACフラグを作成
    # 問題番号とACフラグのインデックスは-1する
    # False: ACを出していない
    # True: ACを出している
    ac_flag_list = [False] * N

    # 問題数分のWAフラグを作成
    # 問題番号とWAフラグのインデックスは-1する
    # 0: ACを出していない
    # 1以上: ACを出すまでのWA数
    wa_flag_list = [0] * N

    # WA数
    wa_count = 0

    # AC数
    ac_count = 0

    # M回の入力
    for i in range(M):
        p, s = input().split()

        # 問題番号(インデックス)は-1する
        p = int(p) - 1

        # ACの場合
        if s == 'AC':
            # まだACを出していない場合
            if ac_flag_list[p] == False:
                # ACフラグを立てる
                ac_flag_list[p] = True
                # AC数をカウントする
                ac_count += 1
                # その問題のWA数をカウントする
                wa_count += wa_flag_list[p]
        # WAの場合
        else:
            # まだACを出していない場合
            if ac_flag_list[p] == False:
                # その問題のWA数をカウントする
                wa_flag_list[p] += 1

    # 結果を出力する
    print(ac_count, wa_count)

=======
Suggestion 8

def main():
    n,m=map(int,input().split())
    p=[0]*n
    s=[0]*n
    for i in range(m):
        a,b=input().split()
        a=int(a)
        if s[a-1]=='AC':
            continue
        if b=='AC':
            p[a-1]+=1
            s[a-1]='AC'
        else:
            p[a-1]+=1
    print(sum(p),s.count('AC'))
main()

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    p = [0] * N
    s = [0] * N
    for i in range(M):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
    ac = [0] * N
    wa = [0] * N
    for i in range(M):
        if s[i] == "AC":
            ac[p[i] - 1] = 1
        elif s[i] == "WA" and ac[p[i] - 1] == 0:
            wa[p[i] - 1] += 1
    ac_cnt = 0
    wa_cnt = 0
    for i in range(N):
        if ac[i] == 1:
            ac_cnt += 1
            wa_cnt += wa[i]
    print(ac_cnt, wa_cnt)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    ac = [False] * n
    wa = [0] * n
    for i in range(m):
        p, s = input().split()
        p = int(p) - 1
        if ac[p]:
            continue
        if s == 'AC':
            ac[p] = True
        else:
            wa[p] += 1
    print(sum(ac), sum([w if ac[i] else 0 for i, w in enumerate(wa)]))
