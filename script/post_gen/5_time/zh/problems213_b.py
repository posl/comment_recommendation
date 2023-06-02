Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int,input().split()))
    second = min(a)
    a.remove(second)
    print(a.index(min(a))+2)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[1])

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    print(A[1])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))

    min1 = min2 = float('inf')
    for i in range(N):
        if A[i] < min1:
            min2 = min1
            min1 = A[i]
        elif A[i] < min2:
            min2 = A[i]

    for i in range(N):
        if A[i] == min2:
            print(i + 1)
            break

=======
Suggestion 6

def main():
    n = int(input())
    player = list(map(int, input().split()))
    player.sort()
    print(player[1])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A = sorted(A)
    print(A[1])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[1])
