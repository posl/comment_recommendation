Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a) - min(a))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A)-min(A))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N-1]-A[0])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    for i in range(n):
        for j in range(i+1,n):
            if max < abs(a[i]-a[j]):
                max = abs(a[i]-a[j])
    print(max)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[n - 1] - a[0])

=======
Suggestion 6

def main():
    n = int(input())
    A = list(map(int,input().split()))
    print(max(A)-min(A))
