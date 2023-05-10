Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    N = len(S)
    Q = S.count("?")
    mod = 10**9 + 7
    ans = 0
    for i, s in enumerate(S):
        if s == "B" or s == "?":
            ans += pow(3, Q, mod) * pow(3, i, mod) * pow(2, N-i-1, mod)
            ans %= mod
        if s == "?":
            Q -= 1
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    l = len(S)
    Q = S.count('?')

    ls = [0] * l
    for i in range(l):
        if S[i] == 'A':
            ls[i] = 1
        elif S[i] == 'B':
            ls[i] = 2
        elif S[i] == 'C':
            ls[i] = 3

    ans = 0
    for i in range(l):
        if ls[i] == 0:
            continue
        elif ls[i] == 1:
            ans += pow(3, Q, 10**9 + 7)
        elif ls[i] == 2:
            ans += pow(3, Q, 10**9 + 7) * pow(2, i, 10**9 + 7)
        elif ls[i] == 3:
            ans += pow(3, Q, 10**9 + 7) * pow(2, i, 10**9 + 7) * pow(2, i, 10**9 + 7)
        ans %= 10**9 + 7

    print(ans)

=======
Suggestion 3

def main():
    S = input()
    Q = S.count('?')
    A = 0
    B = 0
    C = 0
    for i in range(len(S)):
        if S[i] == 'A':
            A += 1
        elif S[i] == 'B':
            B += 1
        elif S[i] == 'C':
            C += 1
    ans = 0
    for i in range(len(S)):
        if S[i] == 'A':
            A -= 1
        elif S[i] == 'B':
            B -= 1
        elif S[i] == 'C':
            C -= 1
        elif S[i] == '?':
            if A == 0:
                ans += pow(3,Q,1000000007) * C
                C -= 1
            elif B == 0:
                ans += pow(3,Q,1000000007) * C
                C -= 1
            elif C == 0:
                ans += pow(3,Q,1000000007) * B
                B -= 1
            else:
                ans += pow(3,Q,1000000007) * (A + B + C)
                A -= 1
                B -= 1
                C -= 1
        ans %= 1000000007
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    Q = S.count('?')
    A = S.count('A')
    B = S.count('B')
    C = S.count('C')
    ans = 0
    for i in range(len(S)):
        if S[i] == 'A':
            A -= 1
        elif S[i] == 'B':
            B -= 1
        elif S[i] == 'C':
            C -= 1
        else:
            ans += A*(pow(3,Q,1000000007) + 3*pow(3,Q-1,1000000007) + 3*pow(3,Q-1,1000000007))
            ans += B*(pow(3,Q,1000000007) + 3*pow(3,Q-1,1000000007))
            ans += C*pow(3,Q,1000000007)
    ans %= 1000000007
    print(ans)

=======
Suggestion 5

def calcABCNum(s):
    #sの中にあるABC数を計算する
    #sの長さが3未満の場合は0を返す
    if len(s) < 3:
        return 0
    #sの先頭の文字がAでない場合は、先頭の文字を削除して再帰呼び出し
    if s[0] != 'A':
        return calcABCNum(s[1:])
    #sの先頭から2文字目の文字がBでない場合は、先頭の文字を削除して再帰呼び出し
    if s[1] != 'B':
        return calcABCNum(s[1:])
    #sの先頭から3文字目の文字がCでない場合は、先頭の文字を削除して再帰呼び出し
    if s[2] != 'C':
        return calcABCNum(s[1:])
    #sの先頭から3文字目までがABCの場合は、先頭の文字を削除して再帰呼び出し
    return 1 + calcABCNum(s[1:])

s = input()
s = s.replace('?', 'A')
print(calcABCNum(s))

=======
Suggestion 6

