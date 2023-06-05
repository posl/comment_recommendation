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
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[-1] - a[0])

=======
Suggestion 3

def max_diff(a_list):
    max_num = max(a_list)
    min_num = min(a_list)
    return max_num - min_num

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_num = max(a)
    min_num = min(a)
    print(max_num - min_num)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A)-min(A))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max = 0
    for i in range(0, N):
        for j in range(i+1, N):
            if abs(A[i] - A[j]) > max:
                max = abs(A[i] - A[j])
    print(max)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max = 0
    for i in range(N):
        for j in range(i+1, N):
            if abs(A[i] - A[j]) > max:
                max = abs(A[i] - A[j])
    print(max)
