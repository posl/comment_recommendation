Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S[:i] + T[len(T)-i:] == T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def solve():
    S = input()
    T = input()
    N = len(T)
    S = S.replace('?', '0')
    T = T.replace('?', '0')
    S = S + '0' * N
    for i in range(len(S) - N + 1):
        if S[i:i + N] == T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    l = len(t)
    for i in range(len(s)-l+1):
        temp = s[i:i+l]
        for j in range(l):
            if temp[j] == '?':
                temp = temp[:j] + t[j] + temp[j+1:]
        if temp == t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    for i in range(len_s - len_t + 1):
        flag = True
        for j in range(len_t):
            if s[i+j] != t[j] and s[i+j] != '?':
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')
    for i in range(len_t, len_s):
        print('No')

=======
Suggestion 5

def solve(s, t):
    s_list = list(s)
    t_list = list(t)
    for i in range(len(t)):
        if s_list[i] != '?' and s_list[i] != t_list[i]:
            return 'No'
        s_list[i] = t_list[i]
    if s_list.count('?') == 0:
        return 'Yes'
    for i in range(len(t), len(s)):
        if s_list[i] == '?':
            s_list[i] = 'a'
    return 'Yes'

=======
Suggestion 6

def main():
    S = input()
    T = input()
    lenT = len(T)
    lenS = len(S)
    for i in range(lenS - lenT + 1):
        flag = True
        for j in range(lenT):
            if S[i + j] != T[j] and S[i + j] != '?':
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')

=======
Suggestion 7

def problems287_d():
    pass

=======
Suggestion 8

def main():
    s = input()
    t = input()
    ls = len(s)
    lt = len(t)
    for i in range(ls-lt+1):
        flag = True
        for j in range(lt):
            if s[i+j] != t[j] and s[i+j] != '?':
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    for i in range(s_len - t_len + 1):
        flag = True
        for j in range(t_len):
            if s[i + j] != t[j] and s[i + j] != '?':
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')

=======
Suggestion 10

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    for i in range(n-m+1):
        for j in range(m):
            if s[i+j] != t[j] and s[i+j] != '?':
                break
        else:
            print('Yes')
            break
    else:
        print('No')
