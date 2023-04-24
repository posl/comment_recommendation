Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    ans = 0
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    c0 = 0
    c1 = 0
    for i in range(N):
        if i % 2 == 0:
            if S[i] == "0":
                c0 += 1
            else:
                c1 += 1
        else:
            if S[i] == "0":
                c1 += 1
            else:
                c0 += 1
    print(min(c0, c1))

=======
Suggestion 3

def main():
    S = input()
    N = len(S)
    if N == 1:
        print(0)
        return
    cnt = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            cnt += 1
    print((cnt+1) // 2)
    return

=======
Suggestion 4

def main():
    S = input()
    #print(S)
    N = len(S)
    #print(N)
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(S[10])
    #print(S[11])
    #print(S[12])
    #print(S[13])
    #print(S[14])
    #print(S[15])
    #print(S[16])
    #print(S[17])
    #print(S[18])
    #print(S[19])
    #print(S[20])
    #print(S[21])
    #print(S[22])
    #print(S[23])
    #print(S[24])
    #print(S[25])
    #print(S[26])
    #print(S[27])
    #print(S[28])
    #print(S[29])
    #print(S[30])
    #print(S[31])
    #print(S[32])
    #print(S[33])
    #print(S[34])
    #print(S[35])
    #print(S[36])
    #print(S[37])
    #print(S[38])
    #print(S[39])
    #print(S[40])
    #print(S[41])
    #print(S[42])
    #print(S[43])
    #print(S[44])
    #print(S[45])
    #print(S[46])
    #print(S[47])
    #print(S[48])
    #print(S[49])
    #print(S[50])
    #print(S[51])
    #print(S[52])
    #print(S[53])
    #print(S[54])
    #print(S[55])
    #print(S[56])
    #print(S[57])
    #print(S[58])
    #print(S[59])
    #print(S[60])
    #print(S[61])
    #print(S[62])
    #print(S[63])
    #print(S[64])
    #print(S[65])
    #print(S[66])
    #print(S[67])

=======
Suggestion 5

def main():
    # 入力
    S = input()
    # 処理
    N = len(S)
    count = 0
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            count += 1
    # 出力
    print(count)

=======
Suggestion 6

def main():
    S = input()
    N = len(S)
    # 0 と 1 の数をそれぞれカウント
    count_0 = S.count('0')
    count_1 = N - count_0
    # 0 と 1 の数が少ない方を選ぶ
    print(min(count_0, count_1))

=======
Suggestion 7

def main():
    s = input()
    # 0と1の数をカウント
    cnt0 = s.count('0')
    cnt1 = s.count('1')
    # 0と1の数を比較し、少ない方が答え
    if cnt0 < cnt1:
        print(cnt0)
    else:
        print(cnt1)

=======
Suggestion 8

def main():
    S = input()
    N = len(S)
    # 0で塗りつぶした場合の塗り替え回数
    cnt1 = 0
    # 1で塗りつぶした場合の塗り替え回数
    cnt2 = 0
    # 0で塗りつぶした場合の塗り替え回数をカウント
    for i in range(N):
        if i % 2 == 0:
            if S[i] == '1':
                cnt1 += 1
        else:
            if S[i] == '0':
                cnt1 += 1
    # 1で塗りつぶした場合の塗り替え回数をカウント
    for i in range(N):
        if i % 2 == 0:
            if S[i] == '0':
                cnt2 += 1
        else:
            if S[i] == '1':
                cnt2 += 1
    # 0で塗りつぶした場合と1で塗りつぶした場合の塗り替え回数の小さい方を出力
    print(min(cnt1, cnt2))

=======
Suggestion 9

def main():
    s = input()
    s0 = s[0] #初期値
    s1 = s[0] #初期値
    for i in range(1,len(s)):
        if i % 2 == 0:
            if s[i] == s0:
                s0 = '0' if s0 == '1' else '1'
        else:
            if s[i] == s1:
                s1 = '0' if s1 == '1' else '1'
    print(min(s.count(s0),s.count(s1)))

=======
Suggestion 10

def main():
    S = input()
    N = len(S)
    # 0 と 1 の差が最小になるように塗り替える
    # 0 と 1 の差が最小になるように塗り替える
    # 0 と 1 の差が最小になるように塗り替える
    print(min(S.count('0'), S.count('1')))
