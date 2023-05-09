Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    print(s1[int(t[0])-1] + s2[int(t[1])-1] + s3[int(t[2])-1] + s1[int(t[3])-1])

=======
Suggestion 2

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    print(S1[int(T[0])-1] + S2[int(T[1])-1] + S3[int(T[2])-1])

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    result = ''
    for i in t:
        if i == '1':
            result += s1
        elif i == '2':
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
    result = ""
    for i in range(len(t)):
        if t[i] == "1":
            result += s1
        elif t[i] == "2":
            result += s2
        elif t[i] == "3":
            result += s3
    print(result)

=======
Suggestion 5

def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    T = input()
    result = ''
    for i in range(len(T)):
        if T[i] == '1':
            result += S_1
        elif T[i] == '2':
            result += S_2
        elif T[i] == '3':
            result += S_3
    print(result)

=======
Suggestion 6

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    s = ""
    for i in t:
        if i == "1":
            s += s1
        elif i == "2":
            s += s2
        else:
            s += s3
    print(s)

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    output = ''
    for i in range(len(t)):
        if t[i] == '1':
            output += s1
        elif t[i] == '2':
            output += s2
        elif t[i] == '3':
            output += s3
    print(output)

=======
Suggestion 8

def solve():
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
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    out = ""
    for i in range(len(t)):
        if t[i] == "1":
            out += s1
        elif t[i] == "2":
            out += s2
        else:
            out += s3
    print(out)

=======
Suggestion 10

def main():
    # input
    S_1 = input()
    S_2 = input()
    S_3 = input()
    T = input()
    # solve
    ans = ""
    for i in range(len(T)):
        if T[i] == "1":
            ans += S_1
        elif T[i] == "2":
            ans += S_2
        else:
            ans += S_3
    # output
    print(ans)
