Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0::2].islower() and s[1::2].isupper():
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 2

def main():
    S = input()
    if S[0::2].islower() and S[1::2].isupper():
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    s = input()
    if s[0::2].islower() and s[1::2].isupper():
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    S = input()
    if S[0::2].islower() and S[1::2].isupper():
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    S = input()
    even = []
    odd = []
    for i in range(len(S)):
        if i % 2 == 0:
            even.append(S[i])
        else:
            odd.append(S[i])
    if all([s.islower() for s in odd]) and all([s.isupper() for s in even]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    S = input()
    print("Yes" if S[0::2].islower() and S[1::2].isupper() else "No")

=======
Suggestion 7

def main():
    S = input()
    print('Yes' if S[0::2].islower() and S[1::2].isupper() else 'No')

=======
Suggestion 8

def main():
    S = input()
    if S[0].islower():
        for i in range(1, len(S), 2):
            if S[i].isupper():
                continue
            else:
                print("No")
                exit()
        for i in range(2, len(S), 2):
            if S[i].islower():
                continue
            else:
                print("No")
                exit()
    else:
        print("No")
        exit()
    print("Yes")

=======
Suggestion 9

def main():
    S = input()
    if S[0].islower():
        for i in range(1,len(S),2):
            if not S[i].islower():
                print('No')
                return
        for i in range(0,len(S),2):
            if not S[i].isupper():
                print('No')
                return
        print('Yes')
    else:
        for i in range(1,len(S),2):
            if not S[i].isupper():
                print('No')
                return
        for i in range(0,len(S),2):
            if not S[i].islower():
                print('No')
                return
        print('Yes')

=======
Suggestion 10

def main():
    s = input()
    if s[0].islower():
        for i in range(1, len(s), 2):
            if not s[i].islower():
                print("No")
                return
    else:
        for i in range(0, len(s), 2):
            if not s[i].isupper():
                print("No")
                return
    print("Yes")
