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

=======
Suggestion 2

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
        elif i == "3":
            ans += s3
    print(ans)

=======
Suggestion 3

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
Suggestion 4

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    ans = ""
    for i in T:
        if i == "1":
            ans += S1
        elif i == "2":
            ans += S2
        else:
            ans += S3
    print(ans)

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
        else:
            print(S3, end='')
    print()

=======
Suggestion 6

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    res = ""
    for i in t:
        if i == "1":
            res += s1
        elif i == "2":
            res += s2
        else:
            res += s3
    print(res)

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    d = {"1":s1, "2":s2, "3":s3}
    print("".join([d[k] for k in t]))

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    s = ''
    for i in t:
        if i == '1':
            s += s1
        if i == '2':
            s += s2
        if i == '3':
            s += s3
    print(s)

=======
Suggestion 9

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    
    for i in range(len(T)):
        if T[i] == "1":
            print(S1, end="")
        elif T[i] == "2":
            print(S2, end="")
        elif T[i] == "3":
            print(S3, end="")
    
    print()

=======
Suggestion 10

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    ans = ""
    for i in T:
        if i=="1":
            ans += S1
        elif i=="2":
            ans += S2
        elif i=="3":
            ans += S3
    print(ans)
