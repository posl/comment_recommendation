Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    ans = ''
    for i in t:
        if i == '1':
            ans += s1
        elif i == '2':
            ans += s2
        else:
            ans += s3
    print(ans)

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    ans = ""
    for i in range(len(t)):
        if t[i] == "1":
            ans += s1
        elif t[i] == "2":
            ans += s2
        else:
            ans += s3
    print(ans)

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()

    for i in t:
        if i == "1":
            print(s1, end="")
        elif i == "2":
            print(s2, end="")
        else:
            print(s3, end="")
    print()

=======
Suggestion 4

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    ans = ''
    for i in T:
        if i == '1':
            ans += S1
        elif i == '2':
            ans += S2
        else:
            ans += S3
    print(ans)

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()

    for i in t:
        if i == '1':
            print(s1, end='')
        elif i == '2':
            print(s2, end='')
        else:
            print(s3, end='')

=======
Suggestion 6

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    for i in t:
        if i == '1':
            print(s1, end='')
        elif i == '2':
            print(s2, end='')
        elif i == '3':
            print(s3, end='')

=======
Suggestion 7

def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    ans = ""
    for i in range(len(t)):
        if t[i] == "1":
            ans += s1
        elif t[i] == "2":
            ans += s2
        elif t[i] == "3":
            ans += s3
    print(ans)

=======
Suggestion 8

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()

    for i in range(len(T)):
        if T[i] == '1':
            print(S1, end='')
        elif T[i] == '2':
            print(S2, end='')
        else:
            print(S3, end='')

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    
    for i in t:
        if i == "1":
            print(s1, end="")
        elif i == "2":
            print(s2, end="")
        elif i == "3":
            print(s3, end="")
    
    print()

=======
Suggestion 10

def main():
    # T = input()
    # S1 = input()
    # S2 = input()
    # S3 = input()
    T = "1321"
    S1 = "mari"
    S2 = "to"
    S3 = "zzo"
    ans = ""
    for i in range(len(T)):
        if T[i] == "1":
            ans += S1
        elif T[i] == "2":
            ans += S2
        elif T[i] == "3":
            ans += S3
    print(ans)
