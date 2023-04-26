Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    ans = n + m - 2 * dp[n][m]
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    print(m - dp[n][m])

=======
Suggestion 3

def main():
    s = input()
    t = input()
    n = len(t)
    ans = n
    for i in range(len(s)-n+1):
        cnt = 0
        for j in range(n):
            if s[i+j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if t[i] == s[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    print(n+m-2*dp[m][n])

=======
Suggestion 5

def main():
    s = input()
    t = input()
    n = len(t)
    m = len(s)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if s[i]==t[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    print(m-dp[m][n])

=======
Suggestion 6

def main():
    S = input()
    T = input()
    #S = "cabacc"
    #T = "abc"
    #S = "codeforces"
    #T = "atcoder"
    #S = "abcde"
    #T = "ace"
    #S = "atcoder"
    #T = "coder"

    #Sの各文字をTのどこに入れるかを考える
    #Tの各文字をSのどこに入れるかを考える
    #Tの各文字をSのどこに入れるかを考える
    #Tの各文字をSのどこに入れるかを考える
    #Tの各文字をSのどこに入れるかを考える
    #Tの各文字をSのどこに入れるかを考える
    #Tの各文字をSのどこに入れるかを考える
    #Tの各文字をSのどこに入れるかを考える
    #Tの各文字をSのどこに入れるかを考える
    #Tの各文字をSのどこに入れるかを考える
    #Tの各文字をSのどこに入れるかを考える
    #Tの各文字をSのどこに入れるかを考える

    #Sの各文字をTのどこに入れるかを考える
    #Tの各文字をSのどこに入れるかを考える
    #Sの各文字をTのどこに入れるかを考える
    #Tの各文字をSのどこに入れるかを考える
    #Sの各文字をTのどこに入れるかを考える
    #Tの各文字をSのどこに入れるかを考える
    #Sの各文字をTのどこに入れるかを考える
    #Tの各文字をS

=======
Suggestion 7

def main():
    S = input()
    T = input()
    # TがSの部分文字列になるように、Sのいくつかの文字を書き換える
    # 1文字でも書き換える必要がある
    # Tの長さはSの長さ以下
    # S,Tは英小文字のみを含む
    # Sを書き換える文字数の最小値を出力せよ
    # TがSの部分文字列になるように、Sのいくつかの文字を書き換える
    # 1文字でも書き換える必要がある
    # Tの長さはSの長さ以下
    # S,Tは英小文字のみを含む
    # Sを書き換える文字数の最小値を出力せよ
    # TがSの部分文字列になるように、Sのいくつかの文字を書き換える
    # 1文字でも書き換える必要がある
    # Tの長さはSの長さ以下
    # S,Tは英小文字のみを含む
    # Sを書き換える文字数の最小値を出力せよ
    # TがSの部分文字列になるように、Sのいくつかの文字を書き換える
    # 1文字でも書き換える必要がある
    # Tの長さはSの長さ以下
    # S,Tは英小文字のみを含む
    # Sを書き換える文字数の最小値を出力せよ
    # TがSの部分文字列になるように、Sのいくつかの文字を書き換える
    # 1文字でも書き換える必要がある
    # Tの長さ

=======
Suggestion 8

def main():
    S = input()
    T = input()
    S = list(S)
    T = list(T)
    S_len = len(S)
    T_len = len(T)
    ans = 10**9
    for i in range(S_len-T_len+1):
        cnt = 0
        for j in range(T_len):
            if S[i+j] != T[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 9

def main():
    S = input()
    T = input()
    #Sの文字数
    s_len = len(S)
    #Tの文字数
    t_len = len(T)
    #Tの文字数がSの文字数より多い場合は-1を出力
    if s_len < t_len:
        print(-1)
        return
    #Sの文字数がTの文字数より多い場合はSの文字数を出力
    if s_len >= t_len:
        print(s_len)
        return

=======
Suggestion 10

def main():
    S = input()
    T = input()
    #print(S,T)
    #print(len(S),len(T))
    #print(S[0],T[0])
    #print(S[1],T[1])
    #print(S[2],T[2])
    #print(S[3],T[3])
    #print(S[4],T[4])
    #print(S[5],T[5])
    #print(S[6],T[6])
    #print(S[7],T[7])
    #print(S[8],T[8])
    #print(S[9],T[9])
    #print(S[10],T[10])
    #print(S[11],T[11])
    #print(S[12],T[12])
    #print(S[13],T[13])
    #print(S[14],T[14])
    #print(S[15],T[15])
    #print(S[16],T[16])
    #print(S[17],T[17])
    #print(S[18],T[18])
    #print(S[19],T[19])
    #print(S[20],T[20])
    #print(S[21],T[21])
    #print(S[22],T[22])
    #print(S[23],T[23])
    #print(S[24],T[24])
    #print(S[25],T[25])
    #print(S[26],T[26])
    #print(S[27],T[27])
    #print(S[28],T[28])
    #print(S[29],T[29])
    #print(S[30],T[30])
    #print(S[31],T[31])
    #print(S[32],T[32])
    #print(S[33],T[33])
    #print(S[34],T[34])
    #print(S[35],T[35])
    #print(S[36],T[36])
    #print(S[37],T[37])
    #print(S[38],T[38])
    #print(S[39],T[39])
    #print(S[40],T[40])
    #print(S[41],T[41])
    #print(S[42],T[42])
