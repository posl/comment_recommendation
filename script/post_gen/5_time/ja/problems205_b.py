Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [i for i in range(1, N+1)]
    B.sort()
    if A == B:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A == list(range(1, N+1)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))

    b = sorted(a)
    if a == b:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        if a[i] != i+1:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a == list(range(1, n + 1)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == n:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a == list(range(1, n+1)):
        print("Yes")
    else:
        print("No")
