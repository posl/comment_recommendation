Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = ['ABC', 'ARC', 'AGC', 'AHC']
    s.remove(s1)
    s.remove(s2)
    s.remove(s3)
    print(s[0])

=======
Suggestion 2

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = [S1, S2, S3]
    T = ["ABC", "ARC", "AGC", "AHC"]
    for s in S:
        T.remove(s)
    print(T[0])

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = ["ABC","ARC","AGC","AHC"]
    s4.remove(s1)
    s4.remove(s2)
    s4.remove(s3)
    print(s4[0])

=======
Suggestion 4

def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()

    if S_1 == "ABC":
        print("ARC")
    elif S_2 == "ABC":
        print("ARC")
    elif S_3 == "ABC":
        print("ARC")
    elif S_1 == "ARC":
        print("ABC")
    elif S_2 == "ARC":
        print("ABC")
    elif S_3 == "ARC":
        print("ABC")
    elif S_1 == "AGC":
        print("AHC")
    elif S_2 == "AGC":
        print("AHC")
    elif S_3 == "AGC":
        print("AHC")
    elif S_1 == "AHC":
        print("AGC")
    elif S_2 == "AHC":
        print("AGC")
    elif S_3 == "AHC":
        print("AGC")

=======
Suggestion 5

def main():
    S = [input() for _ in range(3)]
    for s in ['ABC', 'ARC', 'AGC', 'AHC']:
        if s not in S:
            print(s)
            break

=======
Suggestion 6

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = [S1, S2, S3]
    S.sort()
    if S[0] == 'ABC':
        print('ARC')
    elif S[0] == 'AGC':
        print('AHC')
    elif S[0] == 'ARC':
        print('AGC')

=======
Suggestion 7

def main():
    # 入力
    S1 = input()
    S2 = input()
    S3 = input()
    # 出力
    if S1 == "ABC":
        print("ARC")
    elif S1 == "ARC":
        print("AGC")
    elif S1 == "AGC":
        print("AHC")
    elif S1 == "AHC":
        print("ABC")
    if S2 == "ABC":
        print("ARC")
    elif S2 == "ARC":
        print("AGC")
    elif S2 == "AGC":
        print("AHC")
    elif S2 == "AHC":
        print("ABC")
    if S3 == "ABC":
        print("ARC")
    elif S3 == "ARC":
        print("AGC")
    elif S3 == "AGC":
        print("AHC")
    elif S3 == "AHC":
        print("ABC")

=======
Suggestion 8

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    s.sort()
    for i in range(3):
        if s[i] == "ABC":
            print("ARC")
        elif s[i] == "ARC":
            print("AGC")
        elif s[i] == "AGC":
            print("AHC")
        elif s[i] == "AHC":
            print("ABC")
        else:
            print("Error")

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    print("".join(set(["ABC","ARC","AGC","AHC"]) - set([s1,s2,s3])))

=======
Suggestion 10

def main():
    # S_1 = input()
    # S_2 = input()
    # S_3 = input()
    S_1, S_2, S_3 = input(), input(), input()
    if S_1 != 'ABC' and S_2 != 'ABC' and S_3 != 'ABC':
        print('ABC')
    elif S_1 != 'ARC' and S_2 != 'ARC' and S_3 != 'ARC':
        print('ARC')
    elif S_1 != 'AGC' and S_2 != 'AGC' and S_3 != 'AGC':
        print('AGC')
    elif S_1 != 'AHC' and S_2 != 'AHC' and S_3 != 'AHC':
        print('AHC')
