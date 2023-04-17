Synthesizing 10/10 solutions

=======

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        return
    for i in range(len(s)-1):
        s = s[-1] + s[:-1]
        if s == t:
            print('Yes')
            return
    print('No')

=======

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S) - 1):
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
    if s == t:
        print("Yes")
        return
    for i in range(1, len(s)):
        if s[i:] + s[:i] == t:
            print("Yes")
            return
    print("No")

=======

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
                break
        else:
            print("No")

=======

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        for i in range(len(s) - 1):
            s = s[-1] + s[:-1]
            if s == t:
                print('Yes')
                return
        print('No')

=======

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, len(S)):
        if S[i:] + S[:i] == T:
            print("Yes")
            return
    print("No")

=======

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        for _ in range(len(s) - 1):
            s = s[-1] + s[:-1]
            if s == t:
                print('Yes')
                break
        else:
            print('No')

=======

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-1):
        S = S[-1] + S[0:-1]
        if S == T:
            print("Yes")
            return
    print("No")
    return

=======

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    elif S == T[1:] + T[0]:
        print("Yes")
    else:
        print("No")

=======

def main():

    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    if len(S) != len(T):
        print("No")
        return
    for i in range(len(S) - 1):
        S = S[-1] + S[:len(S) - 1]
        if S == T:
            print("Yes")
            return
    print("No")
    return
