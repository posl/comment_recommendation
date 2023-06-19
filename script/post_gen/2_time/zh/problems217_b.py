Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S1 = input()
    S2 = input()
    S3 = input()

    S = [S1, S2, S3]
    S.sort()

    if S == ['ABC', 'AGC', 'ARC']:
        print('AHC')
    elif S == ['ABC', 'AGC', 'AHC']:
        print('ARC')
    elif S == ['ABC', 'ARC', 'AHC']:
        print('AGC')
    elif S == ['AGC', 'ARC', 'AHC']:
        print('ABC')

=======
Suggestion 2

def main():
    S=[]
    for i in range(3):
        S.append(input())
    if "ABC" not in S:
        print("ABC")
    elif "ARC" not in S:
        print("ARC")
    elif "AGC" not in S:
        print("AGC")
    elif "AHC" not in S:
        print("AHC")

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    s4 = ['ABC', 'ARC', 'AGC', 'AHC']
    for i in s4:
        if i not in s:
            print(i)
            break

=======
Suggestion 4

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    if S1 == 'ABC' and S2 == 'ARC':
        print('AGC')
    elif S1 == 'ABC' and S2 == 'AGC':
        print('ARC')
    elif S1 == 'ARC' and S2 == 'ABC':
        print('AGC')
    elif S1 == 'ARC' and S2 == 'AGC':
        print('ABC')
    elif S1 == 'AGC' and S2 == 'ABC':
        print('ARC')
    elif S1 == 'AGC' and S2 == 'ARC':
        print('ABC')
    elif S1 == 'ABC' and S3 == 'ARC':
        print('AGC')
    elif S1 == 'ABC' and S3 == 'AGC':
        print('ARC')
    elif S1 == 'ARC' and S3 == 'ABC':
        print('AGC')
    elif S1 == 'ARC' and S3 == 'AGC':
        print('ABC')
    elif S1 == 'AGC' and S3 == 'ABC':
        print('ARC')
    elif S1 == 'AGC' and S3 == 'ARC':
        print('ABC')
    elif S2 == 'ABC' and S3 == 'ARC':
        print('AGC')
    elif S2 == 'ABC' and S3 == 'AGC':
        print('ARC')
    elif S2 == 'ARC' and S3 == 'ABC':
        print('AGC')
    elif S2 == 'ARC' and S3 == 'AGC':
        print('ABC')
    elif S2 == 'AGC' and S3 == 'ABC':
        print('ARC')
    elif S2 == 'AGC' and S3 == 'ARC':
        print('ABC')

=======
Suggestion 5

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = [S1, S2, S3]
    S.sort()
    if S[0] == 'ABC' and S[1] == 'AGC' and S[2] == 'ARC':
        print('AHC')
    elif S[0] == 'ABC' and S[1] == 'AGC' and S[2] == 'AHC':
        print('ARC')
    elif S[0] == 'ABC' and S[1] == 'ARC' and S[2] == 'AHC':
        print('AGC')
    elif S[0] == 'AGC' and S[1] == 'ARC' and S[2] == 'AHC':
        print('ABC')

=======
Suggestion 6

def get_input():
    s1 = input()
    s2 = input()
    s3 = input()
    return s1,s2,s3

=======
Suggestion 7

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
        if s2 == 'ARC':
            print('ABC')
        else:
            print('ARC')
    return

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC' and s2 == 'ARC':
        print('AGC')
    elif s1 == 'ABC' and s2 == 'AGC':
        print('ARC')
    elif s1 == 'AGC' and s2 == 'ARC':
        print('ABC')
    elif s1 == 'ARC' and s2 == 'AGC':
        print('ABC')
    elif s1 == 'AGC' and s2 == 'ABC':
        print('ARC')
    elif s1 == 'ARC' and s2 == 'ABC':
        print('AGC')
    elif s1 == 'ABC' and s3 == 'ARC':
        print('AGC')
    elif s1 == 'ABC' and s3 == 'AGC':
        print('ARC')
    elif s1 == 'AGC' and s3 == 'ARC':
        print('ABC')
    elif s1 == 'ARC' and s3 == 'AGC':
        print('ABC')
    elif s1 == 'AGC' and s3 == 'ABC':
        print('ARC')
    elif s1 == 'ARC' and s3 == 'ABC':
        print('AGC')
    elif s2 == 'ABC' and s3 == 'ARC':
        print('AGC')
    elif s2 == 'ABC' and s3 == 'AGC':
        print('ARC')
    elif s2 == 'AGC' and s3 == 'ARC':
        print('ABC')
    elif s2 == 'ARC' and s3 == 'AGC':
        print('ABC')
    elif s2 == 'AGC' and s3 == 'ABC':
        print('ARC')
    elif s2 == 'ARC' and s3 == 'ABC':
        print('AGC')
    else:
        print('ABC')

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    if s.count("ABC") == 0:
        print("ABC")
    elif s.count("ARC") == 0:
        print("ARC")
    elif s.count("AGC") == 0:
        print("AGC")
    elif s.count("AHC") == 0:
        print("AHC")

=======
Suggestion 10

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
