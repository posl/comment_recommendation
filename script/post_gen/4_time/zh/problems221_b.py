Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

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
    return

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        s_list = list(S)
        t_list = list(T)
        for i in range(len(s_list)):
            if i == 0:
                s_list[0], s_list[1] = s_list[1], s_list[0]
                if s_list == t_list:
                    print("Yes")
                    break
                else:
                    s_list[0], s_list[1] = s_list[1], s_list[0]
            else:
                s_list[i], s_list[i-1] = s_list[i-1], s_list[i]
                if s_list == t_list:
                    print("Yes")
                    break
                else:
                    s_list[i], s_list[i-1] = s_list[i-1], s_list[i]
        else:
            print("No")

=======
Suggestion 4

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

=======
Suggestion 5

def is_exchangeable(s,t):
    if s == t:
        return True
    else:
        s = list(s)
        t = list(t)
        for i in range(len(s)-1):
            s[i],s[i+1] = s[i+1],s[i]
            if s == t:
                return True
            else:
                s[i],s[i+1] = s[i+1],s[i]
        return False

s = input()
t = input()

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)-1):
            if S[i+1] == T[i] and S[i] == T[i+1]:
                print("Yes")
                break
            elif i == len(S)-2:
                print("No")

=======
Suggestion 7

def swap(s, i, j):
    if i == j:
        return s
    if i > j:
        i, j = j, i
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

=======
Suggestion 8

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        s = S[0:i] + S[i+1] + S[i] + S[i+2:]
        if s == T:
            print("Yes")
            return
    print("No")
    return

main()

=======
Suggestion 9

def solve():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
    for i in range(len(s) - 1):
        if s[i] == t[i + 1] and s[i + 1] == t[i]:
            print("Yes")
            return
    print("No")

solve()
