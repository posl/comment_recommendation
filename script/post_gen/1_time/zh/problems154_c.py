Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n - 1):
        if a[i] == a[i + 1]:

=======
Suggestion 2

def is_all_different(n, a):
    a.sort()
    for i in range(0, n-1):
        if a[i] == a[i+1]:
            return False
    return True

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    for i in range(n-1):
        if a[i] == a[i+1]:

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    if len(set(A)) == N:
        print("YES")
    else:
        print("NO")

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = set(a)
    if len(a) == len(b):
        print("YES")
    else:
        print("NO")
