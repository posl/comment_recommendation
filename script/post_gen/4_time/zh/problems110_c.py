Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    s_sort = sorted(s)
    t_sort = sorted(t)
    if s_sort == t_sort:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if sorted(s) == sorted(t):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def solve(s, t):
    if len(s) != len(t):
        return False
    
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        if s[i] not in s_dict:
            s_dict[s[i]] = 1
        else:
            s_dict[s[i]] += 1
        if t[i] not in t_dict:
            t_dict[t[i]] = 1
        else:
            t_dict[t[i]] += 1
    
    for k, v in s_dict.items():
        if k not in t_dict:
            return False
        if t_dict[k] != v:
            return False
    
    return True

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    S_set = set(S)
    T_set = set(T)
    if S_set != T_set:
        print("No")
        return
    S_dic = {}
    T_dic = {}
    for i in range(len(S)):
        if S[i] in S_dic:
            S_dic[S[i]].append(i)
        else:
            S_dic[S[i]] = [i]
        if T[i] in T_dic:
            T_dic[T[i]].append(i)
        else:
            T_dic[T[i]] = [i]
    for key in S_dic:
        if S_dic[key] != T_dic[key]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()
    if s_list != t_list:
        print("No")
        return
    print("Yes")

=======
Suggestion 6

def main():
    S = input()
    T = input()
    dic = {}
    for i in range(len(S)):
        if S[i] in dic:
            if dic[S[i]] != T[i]:
                print("No")
                return
        dic[S[i]] = T[i]
    print("Yes")

=======
Suggestion 7

def main():
    S = input()
    T = input()
    S_dict = {}
    T_dict = {}
    for i in range(len(S)):
        if S[i] not in S_dict.keys():
            S_dict[S[i]] = T[i]
        else:
            if S_dict[S[i]] != T[i]:
                print("No")
                return
        if T[i] not in T_dict.keys():
            T_dict[T[i]] = S[i]
        else:
            if T_dict[T[i]] != S[i]:
                print("No")
                return
    print("Yes")

=======
Suggestion 8

def check(s, t):
    s = list(s)
    t = list(t)
    if s == t:
        return True
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            s[i], s[j] = s[j], s[i]
            if s == t:
                return True
            s[i], s[j] = s[j], s[i]
    return False

=======
Suggestion 9

def get_input():
    s = input()
    t = input()
    return s, t

=======
Suggestion 10

def change(S, T):
    s = list(S)
    t = list(T)
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                if t[i] == t[j]:
                    continue
                else:
                    return False
            elif s[i] == t[j]:
                if t[i] == s[j]:
                    continue
                else:
                    return False
            elif s[i] == t[i]:
                if s[j] == t[j]:
                    continue
                else:
                    return False
            else:
                continue
    return True
