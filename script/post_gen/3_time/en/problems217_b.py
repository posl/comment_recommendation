Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    series = ['ABC','ARC','AGC','AHC']
    series.remove(s1)
    series.remove(s2)
    series.remove(s3)
    print(series[0])

=======
Suggestion 2

def main():
    series = ["ABC","ARC","AGC","AHC"]
    s1 = input()
    s2 = input()
    s3 = input()
    series.remove(s1)
    series.remove(s2)
    series.remove(s3)
    print(series[0])

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    print("ABC" if s1 != "ABC" else "ARC" if s2 != "ARC" else "AGC" if s3 != "AGC" else "AHC")

=======
Suggestion 4

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == "ABC":
        if s2 == "ARC":
            print("AGC")
        else:
            print("ARC")
    if s1 == "ARC":
        if s2 == "ABC":
            print("AGC")
        else:
            print("ABC")
    if s1 == "AGC":
        if s2 == "ABC":
            print("ARC")
        else:
            print("ABC")
    if s1 == "AHC":
        if s2 == "ABC":
            print("ARC")
        else:
            print("ABC")

=======
Suggestion 5

def main():
    series = ['ABC', 'ARC', 'AGC', 'AHC']
    for i in range(3):
        series.remove(input())
    print(series[0])

=======
Suggestion 6

def main():
    S = []
    for i in range(3):
        S.append(input())
    for i in ['ABC', 'ARC', 'AGC', 'AHC']:
        if i not in S:
            print(i)

=======
Suggestion 7

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = [S1, S2, S3]
    for i in ["ABC", "ARC", "AGC", "AHC"]:
        if i not in S:
            print(i)

=======
Suggestion 8

def main():
    #write your code here
    s1 = input()
    s2 = input()
    s3 = input()
    s = ["ABC", "ARC", "AGC", "AHC"]
    s.remove(s1)
    s.remove(s2)
    s.remove(s3)
    print(s[0])

=======
Suggestion 9

def main():
    #input
    S = [input() for _ in range(3)]
    #output
    print(*[s for s in ['ABC', 'ARC', 'AGC', 'AHC'] if s not in S], sep='

=======
Suggestion 10

def main():
    # Read input
    S1 = input()
    S2 = input()
    S3 = input()

    # Solve
    S = ["ABC", "ARC", "AGC", "AHC"]
    S.remove(S1)
    S.remove(S2)
    S.remove(S3)

    # Output
    print(S[0])
