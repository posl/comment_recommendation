Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[-1] - A[0])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N-1] - A[0])

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[n-1] - a[0])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_a = max(A)
    min_a = min(A)
    print(max_a - min_a)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            #print(A[i], A[j])
            ans = max(ans, abs(A[i]-A[j]))
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    print(a[-1]-a[0])

=======
Suggestion 7

def main():
    N = int(input())
    A = input().split()
    A = [int(i) for i in A]
    A.sort()
    print(A[-1] - A[0])
