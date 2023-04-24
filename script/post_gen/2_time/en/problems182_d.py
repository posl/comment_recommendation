Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        if A[0] >= 0:
            print(A[0])
        else:
            print(0)
    else:
        if A[0] < 0:
            A[0] = 0
        for i in range(1, N):
            A[i] += A[i-1]
            if A[i] < 0:
                A[i] = 0
        print(max(A))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    tmp = 0
    for i in range(N):
        tmp += A[i]
        ans = max(ans, tmp)
        if ans < 0:
            ans = 0
        if tmp < 0:
            tmp = 0
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
        if ans < 0:
            ans = 0
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #A = [2, -1, -2]
    #A = [-2, 1, 3, -1, -1]
    #A = [-1000, -1000, -1000, -1000, -1000]
    #A = [2, -1, -2]
    #A = [-2, 1, 3, -1, -1]
    #A = [-1000, -1000, -1000, -1000, -1000]
    #A = [-2, 1, 3, -1, -1]
    #A = [-1000, -1000, -1000, -1000, -1000]
    #A = [-2, 1, 3, -1, -1]
    #A = [-1000, -1000, -1000, -1000, -1000]
    #A = [-2, 1, 3, -1, -1]
    #A = [-1000, -1000, -1000, -1000, -1000]
    #A = [-2, 1, 3, -1, -1]
    #A = [-1000, -1000, -1000, -1000, -1000]
    #A = [-2, 1, 3, -1, -1]
    #A = [-1000, -1000, -1000, -1000, -1000]
    #A = [-2, 1, 3, -1, -1]
    #A = [-1000, -1000, -1000, -1000, -1000]
    #A = [-2, 1, 3, -1, -1]
    #A = [-1000, -1000, -1000, -1000, -1000]
    #A = [-2, 1, 3, -1, -1]
    #A = [-1000, -1000, -1000, -1000, -1000]
    #A = [-2, 1, 3, -1, -1]
    #A = [-100

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max = 0
    sum = 0
    for i in range(N):
        sum += A[i]
        if sum > max:
            max = sum
    print(max)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    pos = 0
    neg = 0
    for i in range(n):
        if a[i] >= 0:
            pos += a[i]
        else:
            neg += a[i]
    print(pos - neg)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    total = 0
    max_total = 0
    for i in range(N):
        total += A[i]
        if total > max_total:
            max_total = total
    print(max_total)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if sum(A) <= 0:
        print(0)
    else:
        print(sum(A) - min([a for a in A if a < 0]))

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if sum(A) <= 0:
        print(0)
        return
    for i in range(1, N):
        A[i] += A[i-1]
    print(max(A))

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [2, -1, -2]
    # A = [-2, 1, 3
