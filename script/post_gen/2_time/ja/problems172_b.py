Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    ans = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    t = input()
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    S = input()
    T = input()
    print(sum(s != t for s, t in zip(S, T)))

=======
Suggestion 5

def main():
    s = input()
    t = input()
    print(sum(si != ti for si, ti in zip(s, t)))

=======
Suggestion 6

def main():
    #入力
    S = input()
    T = input()
    #Sの文字列をリストに分割
    S_list = list(S)
    #Tの文字列をリストに分割
    T_list = list(T)
    #Tの文字列とSの文字列を比較
    count = 0
    for i in range(len(S)):
        if S_list[i] != T_list[i]:
            count += 1
    print(count)
