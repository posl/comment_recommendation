Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    return N, K, Q, A, L

=======
Suggestion 2

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = [0] * n
    for i in range(q):
        l[int(input()) - 1] += 1
    for i in range(n):
        if a[i] + l[i] >= q + 1:
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = [0] * n
    for i in range(q):
        l[int(input()) - 1] += 1
    for i in range(n):
        if a[i] + l[i] - q > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = [int(input()) for _ in range(Q)]
    S = [0] * N
    for i in range(Q):
        S[L[i] - 1] += 1
    for i in range(N):
        if K - Q + S[i] > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    result = [0] * N
    for i in range(K):
        result[A[i]-1] += 1
    for i in range(N):
        if result[i] > 0:
            result[i] = result[i] - Q + K
    for i in range(N):
        if result[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    winners = [0] * N
    for i in range(Q):
        winners[L[i]-1] += 1
    for i in range(N):
        if K - Q + winners[i] > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 7

def main():
    n,k,q = map(int, input().split())
    a = [0] * n
    for i in map(int, input().split()):
        a[i-1] += 1
    for i in range(q):
        l = int(input())
        print(k - a[l-1])

=======
Suggestion 8

def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    for i in range(q):
        if l[i] == 1:
            a.sort()
        else:
            a.sort(reverse=True)
        if a[0] == l[i]:
            a[0] = a[1]
        else:
            a[0] = l[i]
    for i in range(k):
        if a[0] == a[i]:
            print(a[0])
        else:
            print(a[1])
main()

=======
Suggestion 9

def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))

    #print("N: {0}, K: {1}, Q: {2}".format(N, K, Q))
    #print("A: {0}".format(A))
    #print("L: {0}".format(L))

    #print("N: {0}, K: {1}, Q: {2}".format(N, K, Q))
    #print("A: {0}".format(A))
    #print("L: {0}".format(L))

    #print("N: {0}, K: {1}, Q: {2}".format(N, K, Q))
    #print("A: {0}".format(A))
    #print("L: {0}".format(L))

    #print("N: {0}, K: {1}, Q: {2}".format(N, K, Q))
    #print("A: {0}".format(A))
    #print("L: {0}".format(L))

    #print("N: {0}, K: {1}, Q: {2}".format(N, K, Q))
    #print("A: {0}".format(A))
    #print("L: {0}".format(L))

    #print("N: {0}, K: {1}, Q: {2}".format(N, K, Q))
    #print("A: {0}".format(A))
    #print("L: {0}".format(L))

    #print("N: {0}, K: {1}, Q: {2}".format(N, K, Q))
    #print("A: {0}".format(A))
    #print("L: {0}".format(L))

    #print("N: {0}, K: {1}, Q: {2}".format(N, K, Q))
    #print("A: {0}".format(A))
    #print("L: {0}".format(L))

    #print("N: {0}, K: {1}, Q: {2}".format(N, K, Q))
    #print("A: {0}".format(A))
    #print("L: {0}".format(L))
    #print("N: {0}, K: {

=======
Suggestion 10

def run():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = []
    for _ in range(q):
        l.append(int(input()))
    s = [0] * n
    for i in range(k):
        s[a[i]-1] += 1
    for i in range(n):
        if s[i] > 0:
            if s[i] - q <= 0:
                print("Yes")
            else:
                print("No")
