Synthesizing 10/10 solutions (Duplicates hidden)

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
    elif s1 == 'ARC' and s2 == 'ABC':
        print('AGC')
    elif s1 == 'ARC' and s2 == 'AGC':
        print('ABC')
    elif s1 == 'AGC' and s2 == 'ABC':
        print('ARC')
    elif s1 == 'AGC' and s2 == 'ARC':
        print('ABC')
    elif s1 == 'ABC' and s3 == 'ARC':
        print('AGC')
    elif s1 == 'ABC' and s3 == 'AGC':
        print('ARC')
    elif s1 == 'ARC' and s3 == 'ABC':
        print('AGC')
    elif s1 == 'ARC' and s3 == 'AGC':
        print('ABC')
    elif s1 == 'AGC' and s3 == 'ABC':
        print('ARC')
    elif s1 == 'AGC' and s3 == 'ARC':
        print('ABC')
    elif s2 == 'ABC' and s3 == 'ARC':
        print('AGC')
    elif s2 == 'ABC' and s3 == 'AGC':
        print('ARC')
    elif s2 == 'ARC' and s3 == 'ABC':
        print('AGC')
    elif s2 == 'ARC' and s3 == 'AGC':
        print('ABC')
    elif s2 == 'AGC' and s3 == 'ABC':
        print('ARC')
    elif s2 == 'AGC' and s3 == 'ARC':
        print('ABC')

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == "ABC" and s2 == "ARC":
        print("AGC")
    elif s1 == "ABC" and s2 == "AGC":
        print("ARC")
    elif s1 == "ARC" and s2 == "ABC":
        print("AGC")
    elif s1 == "ARC" and s2 == "AGC":
        print("ABC")
    elif s1 == "AGC" and s2 == "ABC":
        print("ARC")
    elif s1 == "AGC" and s2 == "ARC":
        print("ABC")
    elif s1 == "ABC" and s3 == "ARC":
        print("AGC")
    elif s1 == "ABC" and s3 == "AGC":
        print("ARC")
    elif s1 == "ARC" and s3 == "ABC":
        print("AGC")
    elif s1 == "ARC" and s3 == "AGC":
        print("ABC")
    elif s1 == "AGC" and s3 == "ABC":
        print("ARC")
    elif s1 == "AGC" and s3 == "ARC":
        print("ABC")
    elif s2 == "ABC" and s3 == "ARC":
        print("AGC")
    elif s2 == "ABC" and s3 == "AGC":
        print("ARC")
    elif s2 == "ARC" and s3 == "ABC":
        print("AGC")
    elif s2 == "ARC" and s3 == "AGC":
        print("ABC")
    elif s2 == "AGC" and s3 == "ABC":
        print("ARC")
    elif s2 == "AGC" and s3 == "ARC":
        print("ABC")

main()

=======
Suggestion 3

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
Suggestion 4

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    contests = ["ABC", "ARC", "AGC", "AHC"]
    contests.remove(S1)
    contests.remove(S2)
    contests.remove(S3)
    print(contests[0])

=======
Suggestion 5

def main():
    a = input()
    b = input()
    c = input()
    if a == 'ABC':
        if b == 'ARC':
            print('AGC')
        else:
            print('ARC')
    elif a == 'ARC':
        if b == 'ABC':
            print('AGC')
        else:
            print('ABC')
    else:
        if b == 'ABC':
            print('ARC')
        else:
            print('ABC')

=======
Suggestion 6

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
Suggestion 7

def main():
    # input
    S1 = input()
    S2 = input()
    S3 = input()

    # compute

    # output
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
    # input
    S_1 = input()
    S_2 = input()
    S_3 = input()

    # compute

    # output
    print('ABC' if S_1!= 'ABC' and S_2!='ABC' and S_3!='ABC' else 'ARC' if S_1!= 'ARC' and S_2!='ARC' and S_3!='ARC' else 'AGC' if S_1!= 'AGC' and S_2!='AGC' and S_3!='AGC' else 'AHC')

=======
Suggestion 9

def get_series(s1, s2, s3):
    series = ["ABC", "ARC", "AGC", "AHC"]
    for s in [s1, s2, s3]:
        series.remove(s)
    return series[0]
