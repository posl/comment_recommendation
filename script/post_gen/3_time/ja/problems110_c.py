Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        if s[i] in s_dict:
            s_dict[s[i]].append(i)
        else:
            s_dict[s[i]] = [i]
        if t[i] in t_dict:
            t_dict[t[i]].append(i)
        else:
            t_dict[t[i]] = [i]
    if sorted(s_dict.values()) == sorted(t_dict.values()):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    s2t = {}
    t2s = {}
    for s, t in zip(S, T):
        if s in s2t and s2t[s] != t:
            print("No")
            return
        if t in t2s and t2s[t] != s:
            print("No")
            return
        s2t[s] = t
        t2s[t] = s
    print("Yes")

=======
Suggestion 3

def main():
    S = input()
    T = input()
    S = list(S)
    T = list(T)
    S.sort()
    T.sort(reverse=True)
    if S < T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    S_list = list(S)
    T_list = list(T)
    S_list.sort()
    T_list.sort(reverse=True)
    if S_list < T_list:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    if s_len != t_len:
        print("No")
        return
    s_dict = {}
    t_dict = {}
    for i in range(s_len):
        s_char = s[i]
        t_char = t[i]
        if s_char in s_dict:
            if s_dict[s_char] != t_char:
                print("No")
                return
        else:
            s_dict[s_char] = t_char
        if t_char in t_dict:
            if t_dict[t_char] != s_char:
                print("No")
                return
        else:
            t_dict[t_char] = s_char
    print("Yes")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if len(set(s)) == len(set(t)) == 26:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    S = input()
    T = input()
    S = S.lower()
    T = T.lower()

    S_list = list(S)
    T_list = list(T)

    S_list.sort()
    T_list.sort()

    if S_list == T_list:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    S = input()
    T = input()

    # 文字列をソートしたものを比較
    S_sort = sorted(S)
    T_sort = sorted(T)
    if S_sort == T_sort:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    S = input()
    T = input()
    #Sの文字をTの文字に変換する辞書を作成
    S_to_T = {}
    T_to_S = {}
    for i in range(len(S)):
        if S[i] in S_to_T:
            if S_to_T[S[i]] != T[i]:
                print("No")
                return
        else:
            S_to_T[S[i]] = T[i]
        if T[i] in T_to_S:
            if T_to_S[T[i]] != S[i]:
                print("No")
                return
        else:
            T_to_S[T[i]] = S[i]
    print("Yes")
    return

=======
Suggestion 10

def is_same(s,t):
    if s == t:
        return True
    else:
        return False
