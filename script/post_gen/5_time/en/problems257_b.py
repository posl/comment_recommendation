Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    S = [0] * N
    for i in range(Q):
        S[L[i] - 1] += 1
    for i in range(N):
        if K - Q + S[i] > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 2

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = [int(input()) for _ in range(Q)]
    S = [0] * N
    for a in A:
        S[a-1] += 1
    for l in L:
        print(K - (Q - S[l-1]))

=======
Suggestion 3

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    p = [0] * n
    for i in range(q):
        p[l[i] - 1] += 1
    for i in range(n):
        if a[i] - q + sum(p) > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = [int(input()) for _ in range(Q)]
    P = [0] * N
    for a in A:
        P[a-1] += 1
    for l in L:
        print(K - (Q - P[l-1]))

=======
Suggestion 5

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))

    cnt = [0] * N
    for i in range(Q):
        cnt[L[i] - 1] += 1

    for i in range(N):
        if K - Q + cnt[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = [int(input()) for i in range(q)]
    c = [0 for i in range(n)]
    for i in range(q):
        c[l[i]-1] += 1
    for i in range(n):
        if k - q + c[i] > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 7

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = []
    for i in range(q):
        l.append(int(input()))
    # print(n, k, q)
    # print(a)
    # print(l)
    ans = [0] * n
    for i in range(q):
        ans[l[i] - 1] += 1
    # print(ans)
    for i in range(n):
        if k - (q - ans[i]) > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    # input
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))

    # compute
    score = [0] * N
    for i in range(Q):
        score[L[i] - 1] += 1
    for i in range(N):
        score[i] += K - Q
    for i in range(N):
        if score[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    B = [0] * (N)
    for i in range(Q):
        B[L[i]-1] += 1
    for i in range(N):
        if (K - Q + B[i]) > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def main():
    n,k,q = map(int, input().split())
    a = list(map(int, input().split()))
    l = [int(input()) for i in range(q)]

    #print(n,k,q)
    #print(a)
    #print(l)

    #print(n,k,q)
    #print(a)
    #print(l)

    #a = [1,3,4]
    #l = [3,3,1,1,2]

    #n = 5
    #k = 3
    #q = 5

    #a = [1,3,4]
    #l = [3,3,1,1,2]

    #n = 2
    #k = 2
    #q = 2

    #a = [1,2]
    #l = [1,2]

    #n = 10
    #k = 6
    #q = 9

    #a = [1,3,5,7,8,9]
    #l = [1,2,3,4,5,6,5,6,2]

    #n = 3
    #k = 3
    #q = 3

    #a = [1,2,3]
    #l = [1,2,3]

    #n = 3
    #k = 2
    #q = 3

    #a = [2,3]
    #l = [1,2,1]

    #n = 3
    #k = 2
    #q = 3

    #a = [1,3]
    #l = [1,2,1]

    #n = 3
    #k = 2
    #q = 3

    #a = [1,2]
    #l = [1,2,1]

    #n = 3
    #k = 2
    #q = 3

    #a = [1,2]
    #l = [2,2,1]

    #n = 3
    #k = 2
    #q = 3

    #a = [1,2]
    #l = [1,1,1]

    #n = 3
