Synthesizing 10/10 solutions

=======
Suggestion 1

def check(s,t):
    if s == t:
        return True
    else:
        for i in range(len(s)-1):
            if s[i] == t[i+1] and s[i+1] == t[i]:
                return True
        return False

s = input()
t = input()

=======
Suggestion 2

def main():
    S = input()
    T = input()
    S_list = list(S)
    T_list = list(T)
    if S_list[0] == T_list[0] and S_list[1] == T_list[1]:
        print("Yes")
    elif S_list[0] == T_list[1] and S_list[1] == T_list[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def check(s,t):
    if s == t:
        return True
    else:
        for i in range(len(s)-1):
            if s[i+1] == t[i] and s[i] == t[i+1]:
                return True
        return False

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)-1):
            if S[i] != S[i+1]:
                S = S[:i] + S[i+1] + S[i] + S[i+2:]
                break
        if S == T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

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
Suggestion 6

def swap_string(s,t):
    if len(s) != len(t):
        return False
    if s == t:
        return True
    else:
        for i in range(len(s)-1):
            if s[i] == t[i+1] and s[i+1] == t[i]:
                return True
        return False

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print('No')
        return
    if s == t:
        print('Yes')
        return
    for i in range(len(s) - 1):
        if s[i] == t[i+1] and s[i+1] == t[i]:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        s = list(s)
        t = list(t)
        for i in range(len(s)-1):
            if s[i] == t[i+1] and s[i+1] == t[i]:
                s[i],s[i+1] = s[i+1],s[i]
                if s == t:
                    print("Yes")
                    break
                else:
                    print("No")
                    break
            else:
                print("No")
                break
        else:
            print("No")

=======
Suggestion 9

def is_anagram(s, t):
    if len(s) == len(t):
        if sorted(s) == sorted(t):
            return True
    return False

=======
Suggestion 10

def main():
    # 从标准输入读取字符串
    s = input()
    t = input()
    # 判断两个字符串是否相等
    if s == t:
        print('Yes')
        return
    # 循环判断s和t的字符是否相等
    for i in range(len(s)-1):
        if s[i] == t[i+1] and s[i+1] == t[i]:
            print('Yes')
            return
    print('No')
main()
