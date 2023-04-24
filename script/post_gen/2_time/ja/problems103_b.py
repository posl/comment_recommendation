Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 2

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
main()

=======
Suggestion 3

def main():
    s = input()
    t = input()

    for i in range(len(s)):
        if s == t:
            print("Yes")
            return
        else:
            s = s[-1] + s[:-1]
    print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        exit()
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 5

def rotate(s):
    return s[1:] + s[0]

S = input()
T = input()

for _ in range(len(S)):
    if S == T:
        print("Yes")
        exit()
    S = rotate(S)
print("No")

=======
Suggestion 6

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
Suggestion 7

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    S = input()
    T = input()

    if S == T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def get_input():
    s = input()
    t = input()
    return s, t
