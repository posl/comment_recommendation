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
        elif i == '3':
            print(s3, end='')

main()

=======
Suggestion 2

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
    print()
main()

=======
Suggestion 3

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
Suggestion 4

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    for i in range(len(t)):
        if t[i] == '1':
            print(s1, end='')
        if t[i] == '2':
            print(s2, end='')
        if t[i] == '3':
            print(s3, end='')
    print()

=======
Suggestion 5

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
Suggestion 6

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

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    s = ""
    for i in range(len(t)):
        if t[i] == "1":
            s += s1
        elif t[i] == "2":
            s += s2
        elif t[i] == "3":
            s += s3
    print(s)

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    s = []
    for i in t:
        if i == '1':
            s.append(s1)
        elif i == '2':
            s.append(s2)
        else:
            s.append(s3)
    print(''.join(s))

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    dic = {'1': s1, '2': s2, '3': s3}
    ans = ''
    for i in t:
        ans += dic[i]
    print(ans)

=======
Suggestion 10

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    S = [S1, S2, S3]
    print("".join([S[int(t)-1] for t in T]))
