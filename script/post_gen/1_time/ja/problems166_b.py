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
    for i in range(n):
        flag = 0
        for j in range(k):
            if i+1 in a[j]:
                flag = 1
        if flag == 0:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    d = [0] * k
    a = [0] * k
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int, input().split()))
    #print(n, k, d, a)
    s = set()
    for i in range(k):
        for j in range(d[i]):
            s.add(a[i][j])
    print(n - len(s))

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    cnt = 0
    for i in range(n):
        for j in range(k):
            if i+1 in a[j]:
                break
        else:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    D = []
    A = []
    for i in range(K):
        d = int(input())
        D.append(d)
        A.append(list(map(int, input().split())))

    result = N
    for i in range(K):
        for j in range(D[i]):
            if A[i][j] == result:
                result -= 1
                break

    print(result)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(K):
            if i+1 in A[j]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    # input
    N, K = map(int, input().split())
    d = [0] * K
    A = [[] for _ in range(K)]
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    # compute
    count = 0
    for i in range(N):
        flag = True
        for j in range(K):
            if i+1 in A[j]:
                flag = False
        if flag:
            count += 1
    # output
    print(count)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = []
    for i in range(k):
        d = int(input())
        a.extend(map(int, input().split()))
    a = set(a)
    print(n - len(a))

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    d = [0] * N
    for _ in range(K):
        A = list(map(int, input().split()))
        for i in range(1, len(A)):
            d[A[i]-1] += 1
    ans = 0
    for i in range(N):
        if d[i] == 0:
            ans += 1
    print(ans)
    return 0

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    a = [0 for _ in range(n + 1)]
    for _ in range(k):
        d = int(input())
        for i in map(int, input().split()):
            a[i] += 1
    print(a.count(0) - 1)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    d = {}
    for i in range(1, K+1):
        d[i] = list(map(int, input().split()[1:]))
    count = 0
    for i in range(1, N+1):
        if i not in d.values():
            count += 1
    print(count)
