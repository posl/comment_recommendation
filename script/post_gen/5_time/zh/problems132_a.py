Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if len(set(s)) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    check = set(s)
    if len(check) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    if len(set(s)) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    s = input()
    # print(s)
    if len(s) != 4:
        print("No")
        return
    if len(set(s)) != 2:
        print("No")
        return
    for i in set(s):
        if s.count(i) != 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    s = input()
    if len(set(s)) == 2:
        if s.count(s[0]) == 2 and s.count(s[1]) == 2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = input()
    if len(s) != 4:
        print("No")
        return
    for c in s:
        if s.count(c) != 2:
            print("No")
            return
    print("Yes")
    return

main()

=======
Suggestion 7

def main():
    s = input()
    if len(s) != 4:
        print("No")
        return
    if len(set(s)) != 2:
        print("No")
        return
    for c in set(s):
        if s.count(c) != 2:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 8

def main():
    S = input()
    if S[0] == S[1] and S[2] == S[3] and S[0] != S[2]:
        print('Yes')
    elif S[0] == S[2] and S[1] == S[3] and S[0] != S[1]:
        print('Yes')
    elif S[0] == S[3] and S[1] == S[2] and S[0] != S[1]:
        print('Yes')
    else:
        print('No')
