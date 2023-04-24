Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    if n != m:
        print('No')
        return
    for i in range(n):
        if s[i] != t[i]:
            if s[i+1:] != t[i+1:]:
                print('No')
                return
    print('Yes')

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if len(s) < len(t):
        print("No")
        return
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == len(t):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if len(S) > len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        if S[i] != T[i+1]:
            print("No")
            return
        if S[i+1] != T[i+2]:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def solve():
    s = input()
    t = input()
    if len(s) > len(t):
        print("No")
        return
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    if i == len(s):
        print("Yes")
    else:
        print("No")

solve()

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if len(s) < len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
    i = 0
    while i < len(s):
        if i == len(t):
            print("Yes")
            return
        if s[i] == t[i]:
            i += 1
        else:
            if i + 1 < len(s) and s[i] == s[i + 1]:
                s = s[:i] + s[i + 1:]
            else:
                print("No")
                return
    if i == len(t):
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 6

def main():
    S = input()
    T = input()

    N = len(S)
    M = len(T)

    if N > M:
        print('No')
        return

    for i in range(M - N + 1):
        s = S
        t = T[i:i + N]
        for j in range(N):
            if s[j] != t[j] and s[j] != '?':
                break
        else:
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
    if len(S) == 1:
        print("No")
        return
    if len(S) == 2:
        if S[0] == T[0] or S[1] == T[1]:
            print("Yes")
        else:
            print("No")
        return
    if S[0] == T[0] and S[-1] == T[-1]:
        print("Yes")
    elif S[0] == T[0]:
        print("Yes")
    elif S[-1] == T[-1]:
        print("Yes")
    else:
        print("No")

main()

I got WA and I don't know why. I think I have covered all the cases.

Can someone please help me?

Thanks in advance.

I am new to python and I am trying to write a program that will take a list of numbers and find the max and min of the list. I have the code below but when I run it, it says that the input is invalid. I don't know what I am doing wrong. Any help would be appreciated.

=======
Suggestion 8

def main():
    S = input()
    T = input()
    S = S.replace("a", "aa")
    S = S.replace("b", "bb")
    S = S.replace("c", "cc")
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def solve():
    S = input()
    T = input()
    #print(S)
    #print(T)
    S = S.replace('a', 'b')
    T = T.replace('a', 'b')
    #print(S)
    #print(T)
    if S == T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def solve(S, T):
    # S = abbaac
    # T = abbbbaaac
    # S = xyzz
    # T = xyyzz
    # S = aaaaa
    # T = aaaaaa
    # S = aaaaa
    # T = aaaaaaa
    # S = aaaaa
    # T = aaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    # S = aaaaa
    # T = aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    # S = aaaaa
    # T =
