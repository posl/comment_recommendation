Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = list(input())
    T = list(input())
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    for i in range(len(S)):
        if S[i] != T[i]:
            for j in range(i+1, len(S)):
                if S[j] == T[i]:
                    S[i], S[j] = S[j], S[i]
                    break
            else:
                print("No")
                return
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if sorted(S) == sorted(T):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
    # 用一个字典记录S中每个字母出现的位置
    s_dict = {}
    for i in range(len(s)):
        if s[i] not in s_dict:
            s_dict[s[i]] = [i]
        else:
            s_dict[s[i]].append(i)
    # 用一个字典记录T中每个字母出现的位置
    t_dict = {}
    for i in range(len(t)):
        if t[i] not in t_dict:
            t_dict[t[i]] = [i]
        else:
            t_dict[t[i]].append(i)
    # 如果s和t中有不同的字母，返回No
    if len(s_dict) != len(t_dict):
        print("No")
        return
    # 如果s和t中有相同的字母，但是出现的次数不同，返回No
    for key in s_dict:
        if key not in t_dict:
            print("No")
            return
        if len(s_dict[key]) != len(t_dict[key]):
            print("No")
            return
    # 如果s和t中有相同的字母，出现的次数也相同，但是出现的位置不同，返回No
    for key in s_dict:
        for i in range(len(s_dict[key])):
            if s_dict[key][i] != t_dict[key][i]:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    s_dic = {}
    t_dic = {}
    for i in range(len(s)):
        if s[i] not in s_dic:
            s_dic[s[i]] = t[i]
        else:
            if s_dic[s[i]] != t[i]:
                print("No")
                return
        if t[i] not in t_dic:
            t_dic[t[i]] = s[i]
        else:
            if t_dic[t[i]] != s[i]:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 5

def solve():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        else:
            for j in range(i+1, len(S)):
                if S[j] == S[i]:
                    if T[j] == T[i]:
                        S = S[:i] + T[j] + S[i+1:]
                        T = T[:i] + S[j] + T[i+1:]
                        break
                    else:
                        print("No")
                        return
                elif T[j] == T[i]:
                    if S[j] == S[i]:
                        S = S[:i] + T[j] + S[i+1:]
                        T = T[:i] + S[j] + T[i+1:]
                        break
                    else:
                        print("No")
                        return
            if S[i] != T[i]:
                print("No")
                return
    print("Yes")

=======
Suggestion 6

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
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            S[i], S[j] = S[j], S[i]
            if S == T:
                print("Yes")
                return
            S[i], S[j] = S[j], S[i]
    print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    s_list = list(s)
    t_list = list(t)
    s_set = set(s_list)
    t_set = set(t_list)
    if len(s_set) != len(t_set):
        print("No")
        return
    else:
        s_dict = {}
        t_dict = {}
        for i in range(len(s_set)):
            s_dict[s_set.pop()] = 0
            t_dict[t_set.pop()] = 0
        for i in range(len(s)):
            s_dict[s_list[i]] += 1
            t_dict[t_list[i]] += 1
        if s_dict == t_dict:
            print("Yes")
        else:
            print("No")
        return

=======
Suggestion 8

def main():
    S = input()
    T = input()
    if len(S) == len(T):
        for i in range(len(S)):
            if S[i] != T[i]:
                if S[i] in S[:i] or T[i] in T[:i]:
                    print('No')
                    break
                else:
                    S = S.replace(S[i], T[i])
                    T = T.replace(T[i], S[i])
        else:
            if S == T:
                print('Yes')
            else:
                print('No')
    else:
        print('No')

=======
Suggestion 9

def main():
    S = input()
    T = input()
    if len(set(S)) != len(set(T)):
        print("No")
        exit()
    if len(S) != len(T):
        print("No")
        exit()
    dic = {}
    for i in range(len(S)):
        if S[i] in dic:
            if dic[S[i]] != T[i]:
                print("No")
                exit()
        else:
            dic[S[i]] = T[i]
    print("Yes")

=======
Suggestion 10

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    # Sの各文字の出現回数を数える
    S_count = {}
    for c in S:
        if c in S_count:
            S_count[c] += 1
        else:
            S_count[c] = 1
    # Tの各文字の出現回数を数える
    T_count = {}
    for c in T:
        if c in T_count:
            T_count[c] += 1
        else:
            T_count[c] = 1
    # Sの各文字の出現回数とTの各文字の出現回数が一致するかどうかを調べる
    for c in S_count.keys():
        if c not in T_count.keys():
            print("No")
            return
        if S_count[c] != T_count[c]:
            print("No")
            return
    print("Yes")
