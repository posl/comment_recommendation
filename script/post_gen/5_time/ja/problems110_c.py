Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    S_dict = {}
    T_dict = {}
    for s in S:
        if s in S_dict:
            S_dict[s] += 1
        else:
            S_dict[s] = 1
    for t in T:
        if t in T_dict:
            T_dict[t] += 1
        else:
            T_dict[t] = 1
    if sorted(S_dict.values()) == sorted(T_dict.values()):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def replace(s, t):
    s = list(s)
    t = list(t)
    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i] in s[i+1:]:
                s[i+1+s[i+1:].index(s[i])] = t[i]
            else:
                return False
    return True

s = input()
t = input()

=======
Suggestion 3

def main():
    S = list(input())
    T = list(input())
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
    if len(set(S)) == len(set(T)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s = input()
    t = input()
    s_dic = {}
    t_dic = {}
    for i in range(len(s)):
        if s[i] in s_dic:
            s_dic[s[i]].append(i)
        else:
            s_dic[s[i]] = [i]
        if t[i] in t_dic:
            t_dic[t[i]].append(i)
        else:
            t_dic[t[i]] = [i]
    s_list = sorted(s_dic.items(), key=lambda x:x[1])
    t_list = sorted(t_dic.items(), key=lambda x:x[1])
    for i in range(len(s_list)):
        if s_list[i][1] != t_list[i][1]:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 6

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
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)
    S_list = list(S)
    T_list = list(T)

    S_dict = {}
    T_dict = {}
    for i in range(S_len):
        if S_list[i] in S_dict:
            S_dict[S_list[i]] += 1
        else:
            S_dict[S_list[i]] = 1

    for i in range(T_len):
        if T_list[i] in T_dict:
            T_dict[T_list[i]] += 1
        else:
            T_dict[T_list[i]] = 1

    S_dict_sorted = sorted(S_dict.items(), key=lambda x:x[1], reverse=True)
    T_dict_sorted = sorted(T_dict.items(), key=lambda x:x[1], reverse=True)

    S_dict_sorted_len = len(S_dict_sorted)
    T_dict_sorted_len = len(T_dict_sorted)

    if S_dict_sorted_len != T_dict_sorted_len:
        print("No")
        exit()

    for i in range(S_dict_sorted_len):
        if S_dict_sorted[i][1] != T_dict_sorted[i][1]:
            print("No")
            exit()

    print("Yes")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        exit()
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    if s == t:
        print('Yes')
    else:
        print('No')
main()

=======
Suggestion 9

def main():
    S = input()
    T = input()
    #print("S:",S)
    #print("T:",T)
    #print("len(S):",len(S))
    #print("len(T):",len(T))
    if len(S) != len(T):
        print("No")
        return
    if len(S) == 1:
        if S == T:
            print("Yes")
        else:
            print("No")
        return
    Sdic = {}
    Tdic = {}
    for i in range(len(S)):
        if S[i] in Sdic:
            Sdic[S[i]] += 1
        else:
            Sdic[S[i]] = 1
        if T[i] in Tdic:
            Tdic[T[i]] += 1
        else:
            Tdic[T[i]] = 1
    #print("Sdic:",Sdic)
    #print("Tdic:",Tdic)
    if len(Sdic) != len(Tdic):
        print("No")
        return
    for i in range(len(S)):
        if S[i] != T[i]:
            if Sdic[S[i]] != Tdic[S[i]]:
                print("No")
                return
    print("Yes")

=======
Suggestion 10

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        if s_dict.get(s[i]) == None:
            s_dict[s[i]] = t[i]
        elif s_dict[s[i]] != t[i]:
            print("No")
            return
        if t_dict.get(t[i]) == None:
            t_dict[t[i]] = s[i]
        elif t_dict[t[i]] != s[i]:
            print("No")
            return
    print("Yes")
