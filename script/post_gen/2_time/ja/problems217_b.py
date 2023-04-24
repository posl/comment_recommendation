Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC':
        if s2 == 'ARC':
            print('AGC')
        else:
            print('ARC')
    elif s1 == 'ARC':
        if s2 == 'ABC':
            print('AGC')
        else:
            print('ABC')
    else:
        if s2 == 'ABC':
            print('ARC')
        else:
            print('ABC')

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == "ABC":
        if s2 == "ARC":
            if s3 == "AGC":
                print("AHC")
            else:
                print("AGC")
        else:
            print("ARC")
    elif s1 == "ARC":
        if s2 == "ABC":
            if s3 == "AGC":
                print("AHC")
            else:
                print("AGC")
        else:
            print("ABC")
    else:
        if s2 == "ABC":
            if s3 == "ARC":
                print("AHC")
            else:
                print("ARC")
        else:
            print("ABC")

=======
Suggestion 4

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC' and s2 == 'ARC':
        print('AGC')
    elif s1 == 'ABC' and s2 == 'AGC':
        print('ARC')
    elif s1 == 'ARC' and s2 == 'AGC':
        print('ABC')
    elif s1 == 'ARC' and s2 == 'ABC':
        print('AGC')
    elif s1 == 'AGC' and s2 == 'ABC':
        print('ARC')
    elif s1 == 'AGC' and s2 == 'ARC':
        print('ABC')
    elif s1 == 'ABC' and s3 == 'ARC':
        print('AGC')
    elif s1 == 'ABC' and s3 == 'AGC':
        print('ARC')
    elif s1 == 'ARC' and s3 == 'AGC':
        print('ABC')
    elif s1 == 'ARC' and s3 == 'ABC':
        print('AGC')
    elif s1 == 'AGC' and s3 == 'ABC':
        print('ARC')
    elif s1 == 'AGC' and s3 == 'ARC':
        print('ABC')
    elif s2 == 'ABC' and s3 == 'ARC':
        print('AGC')
    elif s2 == 'ABC' and s3 == 'AGC':
        print('ARC')
    elif s2 == 'ARC' and s3 == 'AGC':
        print('ABC')
    elif s2 == 'ARC' and s3 == 'ABC':
        print('AGC')
    elif s2 == 'AGC' and s3 == 'ABC':
        print('ARC')
    elif s2 == 'AGC' and s3 == 'ARC':
        print('ABC')

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC' and s2 == 'ARC':
        print('AGC')
    elif s1 == 'ABC' and s2 == 'AGC':
        print('ARC')
    elif s1 == 'ABC' and s2 == 'AHC':
        print('ARC')
    elif s1 == 'ARC' and s2 == 'AGC':
        print('ABC')
    elif s1 == 'ARC' and s2 == 'AHC':
        print('AGC')
    elif s1 == 'AGC' and s2 == 'AHC':
        print('ARC')

=======
Suggestion 6

def main():
    S = []
    for i in range(3):
        S.append(input())

    if 'ABC' not in S:
        print('ABC')
    elif 'ARC' not in S:
        print('ARC')
    elif 'AGC' not in S:
        print('AGC')
    elif 'AHC' not in S:
        print('AHC')

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    total = ["ABC", "ARC", "AGC", "AHC"]
    total.remove(s1)
    total.remove(s2)
    total.remove(s3)
    print(total[0])

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    if 'ABC' in s:
        s.remove('ABC')
    if 'ARC' in s:
        s.remove('ARC')
    if 'AGC' in s:
        s.remove('AGC')
    if 'AHC' in s:
        s.remove('AHC')
    print(s[0])

=======
Suggestion 9

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = [S1, S2, S3]
    S.sort()
    if S[0] == 'AGC' and S[1] == 'ARC' and S[2] == 'ABC':
        print('AHC')
    elif S[0] == 'AGC' and S[1] == 'ABC' and S[2] == 'ARC':
        print('AHC')
    elif S[0] == 'ARC' and S[1] == 'AGC' and S[2] == 'ABC':
        print('AHC')
    elif S[0] == 'ARC' and S[1] == 'ABC' and S[2] == 'AGC':
        print('AHC')
    elif S[0] == 'ABC' and S[1] == 'AGC' and S[2] == 'ARC':
        print('AHC')
    elif S[0] == 'ABC' and S[1] == 'ARC' and S[2] == 'AGC':
        print('AHC')
    else:
        print(S[0])
