Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    S = input()
    T = input()

    if len(S) != len(T):
        print("No")
        return

    if S == T:
        print("Yes")
        return

    S = list(S)
    T = list(T)

    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        else:
            for j in range(i+1,len(S)):
                if S[j] == S[i]:
                    S[j] = T[i]
                elif S[j] == T[i]:
                    S[j] = S[i]
            S[i] = T[i]

    if S == T:
        print("Yes")
        return
    else:
        print("No")
        return

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    S = list(S)
    T = list(T)
    S.sort()
    T.sort()
    if S != T:
        print("No")
        return
    print("Yes")
    return

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    S_dict = {}
    T_dict = {}
    for i in range(len(S)):
        if S[i] not in S_dict:
            S_dict[S[i]] = []
        S_dict[S[i]].append(i)
        if T[i] not in T_dict:
            T_dict[T[i]] = []
        T_dict[T[i]].append(i)
    for key in S_dict:
        if key not in T_dict:
            print("No")
            return
        if len(S_dict[key]) != len(T_dict[key]):
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
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
    for key in s_dict:
        if key not in t_dict:
            print("No")
            return
        if len(s_dict[key]) != len(t_dict[key]):
            print("No")
            return
    print("Yes")
    return
main()

=======
Suggestion 5

def solve(s,t):
    s = list(s)
    t = list(t)
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        else:
            if s[i] in t:
                if t[i] in s:
                    s[i],t[i] = t[i],s[i]
                else:
                    return False
            else:
                return False
    return True

s = input()
t = input()

=======
Suggestion 6

def count(s):
    result = {}
    for i in s:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

=======
Suggestion 7

def solve():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)
    if S_len != T_len:
        print("No")
        return
    S_list = list(S)
    T_list = list(T)
    if S_list == T_list:
        print("Yes")
        return
    S_list.sort()
    T_list.sort()
    if S_list != T_list:
        print("No")
        return
    S_list.sort()
    T_list.sort()
    S_dict = {}
    T_dict = {}
    for i in range(S_len):
        if S_list[i] not in S_dict:
            S_dict[S_list[i]] = 1
        else:
            S_dict[S_list[i]] += 1
        if T_list[i] not in T_dict:
            T_dict[T_list[i]] = 1
        else:
            T_dict[T_list[i]] += 1
    for i in range(S_len):
        if S_dict[S_list[i]] != T_dict[T_list[i]]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 8

def main():
    S = input()
    T = input()
    S = list(S)
    T = list(T)
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)-1):
            S[i],S[i+1] = S[i+1],S[i]
            if S == T:
                print("Yes")
                break
            else:
                S[i], S[i + 1] = S[i + 1], S[i]
        else:
            print("No")

=======
Suggestion 9

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    #S = list(S)
    #T = list(T)
    #S.sort()
    #T.sort()
    #print(S)
    #print(T)
    Sdict = {}
    Tdict = {}
    for i in range(len(S)):
        if S[i] in Sdict:
            Sdict[S[i]] += 1
        else:
            Sdict[S[i]] = 1
        if T[i] in Tdict:
            Tdict[T[i]] += 1
        else:
            Tdict[T[i]] = 1
    #print(Sdict)
    #print(Tdict)
    Sdict = sorted(Sdict.items(), key=lambda x:x[1])
    Tdict = sorted(Tdict.items(), key=lambda x:x[1])
    #print(Sdict)
    #print(Tdict)
    for i in range(len(Sdict)):
        if Sdict[i][1] != Tdict[i][1]:
            print("No")
            return
    print("Yes")
    return

main()

=======
Suggestion 10

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print('No')
        return
    if s == t:
        print('Yes')
        return
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()
    if s_list != t_list:
        print('No')
        return
    s_set = set(s_list)
    t_set = set(t_list)
    if len(s_set) != len(t_set):
        print('No')
        return
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
    for key in s_dict:
        if s_dict[key] != t_dict[key]:
            print('No')
            return
    print('Yes')
    return
