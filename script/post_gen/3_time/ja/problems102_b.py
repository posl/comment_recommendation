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
    print(a[-1] - a[0])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[n-1] - a[0])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a) - min(a))

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    print(a[n-1]-a[0])

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[n-1] - a[0])
main()

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    #Aの最大値と最小値を求める
    A_max = max(A)
    A_min = min(A)

    #Aの最大値と最小値の差を求める
    A_diff = A_max - A_min

    print(A_diff)
