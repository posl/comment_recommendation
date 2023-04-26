Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 4

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    ans = ""
    for i in t:
        if i == "1":
            ans += s1
        elif i == "2":
            ans += s2
        else:
            ans += s3
    print(ans)

=======
Suggestion 5

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
        elif i == '3':
            ans.append(s3)
    print("".join(ans))

=======
Suggestion 6

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    for i in range(len(t)):
        if t[i] == "1":
            print(s1, end="")
        elif t[i] == "2":
            print(s2, end="")
        elif t[i] == "3":
            print(s3, end="")
    print()

=======
Suggestion 7

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()

    ans = ''
    for i in range(len(T)):
        if T[i] == '1':
            ans += S1
        elif T[i] == '2':
            ans += S2
        else:
            ans += S3

    print(ans)

=======
Suggestion 8

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    result = ""
    for i in T:
        if i == "1":
            result += S1
        elif i == "2":
            result += S2
        else:
            result += S3
    print(result)
main()

=======
Suggestion 9

def main():
    s_1 = input()
    s_2 = input()
    s_3 = input()
    t = input()
    result = ""
    for i in t:
        if i == "1":
            result += s_1
        elif i == "2":
            result += s_2
        else:
            result += s_3
    print(result)
main()

=======
Suggestion 10

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    ans = ""
    for i in range(0, len(t)):
        if t[i] == "1":
            ans += s1
        elif t[i] == "2":
            ans += s2
        elif t[i] == "3":
            ans += s3
    print(ans)
