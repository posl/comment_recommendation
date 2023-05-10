Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    d = [0] * k
    a = [0] * k
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int, input().split()))
    ans = 0
    for i in range(1, n+1):
        flag = True
        for j in range(k):
            if i in a[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    cnt = 0
    for i in range(1, n + 1):
        for j in range(k):
            if i in a[j]:
                break
        else:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(K):
            if i+1 in A[j]:
                break
        else:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(k):
            if i+1 in a[j]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        A.append(list(map(int, input().split())))
    B = [0] * N
    for i in range(K):
        for j in range(A[i][0]):
            B[A[i][j+1]-1] += 1
    ans = 0
    for i in range(N):
        if B[i] == 0:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    cnt = 0
    for i in range(k):
        d = int(input())
        A = list(map(int, input().split()))
        for j in range(d):
            if A[j] == i+1:
                cnt += 1
    print(n - cnt)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    #print(d)
    #print(a)
    ans = 0
    for i in range(n):
        if i+1 not in a[0]:
            ans += 1
    print(ans)

=======
Suggestion 8

def solve():
    N,K = map(int,input().split())
    d = [0]*K
    A = [0]*K
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int,input().split()))

    cnt = 0
    for i in range(N):
        for j in range(K):
            if i+1 in A[j]:
                break
        else:
            cnt += 1

    print(cnt)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    D = []
    A = []
    for i in range(K):
        D.append(int(input()))
        A.append(list(map(int, input().split())))
    S = set()
    for i in range(K):
        S |= set(A[i])
    print(N - len(S))

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    print(n - len(set([a[j][i] for j in range(k) for i in range(d[j])])))
