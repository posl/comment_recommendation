Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
    else:
        for i in range(len(s)):
            if s[i:] + s[:i] == t:
                print("Yes")
                exit()
        print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
    else:
        if s == t:
            print("Yes")
        else:
            for i in range(1, len(s)):
                if s[i:] + s[:i] == t:
                    print("Yes")
                    break
            else:
                print("No")

=======
Suggestion 3

def move(s, k):
    #print(s, k)
    if k == 0:
        return s
    else:
        return move(s, k-1)[1:] + s[0]

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    for i in range(len(s)):
        if s[i] != t[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def solve():
    s = input()
    t = input()
    n = len(s)
    if n != len(t):
        return "No"
    for i in range(n):
        if s[i] != t[i]:
            return "No"
    return "Yes"

print(solve())

=======
Suggestion 7

def move(s, k):
    for i in range(len(s)):
        if s[i] == "z":
            s[i] = "a"
        else:
            s[i] = chr(ord(s[i]) + k)
    return s

=======
Suggestion 8

def move(s, k):
    if k == 0:
        return s
    else:
        tmp = ''
        for i in range(len(s)):
            if ord(s[i])+k <= ord('z'):
                tmp += chr(ord(s[i])+k)
            else:
                tmp += chr(ord('a') + (ord(s[i])+k)%ord('z')-1)
        return tmp

=======
Suggestion 9

def move_char(s, k):
    new_s = ''
    for i in range(len(s)):
        new_s += chr((ord(s[i]) - ord('a') + k) % 26 + ord('a'))
    return new_s

=======
Suggestion 10

def f(S,T):
    for i in range(26):
        if S==T:
            return True
        else:
            S=S[-1]+S[:-1]
    return False
