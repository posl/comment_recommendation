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
        if s[i] == s[i+1]:
            s = s[:i+1] + s[i] + s[i+1:]
            if s == t:
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
        print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if len(s) + 1 == len(t):
        if s == t[:-1]:
            print("Yes")
            return
    print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    s_count = {}
    t_count = {}
    for ch in s:
        if ch in s_count:
            s_count[ch] += 1
        else:
            s_count[ch] = 1
    for ch in t:
        if ch in t_count:
            t_count[ch] += 1
        else:
            t_count[ch] = 1
    if s_count == t_count:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def solve():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    if len(s) < len(t):
        print("No")
        return
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s = s[:i+1] + s[i] + s[i+1:]
            if s == t:
                print("Yes")
                return
    print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        exit()
    if len(s) == len(t):
        print('No')
        exit()
    if len(s) < len(t):
        print('No')
        exit()
    while len(s) > len(t):
        if s[-1] == 'a':
            s = s[:-1]
        elif s[-1] == 'b':
            s = s[:-1]
            s = s[::-1]
        else:
            print('No')
            exit()
    if s == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        exit()
    for i in range(1,len(s)):
        if s[i-1] == s[i]:
            if s[:i-1] + s[i+1:] == t:
                print("Yes")
                exit()
    print("No")
