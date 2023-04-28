Synthesizing 10/10 solutions

=======
Suggestion 1

def match(s, t):
    for i in range(len(t)):
        if s[i] != '?' and s[i] != t[i]:
            return False
    return True

s = input()
t = input()

for i in range(len(s) - len(t) + 1):
    if match(s[i:i+len(t)], t):
        s = s[:i] + t + s[i+len(t):]
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

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
            print(''.join(s[:i] + t + s[i+m:]).replace('?', 'a'))
            break
    else:
        print('UNRESTORABLE')

=======
Suggestion 3

def check_match(s, t):
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] != t[i] and s[i] != '?' and t[i] != '?':
            return False
    return True

=======
Suggestion 4

def solve():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    for i in range(n-m+1):
        for j in range(m):
            if s[i+j] != '?' and s[i+j] != t[j]:
                break
        else:
            print('Yes')
            return
    print('No')
solve()

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if len(s) < len(t):
        print('No')
        return
    for i in range(len(t)):
        if s[i] != '?' and s[i] != t[i]:
            print('No')
            return
    for i in range(len(t), len(s)):
        if s[i] != '?':
            print('No')
            return
    print('Yes')

=======
Suggestion 6

def main():
    s = input()
    t = input()
    t_len = len(t)
    s_len = len(s)
    t_list = list(t)
    s_list = list(s)
    for i in range(s_len - t_len + 1):
        for j in range(t_len):
            if s_list[i + j] != t_list[j] and s_list[i + j] != "?":
                break
            if j == t_len - 1:
                for k in range(t_len):
                    s_list[i + k] = t_list[k]
                for k in range(s_len):
                    if s_list[k] == "?":
                        s_list[k] = "a"
                for k in range(s_len):
                    print(s_list[k], end="")
                print()
                return
    print("UNRESTORABLE")

=======
Suggestion 7

def main():
    S = input()
    T = input()
    S = S.replace('?','a')
    T = T.replace('?','a')
    for i in range(0,len(S)-len(T)+1):
        if S[i:i+len(T)] == T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 8

def main():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)
    S = S.replace('?','a')
    T = T.replace('?','a')
    for i in range(S_len-T_len+1):
        if S[i:i+T_len] == T:
            print('Yes')
            for j in range(T_len):
                if S[i+j] == '?':
                    print('a')
                else:
                    print(S[i+j])
            for j in range(i+T_len,S_len):
                if S[j] == '?':
                    print('a')
                else:
                    print(S[j])
            break
        elif i == S_len-T_len:
            print('No')

=======
Suggestion 9

def solve():
    S = input()
    T = input()
    s = len(S)
    t = len(T)
    S = S.replace("?","a")
    for i in range(s-t,-1,-1):
        if T == S[i:i+t]:
            S = S[:i] + T + S[i+t:]
            S = S.replace("?","a")
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 10

def solve(S, T):
    N = len(S)
    M = len(T)
    #print(N, M)
    for i in range(0, M+1):
        S1 = S[0:i]
        S2 = S[i+M:]
        #print(S1, S2)
        if len(S1) != len(S2):
            return False
        for j in range(0, len(S1)):
            if S1[j] != '?' and S2[j] != '?' and S1[j] != S2[j]:
                return False
    return True
