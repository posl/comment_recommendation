Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    if S1 == 'ABC':
        if S2 == 'ARC':
            print('AGC')
        else:
            print('ARC')
    elif S1 == 'AGC':
        if S2 == 'ARC':
            print('ABC')
        else:
            print('ARC')
    else:
        if S2 == 'ABC':
            print('AGC')
        else:
            print('ABC')

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    l = ["ABC", "ARC", "AGC", "AHC"]
    for i in range(4):
        if l[i] not in s:
            print(l[i])
            break

=======
Suggestion 3

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = set([S1,S2,S3])
    S4 = set(['ABC','ARC','AGC','AHC'])
    print(S4.difference(S).pop())

=======
Suggestion 4

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    if S1 == "ABC":
        if S2 == "ARC":
            print("AGC")
        else:
            print("ARC")
    elif S1 == "ARC":
        if S2 == "ABC":
            print("AGC")
        else:
            print("ABC")
    else:
        if S2 == "ABC":
            print("ARC")
        else:
            print("ABC")

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == "ABC":
        if s2 == "ARC":
            print("AGC")
        else:
            print("ARC")
    elif s1 == "ARC":
        if s2 == "ABC":
            print("AGC")
        else:
            print("ABC")
    else:
        if s2 == "ABC":
            print("ARC")
        else:
            print("ABC")

=======
Suggestion 6

def main():
    S = []
    for i in range(3):
        S.append(input())
    S.sort()
    if S[0] == S[1]:
        print(S[2])
    else:
        print(S[0])

=======
Suggestion 7

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    if S1 == 'ABC':
        if S2 == 'ARC':
            print('AGC')
        else:
            print('ARC')
    elif S1 == 'ARC':
        if S2 == 'ABC':
            print('AGC')
        else:
            print('ABC')
    else:
        if S2 == 'ABC':
            print('ARC')
        else:
            print('ABC')

=======
Suggestion 8

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = [S1, S2, S3]
    if 'ABC' not in S:
        print('ABC')
    elif 'ARC' not in S:
        print('ARC')
    elif 'AGC' not in S:
        print('AGC')
    elif 'AHC' not in S:
        print('AHC')
    else:
        print('Error')

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    list = ['ABC','ARC','AGC','AHC']
    list.remove(s1)
    list.remove(s2)
    list.remove(s3)
    print(list[0])

=======
Suggestion 10

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == "ABC" and s2 == "ARC":
        print("AGC")
    elif s1 == "ABC" and s2 == "AGC":
        print("ARC")
    elif s1 == "ABC" and s2 == "AHC":
        print("ARC")
    elif s1 == "ARC" and s2 == "AGC":
        print("ABC")
    elif s1 == "ARC" and s2 == "AHC":
        print("AGC")
    elif s1 == "AGC" and s2 == "AHC":
        print("ARC")
