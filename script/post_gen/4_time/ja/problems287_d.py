Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    for i in range(len(s) - len(t) + 1):
        for j in range(len(t)):
            if s[i + j] != t[j] and s[i + j] != '?':
                break
        else:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    t = input()
    ls = len(s)
    lt = len(t)
    for i in range(lt):
        if s[i] == '?':
            continue
        elif s[i] != t[i]:
            print('No')
            exit()
    for i in range(lt,ls):
        if s[i] == '?':
            continue
        elif s[i] != t[i-lt]:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 3

def check(s, t):
    for i in range(len(t)):
        if s[i] != '?' and s[i] != t[i]:
            return False
    return True

=======
Suggestion 4

def solve():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    for i in range(N-M+1):
        for j in range(M):
            if S[i+j] != T[j] and S[i+j] != '?':
                break
        else:
            print('Yes')
            return
    print('No')

=======
Suggestion 5

def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    for i in range(len_s - len_t + 1):
        s_part = s[i:i+len_t]
        match = True
        for j in range(len_t):
            if s_part[j] != t[j] and s_part[j] != '?':
                match = False
                break
        if match:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def main():
    S = input()
    T = input()
    ls = len(S)
    lt = len(T)
    for i in range(lt):
        if S[i] == '?':
            continue
        elif S[i] != T[i]:
            print('No')
            return
    for i in range(lt, ls):
        if S[i] == '?':
            continue
        elif S[i] != T[i-lt]:
            print('No')
            return
    print('Yes')
main()

=======
Suggestion 7

def solve():
    s = input()
    t = input()
    slen = len(s)
    tlen = len(t)
    if slen < tlen:
        print("No")
        return
    for i in range(tlen):
        if s[i] == "?":
            continue
        if s[i] != t[i]:
            print("No")
            return
    for i in range(tlen, slen):
        if s[i] == "?":
            print("Yes")
            return
        if s[i] != t[tlen-1]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 8

def check(s, t, x):
    for i in range(x):
        if s[i] != t[i]:
            return False
    for i in range(len(t) - x):
        if s[-1 - i] != t[-1 - i]:
            return False
    return True

s = input()
t = input()

for i in range(len(t) + 1):
    if check(s, t, i):
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def check(S,T):
    #x=0,1,...,|T| に対して次の問題を解いてください。
    for x in range(len(T)+1):
        #S の先頭の x 文字と末尾の |T|-x 文字を順番を保ったまま連結することで得られる長さ |T| の文字列を S' とする。
        S1 = S[:x]
        S2 = S[-(len(T)-x):]
        S3 = S1 + S2
        #S' と T がマッチするならば Yes と、そうでなければ No と出力せよ。
        if S3 == T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 10

def main():
    s = input()
    t = input()

    # 入力された文字列の長さを取得
    s_len = len(s)
    t_len = len(t)

    # Sの先頭の x 文字と末尾の |T|-x 文字を順番を保ったまま連結することで得られる長さ |T| の文字列を S' とする。
    # S' と T がマッチするならば Yes と、そうでなければ No と出力
    for i in range(t_len + 1):
        if s[:i] + t_len - i == t:
            print('Yes')
        else:
            print('No')
