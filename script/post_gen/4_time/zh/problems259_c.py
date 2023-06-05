Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    i = 0
    j = 0
    while i < len(S):
        if j == len(T):
            print('No')
            return
        if S[i] == T[j]:
            i += 1
        j += 1
    print('Yes')

=======
Suggestion 2

def main():
    s = input()
    t = input()
    # print(s)
    # print(t)
    if len(s) == len(t):
        for i in range(len(s)-1):
            if s[i] == t[i]:
                s = s[:i+1] + s[i] + s[i+1:]
                # print(s)
                if s == t:
                    print("Yes")
                    exit()
        print("No")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    # s = "abbaac"
    # t = "abbbbaaac"
    # s = "xyzz"
    # t = "xyyzz"
    if len(s) >= len(t):
        print("No")
    else:
        if s == t[:len(s)]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def insert_char(string, index, char):
    return string[:index] + char + string[index:]

=======
Suggestion 5

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    if n+1 != m:
        print("No")
        return
    i = 0
    j = 0
    while i < n and j < m:
        if s[i] == t[j]:
            i += 1
            j += 1
            continue
        if s[i] != t[j] and s[i] == t[j+1]:
            j += 2
            continue
        print("No")
        return
    print("Yes")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        exit()
    if len(s) >= len(t):
        print('No')
        exit()
    s1 = ''
    index = 0
    for i in range(len(t)):
        if index < len(s):
            if s[index] == t[i]:
                s1 += s[index]
                index += 1
            else:
                s1 += t[i]
        else:
            s1 += t[i]
    if s1 == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if len(s) + 1 == len(t):
        if s + s[-1] == t:
            print('Yes')
            return
    print('No')

=======
Suggestion 8

def main():
    s = input()
    t = input()

    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1

    if i == len(s):
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    if len(s) >= len(t):
        print("No")
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 10

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    if len(s) == len(t):
        print('No')
        return
    if s[0] != t[0]:
        print('No')
        return
    if s[-1] != t[-1]:
        print('No')
        return
    s = s[1:-1]
    t = t[1:-1]
    if s == t:
        print('Yes')
    else:
        print('No')

main()
