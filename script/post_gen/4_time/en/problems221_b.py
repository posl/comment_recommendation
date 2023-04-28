Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        if S[i] == T[i+1] and S[i+1] == T[i]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        if S[i] == T[i+1] and S[i+1] == T[i]:
            print("Yes")
            return
    print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s) - 1):
        if s[i] == t[i + 1] and s[i + 1] == t[i]:
            print("Yes")
            return
    print("No")

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        if S[:i] + S[i+1] + S[i] + S[i+2:] == T:
            print("Yes")
            return
    print("No")

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        return
    for i in range(len(S)-1):
        if S[:i] + S[i+1] + S[i] + S[i+2:] == T:
            print('Yes')
            return
    print('No')

=======
Suggestion 7

def main():
    S = input()
    T = input()

    if S == T:
        print("Yes")
        return

    for i in range(len(S)-1):
        s = S[:i] + S[i+1] + S[i] + S[i+2:]
        if s == T:
            print("Yes")
            return

    print("No")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    s_list = list(s)
    t_list = list(t)
    for i in range(len(s_list) - 1):
        s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
        if s_list == t_list:
            print("Yes")
            return
        s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
    print("No")

=======
Suggestion 9

def solve():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        if S[i] != T[i]:
            if S[i+1] == T[i] and S[i] == T[i+1]:
                print("Yes")
                return
    print("No")

=======
Suggestion 10

def solve(s,t):
    s = list(s)
    t = list(t)
    for i in range(len(s)-1):
        if s[i] != t[i]:
            s[i], s[i+1] = s[i+1], s[i]
            break
    return "Yes" if s == t else "No"

s = input()
t = input()
print(solve(s,t))
