Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    d = [0] * K
    A = [0] * K
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if (i + 1) not in A[0]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    snuke = [0] * n
    for _ in range(k):
        d = int(input())
        a = list(map(int, input().split()))
        for i in range(d):
            snuke[a[i]-1] += 1
    print(snuke.count(0))

=======
Suggestion 3

def problems166_b():
    N, K = map(int, input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))
    S = set()
    for i in range(K):
        for j in range(d[i]):
            S.add(A[i][j])
    print(N - len(S))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = [0] * N
    for i in range(K):
        d = int(input())
        A_i = list(map(int, input().split()))
        for j in range(d):
            A[A_i[j] - 1] += 1
    print(A.count(0))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    s = set()
    for _ in range(k):
        d = int(input())
        a = set(map(int, input().split()))
        s |= a

    print(n - len(s))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(list(map(int, input().split()))[1:])
    d = sum(d, [])
    print(N - len(set(d)))

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = [0] * N
    for i in range(K):
        d = int(input())
        A[:d] = list(map(int, input().split()))
    print(N - len(set(A)))

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = [0]*N
    for i in range(K):
        d = int(input())
        A[i] = list(map(int, input().split()))
    print(N - len(set(sum(A, []))))

=======
Suggestion 9

def main():
    n,k = map(int, input().split())
    a = [0]*n
    for i in range(k):
        d = int(input())
        a += list(map(int, input().split()))

    print(n-len(set(a)))

=======
Suggestion 10

def main():
    input = raw_input().split()
    N = int(input[0])
    K = int(input[1])
    A = []
    for i in range(0, K):
        input2 = raw_input().split()
        A.append(input2[1:])
    A = [int(i) for j in A for i in j]
    print N - len(set(A))
