Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)):
            S = S[-1] + S[:-1]
            if S == T:
                print("Yes")
                break
        else:
            print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()

    if S == T:
        print("Yes")
        return

    for i in range(len(S)):
        S = S[-1] + S[:-1]
        if S == T:
            print("Yes")
            return

    print("No")

main()

=======
Suggestion 3

def main():
    S = input()
    T = input()

    if S == T:
        print("Yes")
        return

    for _ in range(len(S) - 1):
        S = S[-1] + S[:-1]
        if S == T:
            print("Yes")
            return

    print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)):
            S = S[-1] + S[:len(S)-1]
            if S == T:
                print("Yes")
                return
        print("No")

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(len(s)):
            s = s[-1] + s[0:-1]
            if s == t:
                print("Yes")
                return
        print("No")

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        for i in range(len(S)):
            if S == T:
                print('Yes')
                break
            else:
                S = S[-1] + S[:-1]
        else:
            print('No')

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s) - 1):
        if s[i + 1:] + s[:i + 1] == t:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def check_rotation(s, t):
    if s == t:
        return 'Yes'
    else:
        for i in range(len(s) - 1):
            s = s[-1] + s[:-1]
            if s == t:
                return 'Yes'
    return 'No'

s = input()
t = input()
print(check_rotation(s, t))

=======
Suggestion 9

def rotate(s):
    return s[-1] + s[:-1]

=======
Suggestion 10

def rotate(s):
    return s[-1]+s[:-1]

s=input()
t=input()
