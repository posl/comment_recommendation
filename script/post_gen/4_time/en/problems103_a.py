Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A1, A2, A3 = map(int, input().split())
    print(min(abs(A1 - A2) + abs(A2 - A3), abs(A1 - A3) + abs(A2 - A3)))

=======
Suggestion 2

def main():
    A = [int(x) for x in input().split()]
    A.sort()
    print(A[1] - A[0] + A[2] - A[1])

=======
Suggestion 3

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[2] - A[0])

=======
Suggestion 4

def main():
    A = list(map(int,input().split()))
    A.sort()
    print(A[1]-A[0]+A[2]-A[1])

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    print(min(abs(a-b)+abs(b-c), abs(a-c)+abs(c-b), abs(b-a)+abs(a-c)))

=======
Suggestion 6

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(abs(A[2]-A[0]))

=======
Suggestion 7

def get_min_cost(a, b, c):
    return abs(a - b) + abs(b - c)
