Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    ans = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    cnt0 = 0
    cnt1 = 0
    for i in range(N):
        if i % 2 == 0:
            if S[i] == '0':
                cnt0 += 1
            else:
                cnt1 += 1
        else:
            if S[i] == '0':
                cnt1 += 1
            else:
                cnt0 += 1
    print(min(cnt0, cnt1))

=======
Suggestion 3

def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    prev = S[0]
    ans = 0
    for i in range(1, len(S)):
        if prev == S[i]:
            ans += 1
        else:
            prev = S[i]
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(1,N):
        if S[i] == S[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    S = input()
    N = len(S)
    # 0 と 1 の数を数える
    count_0 = S.count("0")
    count_1 = N - count_0
    # 0 と 1 の数を比較して、少ない方を塗り替える
    print(min(count_0, count_1))

=======
Suggestion 7

def main():
    S = input()
    N = len(S)
    #print("N=", N)
    #print("S=", S)
    #print("S[0]=", S[0])
    #print("S[1]=", S[1])
    #print("S[2]=", S[2])
    #print("S[3]=", S[3])
    #print("S[4]=", S[4])
    #print("S[5]=", S[5])
    #print("S[6]=", S[6])
    #print("S[7]=", S[7])
    #print("S[8]=", S[8])
    #print("S[9]=", S[9])
    #print("S[10]=", S[10])
    #print("S[11]=", S[11])
    #print("S[12]=", S[12])
    #print("S[13]=", S[13])
    #print("S[14]=", S[14])
    #print("S[15]=", S[15])
    #print("S[16]=", S[16])
    #print("S[17]=", S[17])
    #print("S[18]=", S[18])
    #print("S[19]=", S[19])
    #print("S[20]=", S[20])
    #print("S[21]=", S[21])
    #print("S[22]=", S[22])
    #print("S[23]=", S[23])
    #print("S[24]=", S[24])
    #print("S[25]=", S[25])
    #print("S[26]=", S[26])
    #print("S[27]=", S[27])
    #print("S[28]=", S[28])
    #print("S[29]=", S[29])
    #print("S[30]=", S[30])
    #print("S[31]=", S[31])
    #print("S[32]=", S[32])
    #print("S[33]=", S[33])
    #print("S[34]=", S[34])
    #print("S[35]=", S[35])
    #print

=======
Suggestion 8

def main():
    S = input()
    N = len(S)

    # 左から見ていく
    left = 0
    # 右から見ていく
    right = N - 1

    # 左から見ていくときの塗り替え回数
    left_count = 0
    # 右から見ていくときの塗り替え回数
    right_count = 0

    # 左から見ていくときの現在の色
    left_color = S[left]
    # 右から見ていくときの現在の色
    right_color = S[right]

    while left < right:
        # 左から見ていくときの現在の色と右から見ていくときの現在の色が同じ場合
        if left_color == right_color:
            # 左から見ていくときの塗り替え回数が右から見ていくときの塗り替え回数より多い場合
            if left_count > right_count:
                # 右から見ていくときの現在の色を反転させる
                right_color = '0' if right_color == '1' else '1'
                # 右から見ていくときの塗り替え回数をインクリメント
                right_count += 1
            # 左から見ていくときの塗り替え回数が右から見ていくときの塗り替え回数より少ない場合
            else:
                # 左から見ていくときの現在の色を反転させる
                left_color = '0' if left_color == '1' else '1'
                # 左から見ていくときの塗り替え回数をインクリメント
                left_count += 1

        # 左から見ていくときの現在の色と右から見ていくときの現在の色が違う場合

=======
Suggestion 9

def main():
    s = input()
    # 0, 1の連続する部分をカウントする
    cnt = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            cnt += 1

    print((cnt+1)//2)
