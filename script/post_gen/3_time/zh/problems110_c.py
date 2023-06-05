Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if len(s) != len(t):
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
    for i in s_dict:
        if i not in t_dict or s_dict[i] != t_dict[i]:
            print('No')
            return
    print('Yes')

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    dict1 = {}
    dict2 = {}
    for i in range(len(s)):
        if s[i] in dict1:
            if dict1[s[i]] != t[i]:
                print("No")
                return
        else:
            dict1[s[i]] = t[i]
        if t[i] in dict2:
            if dict2[t[i]] != s[i]:
                print("No")
                return
        else:
            dict2[t[i]] = s[i]
    print("Yes")

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
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    if s != t:
        print("No")
        return
    print("Yes")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    #print(S)
    #print(T)

    if len(S) != len(T):
        print("No")
        return
    else:
        for i in range(len(S)):
            if S[i] == T[i]:
                continue
            else:
                #print(S[i])
                #print(T[i])
                #print(S.find(T[i]))
                #print(T.find(S[i]))
                if S.find(T[i]) != -1 and T.find(S[i]) != -1:
                    if S[i] == T[S.find(T[i])] and T[i] == S[T.find(S[i])]:
                        continue
                    else:
                        print("No")
                        return
                else:
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
    for i in range(len(s)):
        if s[i] != t[i]:
            for j in range(i+1,len(s)):
                if s[i] == t[j] and s[j] == t[i]:
                    s = s[:i] + t[i] + s[i+1:j] + t[j] + s[j+1:]
                    break
            else:
                print("No")
                return
    print("Yes")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    #s = 'chokudai'
    #t = 'Redder'
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()
    if s_list == t_list:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
    else:
        s = list(s)
        t = list(t)
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                s[i], s[j] = s[j], s[i]
                if s == t:
                    print("Yes")
                    return
                s[i], s[j] = s[j], s[i]
        print("No")

=======
Suggestion 8

def main():
    S = input()
    T = input()
    #print(S)
    #print(T)
    #print(len(S))
    #print(len(T))
    if len(S) != len(T):
        print("No")
        return
    #print("Yes")
    #print("No")
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(S[10])
    #print(S[11])
    #print(S[12])
    #print(S[13])
    #print(S[14])
    #print(S[15])
    #print(S[16])
    #print(S[17])
    #print(S[18])
    #print(S[19])
    #print(S[20])
    #print(S[21])
    #print(S[22])
    #print(S[23])
    #print(S[24])
    #print(S[25])
    #print(S[26])
    #print(S[27])
    #print(S[28])
    #print(S[29])
    #print(S[30])
    #print(S[31])
    #print(S[32])
    #print(S[33])
    #print(S[34])
    #print(S[35])
    #print(S[36])
    #print(S[37])
    #print(S[38])
    #print(S[39])
    #print(S[40])
    #print(S[41])
    #print(S[42])
    #print(S[43])
    #print(S[44])
    #print(S[45])
    #print(S[46])
    #print(S[47])
    #print(S[48])
    #print(S[49])
    #print(S[50])
    #print(S[51])
    #print(S[52])
    #print(S[53])
    #print(S[54])
    #print(S[55])
    #print(S[56])
    #print(S[57])
    #print(S[58])
    #print(S[59])
    #print(S[60])
    #print(S[61])
    #print

=======
Suggestion 9

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    if s_len != t_len:
        print("No")
        return

    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()
    if s_list != t_list:
        print("No")
        return

    s_dict = {}
    t_dict = {}
    for i in range(s_len):
        if s[i] not in s_dict:
            s_dict[s[i]] = 1
        else:
            s_dict[s[i]] += 1
        if t[i] not in t_dict:
            t_dict[t[i]] = 1
        else:
            t_dict[t[i]] += 1
    s_list = list(s_dict.values())
    t_list = list(t_dict.values())
    s_list.sort()
    t_list.sort()
    if s_list != t_list:
        print("No")
        return

    print("Yes")
