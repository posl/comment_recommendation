Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 4

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    ans = []
    for i in t:
        if i == '1':
            ans.append(s1)
        elif i == '2':
            ans.append(s2)
        else:
            ans.append(s3)
    print(''.join(ans))

=======
Suggestion 5

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()

    ans = ""
    for i in range(len(T)):
        if T[i] == "1":
            ans += S1
        elif T[i] == "2":
            ans += S2
        else:
            ans += S3
    print(ans)

=======
Suggestion 6

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
        elif i == '3':
            ans += S3
    print(ans)

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    ans = ''
    for i in range(len(t)):
        if t[i] == '1':
            ans += s1
        elif t[i] == '2':
            ans += s2
        else:
            ans += s3
    print(ans)

=======
Suggestion 8

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
