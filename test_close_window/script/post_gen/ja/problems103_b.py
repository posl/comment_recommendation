Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        S = S[-1] + S[:-1]
        if S == T:
            print("Yes")
            break
    else:
        print("No")

=======

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        S = S[-1] + S[:-1]
        if S == T:
            print('Yes')
            exit()
    print('No')

=======

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

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)-1):
            S = S[-1] + S[:-1]
            if S == T:
                print("Yes")
                break
        else:
            print("No")

=======

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s == t:
            print("Yes")
            exit()
    print("No")

=======

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s == t:
            print("Yes")
            exit()
        s = s[1:] + s[0]
    print("No")

=======

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s == t:
            print('Yes')
            break
        else:
            s = s[1:] + s[0]
    else:
        print('No')

=======

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

def main():
    S = input()
    T = input()

    if S == T:
        print('Yes')
        return

    for i in range(len(S)):
        if S == T:
            print('Yes')
            return
        S = S[1:] + S[0]

    print('No')
