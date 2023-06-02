Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print('No')
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 2

def move(s, k):
    return ''.join([chr((ord(x)-ord('a')+k)%26+ord('a')) for x in s])

s = input()
t = input()

for i in range(26):
    if move(s, i) == t:
        print('Yes')
        exit()
print('No')

=======
Suggestion 3

def check(s,t):
    if s == t:
        return True
    else:
        return False

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        for i in range(1, 26):
            ss = ''
            for c in s:
                ss += chr((ord(c) - ord('a') + i) % 26 + ord('a'))
            if ss == t:
                print('Yes')
                return
        print('No')

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
    else:
        for i in range(len(s)):
            if s[i] != t[i]:
                print("No")
                return
        print("Yes")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 7

def move(s, k):
    return chr((ord(s) - ord('a') + k) % 26 + ord('a'))

s = input()
t = input()

for i in range(26):
    for j in range(len(s)):
        if move(s[j], i) != t[j]:
            break
    else:
        print('Yes')
        exit()

print('No')

=======
Suggestion 8

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[i]:
            break
    else:
        print('Yes')
        return

    for k in range(1, 26):
        u = ''
        for j in range(len(s)):
            u += chr((ord(s[j]) - ord('a') + k) % 26 + ord('a'))
        if u == t:
            print('Yes')
            return
    print('No')

=======
Suggestion 9

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if (ord(t[i])-ord(s[i]))%26 != 0:
            print("No")
            return
    print("Yes")
    return

main()

=======
Suggestion 10

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print('No')
        return
    if s == t:
        print('Yes')
        return
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            print('Yes')
            return
    print('No')
