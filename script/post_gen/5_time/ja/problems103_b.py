Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        S = S[-1] + S[:-1]
        if S == T:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def rotate(s):
    return s[1:] + s[0]

s = input()
t = input()

ans = "No"

for i in range(len(s)):
    if s == t:
        ans = "Yes"
        break
    s = rotate(s)

print(ans)

=======
Suggestion 3

def solve():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    else:
        for i in range(len(S)):
            S = S[-1] + S[0:-1]
            if S == T:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 4

def solve():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if s in t+t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        return
    for i in range(len(S)):
        S = S[-1] + S[:-1]
        if S == T:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print('Yes')
            return
    print('No')
main()

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        for i in range(len(s)):
            s = s[-1] + s[:-1]
            if s == t:
                print('Yes')
                break
        else:
            print('No')
main()

=======
Suggestion 9

def main():
    s = input()
    t = input()
    if t in s*2:
        print('Yes')
    else:
        print('No')
