Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if len(s) + 1 != len(t):
        print('No')
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            print('No')
            return
    print('Yes')

=======
Suggestion 2

def solve():
    S = input()
    T = input()
    s = len(S)
    t = len(T)
    if s == t:
        if S == T:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if len(s) + 1 == len(t):
        if s == t[:-1]:
            print("Yes")
            return
    print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if len(s) >= len(t):
        print("Yes")
        return
    else:
        print("No")
        return

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if len(s) + 1 == len(t):
        for i in range(len(s)):
            if s[i] != t[i]:
                print("No")
                exit()
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    S = input()
    T = input()
    while len(S) < len(T):
        if S[-1] == T[-1]:
            if S[0] == T[0]:
                S = S[0] + S + S[1:]
            else:
                S = S + S[0]
        else:
            break
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        return
    else:
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                S = S[:i+1] + S[i] + S[i+1:]
                if S == T:
                    print('Yes')
                    return
        print('No')
        return

=======
Suggestion 8

def main():
    S = input()
    T = input()
    #print(S)
    #print(T)
    #print(len(S))
    #print(len(T))
    if len(S) + 1 != len(T):
        print('No')
        return
    if S == T[:-1]:
        print('Yes')
        return
    print('No')

=======
Suggestion 9

def solve():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    if len(S) < len(T):
        print("No")
        return
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            S = S[:i + 1] + S[i] + S[i + 1:]
            if S == T:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 10

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        exit()
    if len(S) < len(T):
        print('No')
        exit()
    if len(S) == len(T):
        if S[0] == T[0] and S[1] == T[1]:
            print('Yes')
            exit()
        else:
            print('No')
            exit()
    else:
        if S[0] == T[0] and S[1] == T[1]:
            if S[2] == T[2]:
                print('Yes')
                exit()
            elif S[2] == S[1]:
                print('Yes')
                exit()
            else:
                print('No')
                exit()
        else:
            print('No')
            exit()
