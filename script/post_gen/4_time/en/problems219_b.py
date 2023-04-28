Synthesizing 10/10 solutions

=======
Suggestion 1

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
        else:
            result += s3
    print(result)

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
        elif t[i] == "3":
            result += s3
    print(result)

=======
Suggestion 3

def main():
    a = input()
    b = input()
    c = input()
    d = input()
    print(a[int(d[0])-1] + b[int(d[1])-1] + c[int(d[2])-1] + a[int(d[3])-1])

=======
Suggestion 4

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    result = ""
    for i in range(len(T)):
        if T[i] == "1":
            result += S1
        elif T[i] == "2":
            result += S2
        else:
            result += S3
    print(result)

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    res = ""
    for i in range(len(t)):
        if t[i] == "1":
            res += s1
        elif t[i] == "2":
            res += s2
        else:
            res += s3
    print(res)

=======
Suggestion 6

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    ans = ""
    for i in range(len(t)):
        if t[i] == "1":
            ans = ans + s1
        elif t[i] == "2":
            ans = ans + s2
        else:
            ans = ans + s3
    print(ans)

=======
Suggestion 7

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    output = ''
    for i in T:
        if i == '1':
            output += S1
        elif i == '2':
            output += S2
        else:
            output += S3
    print(output)

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    ret = ''
    for i in range(len(t)):
        if t[i] == '1':
            ret += s1
        elif t[i] == '2':
            ret += s2
        elif t[i] == '3':
            ret += s3
    print(ret)

=======
Suggestion 9

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    for i in T:
        if i == "1":
            print(S1, end = "")
        elif i == "2":
            print(S2, end = "")
        else:
            print(S3, end = "")

=======
Suggestion 10

def concatenate_strings(S_1, S_2, S_3, T):
    if len(S_1) <= 10 and len(S_2) <= 10 and len(S_3) <= 10 and len(T) <= 1000:
        if T.count("1") + T.count("2") + T.count("3") == len(T):
            result = ""
            for i in T:
                if i == "1":
                    result += S_1
                elif i == "2":
                    result += S_2
                elif i == "3":
                    result += S_3
            print(result)
