Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    K = [0] * (n + 1)

    for i in range(n):
        K[i + 1] = K[i] + (A[i] != A[i - 1]) # K[i]是A中小于A[i]的不同的整数的个数
    for i in range(1, n + 1):
        print(K[i])

=======
Suggestion 2

def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    n = 10
    a = [979861204, 57882493, 979861204, 447672230, 644706927, 710511029, 763027379, 710511029, 447672230, 136397527]
    #n = 6
    #a = [2, 7, 1, 8, 2, 8]
    #n = 1
    #a = [1]
    #n = 3
    #a = [1, 2, 3]
    #n = 3
    #a = [1, 1, 1]
    #n = 3
    #a = [1, 2, 1]
    #n = 3
    #a = [1, 2, 2]
    #n = 3
    #a = [2, 1, 1]
    #n = 3
    #a = [2, 1, 2]
    #n = 3
    #a = [2, 2, 1]
    #n = 3
    #a = [2, 2, 2]
    #n = 3
    #a = [1, 2, 3]
    #n = 3
    #a = [3, 2, 1]
    #n = 3
    #a = [1, 2, 1]
    #n = 3
    #a = [1, 2, 2]
    #n = 3
    #a = [2, 1, 1]
    #n = 3
    #a = [2, 1, 2]
    #n = 3
    #a = [2, 2, 1]
    #n = 3
    #a = [2, 2, 2]
    #n = 3
    #a = [1, 1, 1]
    #n = 3
    #a = [1, 1, 2]
    #n = 3
    #a = [1, 2,

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    count = 0
    for i in range(n):
        if i == 0 or a[i] != a[i-1]:
            count = 1
        else:
            count += 1
        print(n - count)

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    count = 0
    for i in range(N):
        if i == 0:
            print(0)
            continue
        elif A[i] == A[i-1]:
            print(count)
            continue
        else:
            count += 1
            print(count)
            continue

=======
Suggestion 5

def count(K, A):
    A.sort()
    count = 0
    for i in range(len(A)):
        if A[i] > A[K]:
            count += 1
    return count

N = int(input())
A = [int(i) for i in input().split()]
for i in range(N):
    print(count(i, A))

=======
Suggestion 6

def main():
    n = int(input())
    A = list(map(int, input().split()))
    A_set = set(A)
    A.sort()
    A_dict = {}
    for i in range(n):
        A_dict[A[i]] = i
    for i in range(n):
        cnt = 0
        for j in range(A_dict[A[i]]):
            if A[j] > A[i]:
                cnt += 1
        print(cnt)

=======
Suggestion 7

def solve():
    pass

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    ans = [0] * n
    ans[0] = 1
    cnt = 1
    for i in range(1, n):
        if a[i] != a[i-1]:
            cnt += 1
        ans[i] = cnt
    for i in range(n):
        print(ans[i])

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    for i in range(n):
        ans[i] = min(i, n - i - 1)
    for i in range(1, n):
        if a[i] == a[i - 1]:
            ans[i] = ans[i - 1]
    for i in range(n - 2, -1, -1):
        if a[i] == a[i + 1]:
            ans[i] = ans[i + 1]
    for i in range(n):
        print(ans[i])

=======
Suggestion 10

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        for j in range(i, N):
            if A[i] < A[j]:
                ans[i] += 1
    for i in range(N):
        print(ans[i])
