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

=======
Suggestion 2

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

main()

=======
Suggestion 4

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
        elif i == '3':
            result += s3
    print(result)

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    d = {'1':s1, '2':s2, '3':s3}
    print(''.join([d[c] for c in t]))

=======
Suggestion 6

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
Suggestion 7

def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    T = input()

    for i in range(len(T)):
        if T[i] == '1':
            print(S_1, end='')
        elif T[i] == '2':
            print(S_2, end='')
        elif T[i] == '3':
            print(S_3, end='')

=======
Suggestion 8

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    S = {1: S1, 2: S2, 3: S3}
    print(''.join([S[int(t)] for t in T]))

=======
Suggestion 9

def main():
    s1=input()
    s2=input()
    s3=input()
    t=input()
    d={'1':s1,'2':s2,'3':s3}
    s=''
    for i in t:
        s=s+d[i]
    print(s)

=======
Suggestion 10

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    
    s = ''
    for i in T:
        if i == '1':
            s += S1
        elif i == '2':
            s += S2
        else:
            s += S3
    print(s)
