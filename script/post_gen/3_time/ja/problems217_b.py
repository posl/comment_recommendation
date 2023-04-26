Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = [input() for _ in range(3)]
    if "ABC" not in s:
        print("ABC")
    elif "ARC" not in s:
        print("ARC")
    elif "AGC" not in s:
        print("AGC")
    elif "AHC" not in s:
        print("AHC")

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    s3 = input()

    if s1 == "ABC":
        print("ARC")
    elif s1 == "ARC":
        print("ABC")
    elif s1 == "AGC":
        print("AHC")
    elif s1 == "AHC":
        print("AGC")

    if s2 == "ABC":
        print("ARC")
    elif s2 == "ARC":
        print("ABC")
    elif s2 == "AGC":
        print("AHC")
    elif s2 == "AHC":
        print("AGC")

    if s3 == "ABC":
        print("ARC")
    elif s3 == "ARC":
        print("ABC")
    elif s3 == "AGC":
        print("AHC")
    elif s3 == "AHC":
        print("AGC")

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == "ABC":
        print("ARC")
    elif s1 == "ARC":
        print("ABC")
    elif s1 == "AGC":
        print("AHC")
    elif s1 == "AHC":
        print("AGC")
    elif s2 == "ABC":
        print("ARC")
    elif s2 == "ARC":
        print("ABC")
    elif s2 == "AGC":
        print("AHC")
    elif s2 == "AHC":
        print("AGC")
    elif s3 == "ABC":
        print("ARC")
    elif s3 == "ARC":
        print("ABC")
    elif s3 == "AGC":
        print("AHC")
    elif s3 == "AHC":
        print("AGC")

=======
Suggestion 4

def main():
    s1 = input()
    s2 = input()
    s3 = input()

    if s1 == 'ABC':
        print('ARC')
    elif s2 == 'ABC':
        print('ARC')
    elif s3 == 'ABC':
        print('ARC')

    if s1 == 'ARC':
        print('AGC')
    elif s2 == 'ARC':
        print('AGC')
    elif s3 == 'ARC':
        print('AGC')

    if s1 == 'AGC':
        print('AHC')
    elif s2 == 'AGC':
        print('AHC')
    elif s3 == 'AGC':
        print('AHC')

    if s1 == 'AHC':
        print('ABC')
    elif s2 == 'AHC':
        print('ABC')
    elif s3 == 'AHC':
        print('ABC')

=======
Suggestion 5

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S4 = ['ABC', 'ARC', 'AGC', 'AHC']
    S4.remove(S1)
    S4.remove(S2)
    S4.remove(S3)
    print(S4[0])

=======
Suggestion 6

def main():
    S = [input() for _ in range(3)]
    T = ['ABC', 'ARC', 'AGC', 'AHC']
    for t in T:
        if t not in S:
            print(t)

=======
Suggestion 7

def main():
    S = []
    for i in range(3):
        S.append(input())
    for i in ["ABC", "ARC", "AGC", "AHC"]:
        if i not in S:
            print(i)

=======
Suggestion 8

def main():
    s = [input() for _ in range(3)]
    t = ["ABC", "ARC", "AGC", "AHC"]
    for i in s:
        t.remove(i)
    print(t[0])

=======
Suggestion 9

def main():
    # 入力
    S = [input() for _ in range(3)]

    # 出力
    print('ABC' if 'ABC' not in S else 'ARC' if 'ARC' not in S else 'AGC' if 'AGC' not in S else 'AHC')

=======
Suggestion 10

def main():
    S = [input() for _ in range(3)]
    print(*set('ABC')-set(S), sep='')
