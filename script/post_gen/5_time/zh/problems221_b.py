Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        if S[i:i+2] == T[i+1:i-1:-1]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 2

def swap(S,T):
    if len(S) != len(T):
        return False
    if S == T:
        return True
    else:
        for i in range(len(S)):
            for j in range(i+1,len(S)):
                if S[i] == T[j] and S[j] == T[i]:
                    return True
    return False

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    for i in range(len(s)-1):
        if s[i] == t[i+1] and s[i+1] == t[i]:
            print('Yes')
            return
    print('No')

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            if S[i] == T[i+1] and S[i+1] == T[i]:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 5

def swap_char(s, t):
    if len(s) != len(t):
        return False
    if s == t:
        return True
    s_list = list(s)
    t_list = list(t)
    for i in range(len(s_list) - 1):
        s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
        if s_list == t_list:
            return True
        else:
            s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
    return False

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    if len(S) != len(T):
        print("No")
        return
    for i in range(len(S)-1):
        if S[i] == T[i+1] and S[i+1] == T[i]:
            print("Yes")
            return
    print("No")

=======
Suggestion 7

def swap(s):
    if len(s) != 2:
        return s
    else:
        return s[::-1]

s = input()
t = input()

=======
Suggestion 8

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        exit()
    for i in range(len(S)-1):
        if S[i] == T[i+1] and S[i+1] == T[i]:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 9

def swap(s, t):
    for i in range(len(s)-1):
        if s[i] == t[i+1] and s[i+1] == t[i]:
            return True
    return False

s = input()
t = input()
