Synthesizing 10/10 solutions

=======
Suggestion 1

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
    if s3 == 'ABC':
        if s1 == 'ARC':
            print('AGC')
        else:
            print('ARC')
    elif s3 == 'ARC':
        if s1 == 'AGC':
            print('ABC')
        else:
            print('AGC')
    elif s3 == 'AGC':
        if s1 == 'ARC':
            print('ABC')
        else:
            print('ARC')
    return 0

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    if 'ABC' not in s:
        print('ABC')
    elif 'ARC' not in s:
        print('ARC')
    elif 'AGC' not in s:
        print('AGC')
    elif 'AHC' not in s:
        print('AHC')

=======
Suggestion 3

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
Suggestion 4

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC' and s2 == 'ARC':
        print('AGC')
    elif s1 == 'ABC' and s2 == 'AGC':
        print('ARC')
    elif s1 == 'ARC' and s2 == 'ABC':
        print('AGC')
    elif s1 == 'ARC' and s2 == 'AGC':
        print('ABC')
    elif s1 == 'AGC' and s2 == 'ABC':
        print('ARC')
    elif s1 == 'AGC' and s2 == 'ARC':
        print('ABC')

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    l = ['ABC', 'ARC', 'AGC', 'AHC']
    l.remove(s1)
    l.remove(s2)
    l.remove(s3)
    print(l[0])

=======
Suggestion 6

def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()

    S = [S_1, S_2, S_3]
    S.sort()

    if S[0] == "ABC" and S[1] == "AGC":
        print("ARC")
    elif S[0] == "ABC" and S[1] == "AHC":
        print("AGC")
    elif S[0] == "AGC" and S[1] == "ARC":
        print("ABC")
    elif S[0] == "AGC" and S[1] == "AHC":
        print("ARC")
    elif S[0] == "ARC" and S[1] == "AHC":
        print("AGC")
    elif S[0] == "ARC" and S[1] == "ABC":
        print("AGC")
    elif S[0] == "AHC" and S[1] == "ABC":
        print("ARC")
    elif S[0] == "AHC" and S[1] == "ARC":
        print("AGC")

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = set()
    s.add(s1)
    s.add(s2)
    s.add(s3)
    if 'ABC' not in s:
        print('ABC')
    elif 'ARC' not in s:
        print('ARC')
    elif 'AGC' not in s:
        print('AGC')
    else:
        print('AHC')

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()

    if s1 == 'ABC' and s2 == 'ARC':
        print('AGC')
    elif s1 == 'ARC' and s2 == 'ABC':
        print('AGC')
    elif s1 == 'ABC' and s2 == 'AGC':
        print('ARC')
    elif s1 == 'AGC' and s2 == 'ABC':
        print('ARC')
    elif s1 == 'ARC' and s2 == 'AGC':
        print('ABC')
    elif s1 == 'AGC' and s2 == 'ARC':
        print('ABC')

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC':
        if s2 == 'ARC':
            print('AGC')
        else:
            print('ARC')
    elif s2 == 'ABC':
        if s1 == 'ARC':
            print('AGC')
        else:
            print('ARC')
    else:
        if s1 == 'ABC':
            print('AGC')
        else:
            print('ARC')

=======
Suggestion 10

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
