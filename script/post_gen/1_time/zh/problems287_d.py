Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    #print(S,T)
    for x in range(len(T)+1):
        S_ = S[:x] + S[len(S) - len(T) + x:]
        #print(S_)
        flag = True
        for i in range(len(T)):
            if S_[i] == "?":
                continue
            if S_[i] != T[i]:
                flag = False
                break
        if flag:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    n = len(t)
    m = len(s)
    for i in range(m-n+1):
        flag = True
        for j in range(n):
            if s[i+j] != t[j] and s[i+j] != "?":
                flag = False
                break
        if flag:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    slen = len(s)
    tlen = len(t)
    for i in range(tlen+1):
        s1 = s[0:i]
        s2 = s[i+tlen:slen]
        if s1.replace('?', 'a') + t + s2.replace('?', 'a') == s:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def solve():
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
    for i in range(ls-lt+1,lt+1):
        print('No')

=======
Suggestion 5

def solve():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    s = s.replace('?', 'a')
    t = t.replace('?', 'a')
    for i in range(n - m + 1):
        if s[i:i + m] == t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def main():
    S = input()
    T = input()

    for i in range(len(S) - len(T) + 1):
        if S[i] == T[0] or S[i] == '?':
            for j in range(len(T)):
                if S[i + j] != T[j] and S[i + j] != '?':
                    break
            else:
                print('YES')
                continue
        print('NO')

=======
Suggestion 7

def main():
    S = input()
    T = input()
    len_s = len(S)
    len_t = len(T)
    for x in range(len_t+1):
        if x == 0:
            S_ = S[len_s-len_t:]
        else:
            S_ = S[:x] + S[len_s-len_t+x:]
        flag = True
        for i in range(len_t):
            if T[i] != '?' and T[i] != S_[i]:
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')

=======
Suggestion 8

def main():
    s = input()
    t = input()
    ls = len(s)
    lt = len(t)
    for x in range(0, lt+1):
        if s[x] == t[x] or s[x] == '?':
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def main():
    s = input()
    t = input()
    print(s)
    print(t)
    for i in range(len(t)+1):
        print(i)

=======
Suggestion 10

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    for i in range(t_len+1):
        s_new = s[:i] + t_len * '?' + s[i+t_len:]
        #print(s_new)
        if s_new == t:
            print('Yes')
        else:
            print('No')
