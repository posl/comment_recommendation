Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    s = S
    t = T
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()
    if s_list != t_list:
        print("No")
        return
    s_list = list(s)
    t_list = list(t)
    for i in range(len(s_list)):
        for j in range(i+1,len(s_list)):
            s_list[i],s_list[j] = s_list[j],s_list[i]
            if s_list == t_list:
                print("Yes")
                return
            s_list[i],s_list[j] = s_list[j],s_list[i]
    print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    S_list = list(S)
    T_list = list(T)
    S_list.sort()
    T_list.sort()
    if S_list == T_list:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def solve():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
    s_map = {}
    t_map = {}
    for i in range(len(s)):
        if s[i] not in s_map:
            s_map[s[i]] = 1
        else:
            s_map[s[i]] += 1
        if t[i] not in t_map:
            t_map[t[i]] = 1
        else:
            t_map[t[i]] += 1
    if s_map == t_map:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def check(s, t):
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    
    s_dict = {}
    t_dict = {}
    for s, t in zip(S, T):
        if s not in s_dict:
            s_dict[s] = t
        else:
            if s_dict[s] != t:
                print("No")
                return
        if t not in t_dict:
            t_dict[t] = s
        else:
            if t_dict[t] != s:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 6

def main():
    S = input()
    T = input()

    if len(S) != len(T):
        print('No')
        return

    alphabets = [0] * 26
    for i in range(len(S)):
        alphabets[ord(S[i]) - ord('a')] += 1
        alphabets[ord(T[i]) - ord('a')] -= 1

    for i in range(26):
        if alphabets[i] != 0:
            print('No')
            return

    print('Yes')
    return

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
    dic = {}
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = t[i]
        else:
            if dic[s[i]] != t[i]:
                print("No")
                return
    print("Yes")

=======
Suggestion 8

def main():
    S = input()
    T = input()
    #print(S,T)
    #print(len(S),len(T))
    #print(len(S) == len(T))
    #print(S.islower(),T.islower())
    #print(S.isalpha(),T.isalpha())
    if len(S) == len(T) and S.islower() and T.islower() and S.isalpha() and T.isalpha():
        S_list = list(S)
        T_list = list(T)
        S_list.sort()
        T_list.sort()
        #print(S_list)
        #print(T_list)
        if S_list == T_list:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 9

def main():
    s = input()
    t = input()
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort(reverse=True)
    if s_list < t_list:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

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
        if s[i] not in s_dict:
            s_dict[s[i]] = set()
        s_dict[s[i]].add(i)
        if t[i] not in t_dict:
            t_dict[t[i]] = set()
        t_dict[t[i]].add(i)
    s_set = set(s)
    t_set = set(t)
    if s_set != t_set:
        print("No")
        return
    for i in s_set:
        if s_dict[i] != t_dict[i]:
            print("No")
            return
    print("Yes")
    return
