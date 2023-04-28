Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    print(A.index(B[-2]) + 1)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sorted = sorted(A)
    print(A.index(A_sorted[-2]) + 1)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sorted = sorted(A, reverse=True)
    print(A.index(A_sorted[1])+1)

=======
Suggestion 4

def main():
    n = int(input())
    scores = list(map(int, input().split()))
    sorted_scores = sorted(scores)
    print(scores.index(sorted_scores[-2])+1)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[-2])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a_sorted = sorted(a, reverse=True)
    print(a.index(a_sorted[1]) + 1)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[-2:].index(A[-2]) + N - 1)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[-2])

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A2 = sorted(A)
    print(A.index(A2[-2])+1)

=======
Suggestion 10

def main():
    n = int(input())
    scores = list(map(int, input().split()))
    scores.sort()
    print(scores[-2])
