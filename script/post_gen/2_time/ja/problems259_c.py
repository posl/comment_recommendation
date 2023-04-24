Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    if N > M:
        print('No')
        return
    i = 0
    j = 0
    while i < N and j < M:
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == N:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if len(S) == len(T):
        if S == T:
            print("Yes")
        else:
            print("No")
    else:
        for i in range(len(S)):
            if S[i] == T[i]:
                continue
            else:
                if S[i] == T[i+1] and S[i+1] == T[i]:
                    print("Yes")
                    break
                else:
                    print("No")
                    break

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if len(S) > len(T):
        print("No")
        return
    i = 0
    j = 0
    while i < len(S) and j < len(T):
        if S[i] == T[j]:
            i += 1
        j += 1
    if i == len(S):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            count += 1
    if count == len(s):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    S = list(input())
    T = list(input())
    if S == T:
        print("Yes")
        return
    if len(S) > len(T):
        print("No")
        return
    for i in range(len(S)):
        if S[i] != T[i]:
            if S[i] == T[i+1] and S[i+1] == T[i]:
                S[i], S[i+1] = S[i+1], S[i]
                if S == T:
                    print("Yes")
                    return
                else:
                    print("No")
                    return
            else:
                print("No")
                return
    print("Yes")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    
    if s == t:
        print("Yes")
        return
    
    if len(s) > len(t):
        print("No")
        return
    
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i] == t[i+1] and s[i+1] == t[i+2]:
                print("Yes")
                return
            else:
                print("No")
                return
    
    print("Yes")

=======
Suggestion 7

def main():
    S = input()
    T = input()

    # Sの文字列の長さ
    len_s = len(S)
    # Tの文字列の長さ
    len_t = len(T)

    # Sの文字列の長さがTの文字列の長さよりも大きい場合はNoを出力
    if len_s > len_t:
        print("No")
        return

    # Sの文字列の長さがTの文字列の長さよりも小さい場合
    # Sの文字列の長さ分ループを回し、Sの文字列とTの文字列を比較
    # Sの文字列とTの文字列が一致している場合は、Sの文字列の長さを1増やす
    # Sの文字列とTの文字列が一致していない場合は、Sの文字列の長さを1減らす
    # Sの文字列の長さがTの文字列の長さになった場合は、Yesを出力
    # Sの文字列の長さがTの文字列の長さにならなかった場合は、Noを出力
    for i in range(len_t):
        if S == T[i:i+len_s]:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def main():
    S = input()
    T = input()
    N = len(T)
    M = len(S)
    #print(N,M)
    i = 0
    j = 0
    while i < N and j < M:
        if T[i] == S[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == M:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    S = input()
    T = input()
    #Tの数をカウントする
    t_count = {}
    for t in T:
        t_count[t] = t_count.get(t, 0) + 1
    #Tの数をカウントする
    s_count = {}
    for s in S:
        s_count[s] = s_count.get(s, 0) + 1
    #Tの数をカウントする
    for t in t_count:
        #SにTの文字がない場合
        if not t in s_count:
            print("No")
            return
        #SにTの文字がある場合
        else:
            #Sの文字の数がTの文字の数以上でない場合
            if s_count[t] < t_count[t]:
                print("No")
                return
    #Sの文字の数がTの文字の数以上の場合
    print("Yes")

=======
Suggestion 10

def main():
    S = input()
    T = input()

    #Tを一文字ずつ見ていく
    #Tの文字数分だけ回す
    for i in range(len(T)):
        #Tのi文字目とSのi文字目が違う場合
        if T[i] != S[i]:
            #Tのi文字目がSのi+1文字目と一致する場合
            if T[i] == S[i+1]:
                #Tのi文字目とSのi+1文字目を入れ替える
                S = S[:i+1] + T[i] + S[i+1:]
            #違う場合
            else:
                #Noを出力して終了
                print("No")
                return
    #Yesを出力して終了
    print("Yes")
