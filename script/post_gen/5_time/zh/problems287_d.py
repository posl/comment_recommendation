Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)
    for i in range(s_len - t_len + 1):
        s1 = s[:i] + s[i + t_len:]
        if t == s1.replace('?', 'a'):
            print('Yes')
        else:
            print('No')

=======
Suggestion 2

def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    for i in range(len_t+1):
        if (s[:i] + t[i:]).replace("?", "a") == t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    n = len(t)
    m = len(s)
    for i in range(m-n+1):
        flag = True
        for j in range(n):
            if s[i+j] != t[j] and s[i+j] != '?':
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')
    for i in range(m-n+1,m):
        print('No')

=======
Suggestion 4

def main():
    S = input()
    T = input()
    x = len(T)
    S = S.replace("?","")
    T = T.replace("?","")
    if x == 0:
        print("Yes")
        return
    if len(S) < x:
        print("No")
        return
    for i in range(len(S)-x+1):
        if S[i:i+x] == T:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 5

def main():
    S = input()
    T = input()
    for i in range(len(S) - len(T) + 1):
        if S[i:i+len(T)].replace('?', 'a') == T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def solve():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    for i in range(n-m+1):
        if s[i:i+m].replace('?', 'a') == t:
            print('Yes')
        else:
            print('No')

solve()

=======
Suggestion 7

def main():
    S = input()
    T = input()
    lenS = len(S)
    lenT = len(T)
    for i in range(lenT+1):
        if i == 0:
            if S[lenT:lenS] == T:
                print("Yes")
            else:
                print("No")
        elif i == lenT:
            if S[0:lenT] == T:
                print("Yes")
            else:
                print("No")
        else:
            if S[i:lenT+i] == T:
                print("Yes")
            else:
                print("No")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)

    for i in range(t_len + 1):
        s_ = s[0:i] + t_len * '?' + s[i + t_len:]
        if s_ == t:
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
    if s_len < t_len:
        print("No")
        return
    for i in range(t_len):
        if s[i] == t[i] or s[i] == "?":
            continue
        else:
            print("No")
            return
    print("Yes")
    for i in range(t_len, s_len):
        if s[i] == "?":
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def main():
    S = input()
    T = input()
    n = len(S)
    m = len(T)
    for x in range(n - m + 1):
        flag = True
        for i in range(m):
            if S[x + i] != T[i] and S[x + i] != '?':
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')
