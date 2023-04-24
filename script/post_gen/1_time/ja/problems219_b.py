Synthesizing 10/10 solutions

=======
Suggestion 1

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
    print()

=======
Suggestion 2

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
Suggestion 3

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    for i in T:
        if i == '1':
            print(S1, end='')
        elif i == '2':
            print(S2, end='')
        else:
            print(S3, end='')

=======
Suggestion 4

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

=======
Suggestion 5

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
        elif T[i] == '3':
            print(S3, end='')

=======
Suggestion 6

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
Suggestion 7

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    for t in T:
        if t == '1':
            print(S1, end='')
        elif t == '2':
            print(S2, end='')
        elif t == '3':
            print(S3, end='')

=======
Suggestion 8

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
        elif i == '3':
            ans += s3

    print(ans)

=======
Suggestion 9

def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    T = input()
    ans = ""
    for i in T:
        if i == "1":
            ans += S_1
        elif i == "2":
            ans += S_2
        else:
            ans += S_3
    print(ans)

=======
Suggestion 10

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()

    S = [S1, S2, S3]
    ans = ''
    for t in T:
        ans += S[int(t) - 1]
    print(ans)