def main():
    #文字列の入力
    S = input()
    #print(S)
    #文字列の長さ
    length = len(S)
    #print(length)
    #文字列の中にある?の数
    Q = S.count('?')
    #print(Q)
    #ABC数
    ABC = 0
    #?の数が0の場合は、Sの中にABCが何個あるかを調べる
    if Q == 0:
        #print('Q = 0')
        #Sの中にABCが何個あるかを調べる
        for i in range(length-2):
            if S[i] == 'A':
                if S[i+1] == 'B':
                    if S[i+2] == 'C':
                        ABC += 1
        #print(ABC)
        #ABC数を10^9 + 7で割った余りを出力
        print(ABC % (10**9 + 7))
    #?の数が0より大きい場合は、Sの中に?があるところにA,B,Cを入れてABC数を求める
    else:
        #print('Q > 0')
        #?があるところにA,B,Cを入れてABC数を求める
        for i in range(3**Q):
            #print('i = ' + str(i))
            #Sの中に?があるところにA,B,Cを入れる
            for j in range(Q):
                #print('j = ' + str(j))
                #print('i // (3**j) % 3 = ' + str(i // (3**j) % 3))
                S = S.replace('?', 'A', 1)
                S = S.replace('?', 'B', 1)
                S = S.replace('?', 'C', 1)
            #print(S)
            #Sの中にABCが何個あるかを調べる
            for k in range(length-2):
                if S[k] == 'A':
                    if S[k+1] == 'B':
                        if S[k+2]

=======
Suggestion 7

def main():
    s = input()
    ans = 0
    a = 0
    b = 0
    c = 0
    q = 0
    for i in range(len(s)):
        if s[i] == "A":
            a += 1
        elif s[i] == "B":
            b += 1
        elif s[i] == "C":
            c += 1
        elif s[i] == "?":
            q += 1
    for i in range(len(s)):
        if s[i] == "A":
            a -= 1
        elif s[i] == "B":
            b -= 1
        elif s[i] == "C":
            c -= 1
        elif s[i] == "?":
            q -= 1
        if s[i] == "B" or s[i] == "?":
            ans += a * c * pow(3, q, mod)
    print(ans % mod)

=======
Suggestion 8

def main():
    S = input()
    MOD = 10**9 + 7
    n = len(S)
    ans = 0
    a = 0
    b = 0
    c = 0
    for i in range(n):
        if S[i] == 'A':
            a += 1
        elif S[i] == 'B':
            b += 1
        elif S[i] == 'C':
            c += 1
        else:
            ans = (ans + (a * b * c) % MOD) % MOD
            a = (a * 3) % MOD
            b = (b * 3) % MOD
            c = (c * 3) % MOD
    print(ans)

=======
Suggestion 9

def main():
    s = input()
    n = len(s)
    mod = 10 ** 9 + 7
    a = 0
    b = 0
    c = 0
    ans = 0
    for i in range(n):
        if s[i] == "A":
            a += 1
        elif s[i] == "B":
            b += 1
        elif s[i] == "C":
            c += 1
        else:
            ans = (ans * 3 + c) % mod
            c = (c * 3 + b) % mod
            b = (b * 3 + a) % mod
            a = (a * 3 + 1) % mod
    print(ans)

=======
Suggestion 10

def main():
    s = input()
    n = len(s)
    dp = [[0 for _ in range(4)] for _ in range(n+1)]
    dp[0][0] = 1
    mod = 10**9 + 7
    for i in range(n):
        if s[i] == "A":
            dp[i+1][0] += dp[i][0]
            dp[i+1][1] += dp[i][1]
            dp[i+1][2] += dp[i][2]
            dp[i+1][3] += dp[i][3]
        elif s[i] == "B":
            dp[i+1][0] += dp[i][0]
            dp[i+1][1] += dp[i][1]
            dp[i+1][2] += dp[i][2]
            dp[i+1][3] += dp[i][3]
        elif s[i] == "C":
            dp[i+1][0] += dp[i][0]
            dp[i+1][1] += dp[i][1]
            dp[i+1][2] += dp[i][2]
            dp[i+1][3] += dp[i][3]
        else:
            dp[i+1][0] += dp[i][0] * 3
            dp[i+1][1] += dp[i][1] * 3
            dp[i+1][2] += dp[i][2] * 3
            dp[i+1][3] += dp[i][3] * 3
            dp[i+1][1] += dp[i][0]
            dp[i+1][2] += dp[i][1]
            dp[i+1][3] += dp[i][2]
            dp[i+1][0] %= mod
            dp[i+1][1] %= mod
            dp[i+1][2] %= mod
            dp[i+1][3] %= mod
    print(dp[n][3])
