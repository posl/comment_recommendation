Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        for i in range(len(s)-1):
            if s[i] == t[i+1] and s[i+1] == t[i]:
                print('Yes')
                break
        else:
            print('No')

=======
Suggestion 2

def main():
    s = input()
    t = input()

    if s == t:
        print("Yes")
        return

    for i in range(len(s)-1):
        if s[i] == t[i+1] and s[i+1] == t[i]:
            print("Yes")
            return

    print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(len(s)-1):
            s = s[:i] + s[i+1] + s[i] + s[i+2:]
            if s == t:
                print("Yes")
                break
            else:
                s = s[:i] + s[i+1] + s[i] + s[i+2:]
        else:
            print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    for i in range(len(s) - 1):
        if s[i] == t[i + 1] and s[i + 1] == t[i]:
            print('Yes')
            return
    print('No')

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        for i in range(len(S)-1):
            if S[i+1] == T[i] and S[i] == T[i+1]:
                print('Yes')
                exit()
        print('No')

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s)-1):
        s = list(s)
        s[i], s[i+1] = s[i+1], s[i]
        s = "".join(s)
        if s == t:
            print("Yes")
            return
        else:
            s = list(s)
            s[i], s[i+1] = s[i+1], s[i]
            s = "".join(s)
    print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    s = list(s)
    t = list(t)
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            s[i],s[j] = s[j],s[i]
            if s == t:
                print('Yes')
                return
            s[i],s[j] = s[j],s[i]
    print('No')

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        exit()
    for i in range(len(s)-1):
        if s[i+1] + s[i] == t[i+1] + t[i]:
            print("Yes")
            exit()
    print("No")
main()

=======
Suggestion 9

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    else:
        for i in range(0,len(S)-1):
            if S[i] == T[i+1] and S[i+1] == T[i]:
                print("Yes")
                return
        print("No")
        return

=======
Suggestion 10

def check(s,t):
    if s == t:
        print('Yes')
        return
    s_list = list(s)
    t_list = list(t)
    for i in range(len(s)-1):
        s_list[i],s_list[i+1] = s_list[i+1],s_list[i]
        if s_list == t_list:
            print('Yes')
            return
        s_list[i],s_list[i+1] = s_list[i+1],s_list[i]
    print('No')
    return
