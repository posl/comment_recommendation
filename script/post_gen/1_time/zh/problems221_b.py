Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()

    if len(S) != len(T):
        print("No")
        return

    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            if S[i] == T[j] and S[j] == T[i]:
                print("Yes")
                return

    print("No")

=======
Suggestion 2

def swap(s):
    return s[1]+s[0]

s = input()
t = input()

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if len(s) == len(t):
        s_list = list(s)
        t_list = list(t)
        if s_list == t_list:
            print('Yes')
        else:
            for i in range(len(s_list)):
                for j in range(len(s_list)):
                    if i == j:
                        continue
                    else:
                        s_list[i],s_list[j] = s_list[j],s_list[i]
                        if s_list == t_list:
                            print('Yes')
                            break
                        else:
                            s_list[i],s_list[j] = s_list[j],s_list[i]
                else:
                    continue
                break
            else:
                print('No')
    else:
        print('No')

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        return
    for i in range(len(S)-1):
        if S[i] == T[i+1] and S[i+1] == T[i]:
            print('Yes')
            return
    print('No')

=======
Suggestion 5

def func(s,t):
    if s==t:
        return True
    else:
        for i in range(len(s)-1):
            if s[i+1]+s[i]==t[i+1]+t[i]:
                return True
    return False

=======
Suggestion 6

def swap(s, i, j):
    s[i], s[j] = s[j], s[i]
    return s

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s)-1):
        if s[i+1] == t[i] and s[i] == t[i+1]:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def swap(S, T):
    for i in range(len(S)-1):
        if S[i] != T[i]:
            if S[i+1] != T[i+1]:
                return False
    return True

S = input()
T = input()

=======
Suggestion 9

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s)-1):
        s = s[:i] + s[i+1] + s[i] + s[i+2:]
        if s == t:
            print("Yes")
            return
        s = s[:i] + s[i+1] + s[i] + s[i+2:]
    print("No")
    return

=======
Suggestion 10

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            tmp = list(S)
            tmp[i], tmp[j] = tmp[j], tmp[i]
            if "".join(tmp) == T:
                print("Yes")
                return
    print("No")
