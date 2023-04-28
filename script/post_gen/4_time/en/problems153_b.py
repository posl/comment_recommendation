Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if H <= sum(A):
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) >= h:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    H, N = map(int, input().split())
    A = map(int, input().split())
    if H <= sum(A):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    h, n = map(int, input().split())
    a = map(int, input().split())
    if h <= sum(a):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def solve():
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
    A = map(int, input().split())
    print('Yes' if H <= sum(A) else 'No')

=======
Suggestion 7

def main():
    h, n = map(int, input().split())
    arr = list(map(int, input().split()))

    if h <= sum(arr):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    H,N = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    if H <= sum(A):
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    h, n = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))
    a.sort()
    a.reverse()
    for i in range(n):
        h -= a[i]
        if h <= 0:
            print('Yes')
            return
    print('No')
