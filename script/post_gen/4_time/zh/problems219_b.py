Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    result = ""
    for i in T:
        if i == '1':
            result += S1
        elif i == '2':
            result += S2
        else:
            result += S3
    print(result)
main()

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    result = ""
    for i in range(len(t)):
        if t[i] == "1":
            result += s1
        elif t[i] == "2":
            result += s2
        else:
            result += s3
    print(result)

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    result = ''
    for i in range(len(t)):
        if t[i] == '1':
            result += s1
        elif t[i] == '2':
            result += s2
        else:
            result += s3
    print(result)

=======
Suggestion 4

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    result = ''
    for i in range(len(t)):
        if t[i] == '1':
            result += s1
        elif t[i] == '2':
            result += s2
        elif t[i] == '3':
            result += s3
    print(result)

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    result = ''
    for i in range(len(t)):
        if t[i] == '1':
            result += s1
        elif t[i] == '2':
            result += s2
        elif t[i] == '3':
            result += s3
    print(result)
main()

=======
Suggestion 6

def main():
    s1 = input().rstrip()
    s2 = input().rstrip()
    s3 = input().rstrip()
    t = input().rstrip()
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
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    result = ""
    for i in t:
        if i == "1":
            result += s1
        elif i == "2":
            result += s2
        elif i == "3":
            result += s3
    print(result)

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    result = ""
    for i in range(len(t)):
        if t[i] == '1':
            result += s1
        elif t[i] == '2':
            result += s2
        else:
            result += s3
    print(result)

=======
Suggestion 9

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    s = ""
    for t in T:
        if t == '1':
            s += S1
        elif t == '2':
            s += S2
        else:
            s += S3
    print(s)

=======
Suggestion 10

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()

    for i in range(len(t)):
        if t[i] == '1':
            print(s1, end='')
        elif t[i] == '2':
            print(s2, end='')
        elif t[i] == '3':
            print(s3, end='')
    print()
