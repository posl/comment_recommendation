Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(a) == len(set(a)):
        print("YES")
    else:
        print("NO")

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(a) == len(set(a)):
        print('YES')
    else:
        print('NO')

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if len(A) == len(set(A)):
        print("YES")
    else:
        print("NO")

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == n:
        print("YES")
    else:
        print("NO")

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if len(A) == len(set(A)):
        print('YES')
    else:
        print('NO')

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))

    if len(set(A)) == N:
        print("YES")
    else:
        print("NO")

=======
Suggestion 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == n:
        print("YES")
    else:
        print("NO")

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == len(a):
        print("YES")
    else:
        print("NO")
