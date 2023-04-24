Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    d = [0] * K
    A = [0] * K
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    ans = 0
    for i in range(1, N + 1):
        flag = 0
        for j in range(K):
            if i in A[j]:
                flag = 1
                break
        if flag == 0:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = [0] * N
    for i in range(K):
        d = int(input())
        for j in map(int, input().split()):
            A[j-1] = 1
    print(A.count(0))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    d = [0] * K
    A = [[0] * N for _ in range(K)]
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(K):
            if i+1 in A[j]:
                ans += 1
                break
    print(N - ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    d = [0] * n
    for i in range(k):
        for j in map(int, input().split()[1:]):
            d[j - 1] += 1
    print(d.count(0))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        d = int(input())
        A += list(map(int, input().split()))
    print(N - len(set(A)))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        d = int(input())
        A.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, N+1):
        for j in range(K):
            if i in A[j]:
                ans += 1
                break
    print(N - ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    d = [0 for i in range(N)]
    for i in range(K):
        d_i = int(input())
        for j in range(d_i):
            d[int(input()) - 1] += 1
    print(d.count(0))

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(int(input()))
        A = list(map(int, input().split()))
        d.append(A)
    #print(d)

    ans = 0
    for i in range(1, N + 1):
        for j in range(0, len(d), 2):
            if i in d[j + 1]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(input())
    A = []
    for i in range(K):
        A.append(input().split())
    d = [int(i) for i in d]
    A = [[int(j) for j in i] for i in A]
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] -= 1
    a = []
    for i in range(len(A)):
        for j in range(len(A[i])):
            a.append(A[i][j])
    a = list(set(a))
    print(N - len(a))
