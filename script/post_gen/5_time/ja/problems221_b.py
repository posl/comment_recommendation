Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
    return

=======
Suggestion 2

def main():
    s = input()
    t = input()

    if s == t:
        print("Yes")
    else:
        for i in range(len(s) - 1):
            if s[i] != t[i]:
                if s[i] != t[i + 1] or s[i + 1] != t[i]:
                    print("No")
                    exit()
        print("Yes")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(len(s)-1):
            if s[i] == t[i+1] and s[i+1] == t[i]:
                print("Yes")
                exit()
        print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    s_list = list(s)
    t_list = list(t)
    for i in range(len(s_list)-1):
        tmp = s_list[i]
        s_list[i] = s_list[i+1]
        s_list[i+1] = tmp
        if s_list == t_list:
            print("Yes")
            return
        tmp = s_list[i]
        s_list[i] = s_list[i+1]
        s_list[i+1] = tmp
    print("No")
    return

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(len(s)-1):
            if s[i] == t[i+1] and s[i+1] == t[i]:
                print("Yes")
                return
        print("No")

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)-1):
            if S[i] == T[i+1] and S[i+1] == T[i]:
                print("Yes")
                break
        else:
            print("No")
main()

=======
Suggestion 8

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
Suggestion 9

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    S = list(S)
    T = list(T)
    for i in range(len(S)-1):
        S[i],S[i+1] = S[i+1],S[i]
        if S == T:
            print("Yes")
            return
        S[i],S[i+1] = S[i+1],S[i]
    print("No")
