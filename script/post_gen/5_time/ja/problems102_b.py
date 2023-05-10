Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a)-min(a))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[-1]-a[0])

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
    n = int(input())
    a_list = list(map(int, input().split()))
    a_max = max(a_list)
    a_min = min(a_list)
    print(a_max - a_min)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    min_a = min(a)
    print(max_a - min_a)

=======
Suggestion 6

def main():
    # 整数の入力
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a)-min(a))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A)-min(A))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N-1]-A[0])
