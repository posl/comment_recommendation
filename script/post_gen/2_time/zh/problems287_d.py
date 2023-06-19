Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    t_len = len(t)
    s_len = len(s)
    if t_len == 1:
        for i in range(s_len):
            if s[i] == '?':
                s = s[:i] + t + s[i+1:]
        if s == t:
            print('Yes')
        else:
            print('No')
    else:
        for i in range(s_len-t_len+1):
            if s[i] == '?':
                s = s[:i] + t + s[i+t_len:]
            elif s[i] != t[0]:
                continue
            else:
                if s[i:i+t_len] == t:
                    print('Yes')
                else:
                    print('No')
        if s[i+t_len] == '?':
            s = s[:i+t_len] + t + s[i+t_len+1:]
        elif s[i+t_len] != t[0]:
            pass
        else:
            if s[i+t_len:i+2*t_len] == t:
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
    for i in range(len_t + 1):
        s1 = s[:i] + t[i:] #用t的后半部分替换s的前半部分
        s2 = s[len_s - len_t + i:] + s[:i] #用t的后半部分替换s的前半部分
        if (s1.replace('?', 'a') == t) or (s2.replace('?', 'a') == t):
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def main():
    s = input()
    t = input()
    s = list(s)
    t = list(t)
    for i in range(len(t)):
        if t[i] == '?':
            t[i] = s[i]
    t = ''.join(t)
    for i in range(len(s)-len(t)+1):
        t1 = s[i:i+len(t)]
        flag = True
        for j in range(len(t)):
            if t1[j] != t[j] and t1[j] != '?':
                flag = False
                break
        if flag:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def main():
    S = input()
    T = input()
    S = S.replace('?', 'a')
    T = T.replace('?', 'a')
    for i in range(len(S)-len(T)+1):
        if S[i:i+len(T)] == T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def main():
    s = input()
    t = input()
    s_len = len(s)
    t_len = len(t)

    for i in range(0, t_len + 1):
        s_new = s[0:i] + t_len * "?" + s[i + t_len:s_len]
        flag = True
        for j in range(0, s_len):
            if s_new[j] == "?":
                continue
            elif s_new[j] == t[j]:
                continue
            else:
                flag = False
                break
        if flag:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def match(s, t):
    for i in range(len(s)):
        if s[i] != '?' and t[i] != s[i]:
            return False
    return True

s = input()
t = input()

for i in range(len(s) - len(t) + 1):
    if match(s[i:i+len(t)], t):
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    S = input()
    T = input()
    lenS = len(S)
    lenT = len(T)

    for x in range(lenT+1):
        S1 = S[0:x] + S[lenS-lenT+x:lenS]
        if len(S1) == len(T):
            flag = True
            for i in range(lenT):
                if S1[i] != T[i] and S1[i] != "?":
                    flag = False
                    break
            if flag:
                print("Yes")
            else:
                print("No")
        else:
            print("No")

=======
Suggestion 8

def match(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] == '?':
            continue
        if s[i] != t[i]:
            return False
    return True

=======
Suggestion 9

def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    if len_s < len_t:
        print('No')
        return
    for i in range(len_s - len_t + 1):
        if s[i] == t[0] or s[i] == '?':
            for j in range(1, len_t):
                if s[i + j] != t[j] and s[i + j] != '?':
                    break
            else:
                print('Yes')
                return
    print('No')

=======
Suggestion 10

def main():
    S = input()
    T = input()
    for i in range(len(S) - len(T) + 1):
        if S[i:i + len(T)].replace('?', 'a') >= T.replace('?', 'a'):
            print('Yes')
        else:
            print('No')
