Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = []
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
Suggestion 2

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
    else:
        print("ABC")

main()

=======
Suggestion 4

def main():
    S = []
    S.append(input())
    S.append(input())
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
Suggestion 5

def main():
    S = [input() for _ in range(3)]
    T = ['ABC', 'ARC', 'AGC', 'AHC']
    for s in S:
        T.remove(s)
    print(T[0])

=======
Suggestion 6

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    if "ABC" not in s:
        print("ABC")
    elif "ARC" not in s:
        print("ARC")
    elif "AGC" not in s:
        print("AGC")
    elif "AHC" not in s:
        print("AHC")
    else:
        print("Error")
    return

=======
Suggestion 7

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    for i in ["ABC", "ARC", "AGC", "AHC"]:
        if i not in s:
            print(i)

main()

=======
Suggestion 8

def main():
    S = []
    for i in range(3):
        S.append(input())
    for c in ["ABC", "ARC", "AGC", "AHC"]:
        if c not in S:
            print(c)
            break

=======
Suggestion 9

def main():
    # put your code here
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC':
        if s2 == 'ARC':
            if s3 == 'AGC':
                print('AHC')
            else:
                print('AGC')
        else:
            print('ARC')
    else:
        print('ABC')

=======
Suggestion 10

def main():
    # S_1 = input()
    # S_2 = input()
    # S_3 = input()
    S_1, S_2, S_3 = input().split()
    S = ['ABC', 'ARC', 'AGC', 'AHC']
    S.remove(S_1)
    S.remove(S_2)
    S.remove(S_3)
    print(S[0])
