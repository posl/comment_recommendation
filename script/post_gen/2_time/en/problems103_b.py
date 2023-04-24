Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        return
    for i in range(len(S)-1):
        S = S[-1] + S[:-1]
        if S == T:
            print('Yes')
            return
    print('No')

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        return
    for i in range(len(S)-1):
        S = S[-1] + S[:-1]
        if S == T:
            print('Yes')
            return
    print('No')
    return

main()

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        for i in range(len(S)-1):
            S = S[-1] + S[:-1]
            if S == T:
                print('Yes')
                break
        else:
            print('No')

=======
Suggestion 4

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s) - 1):
        s = s[-1] + s[:-1]
        if s == t:
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
        return
    for i in range(len(s)):
        s = s[-1] + s[:-1]
        if s == t:
            print("Yes")
            return
    print("No")

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(len(s)):
            s = s[-1] + s[:-1]
            if s == t:
                print("Yes")
                return
        print("No")
        return

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)-1):
            S = S[-1] + S[:len(S)-1]
            if S == T:
                print("Yes")
                break
        else:
            print("No")

=======
Suggestion 8

def main():
    S = input()
    T = input()

    if S == T:
        print('Yes')
    else:
        for i in range(1, len(S)):
            if S[i:] + S[:i] == T:
                print('Yes')
                break
        else:
            print('No')

=======
Suggestion 9

def isRotated(S, T):
    if S == T:
        return "Yes"
    else:
        for i in range(len(S)-1):
            S = S[-1] + S[:-1]
            if S == T:
                return "Yes"
        return "No"

=======
Suggestion 10

def main():
    S = input()
    T = input()
    print('Yes' if S in T + T else 'No')
