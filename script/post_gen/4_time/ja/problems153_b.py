Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) >= H:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if H <= sum(A):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if H <= sum(A):
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) >= h:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))

    if h <= sum(a):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    print('Yes' if H <= sum(A) else 'No')

=======
Suggestion 7

def solve():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    print('Yes' if H <= sum(A) else 'No')

=======
Suggestion 8

def solve():
    h,n = map(int, input().split())
    a = list(map(int, input().split()))
    print('Yes' if h <= sum(a) else 'No')
