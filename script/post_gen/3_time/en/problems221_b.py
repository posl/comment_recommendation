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
        if s[i] == t[i+1] and s[i+1] == t[i]:
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
        for i in range(len(s)-1):
            if s[i] == t[i+1] and s[i+1] == t[i]:
                print("Yes")
                break
        else:
            print("No")

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        for i in range(len(s)-1):
            if s[i] == t[i+1] and s[i+1] == t[i]:
                print("Yes")
                exit()
        print("No")

=======
Suggestion 4

def main():
    s = input()
    t = input()

    if s == t:
        print('Yes')
        return

    for i in range(len(s)-1):
        if s[i] == t[i+1] and s[i+1] == t[i]:
            print('Yes')
            return

    print('No')
    return

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        exit()
    for i in range(len(s)-1):
        if s[i] == t[i+1] and s[i+1] == t[i]:
            print("Yes")
            exit()
    print("No")
    exit()

=======
Suggestion 6

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        s = list(s)
        t = list(t)
        for i in range(len(s)-1):
            s[i], s[i+1] = s[i+1], s[i]
            if s == t:
                print("Yes")
                break
            s[i], s[i+1] = s[i+1], s[i]
        else:
            print("No")

=======
Suggestion 7

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return

    for i in range(len(s)-1):
        if s[i] == t[i+1] and s[i+1] == t[i]:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
        exit()
    s = list(s)
    t = list(t)
    for i in range(len(s)-1):
        s[i], s[i+1] = s[i+1], s[i]
        if s == t:
            print('Yes')
            exit()
        s[i], s[i+1] = s[i+1], s[i]
    print('No')

=======
Suggestion 9

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    for i in range(len(s)-1):
        if s[i] != t[i]:
            if s[i+1] == t[i] and s[i] == t[i+1]:
                print("Yes")
                return
    print("No")
