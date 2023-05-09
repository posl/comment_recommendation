Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        x, k = map(int, input().split())
        count = 0
        for j in range(n):
            if a[j] == x:
                count += 1
            if count == k:
                print(j+1)
                break
        else:
            print(-1)

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(q):
        x, k = map(int, input().split())
        cnt = 0
        for i in range(n):
            if a[i] == x:
                cnt += 1
            if cnt == k:
                print(i+1)
                break
        else:
            print(-1)

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        x, k = map(int, input().split())
        count = 0
        for j in range(N):
            if A[j] == x:
                count += 1
            if count == k:
                print(j+1)
                break
        else:
            print(-1)

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        x, k = map(int, input().split())
        if a.count(x) < k:
            print(-1)
        else:
            print(a.index(x, k-1) + 1)

=======
Suggestion 5

def get_input():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    queries = []
    for _ in range(Q):
        queries.append(tuple(map(int, input().split())))
    return N, Q, A, queries

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(Q):
        x, k = map(int, input().split())
        kth = 0
        for i in range(N):
            if A[i] == x:
                kth += 1
            if kth == k:
                print(i+1)
                break
        else:
            print(-1)

=======
Suggestion 7

def solve(n, q, a, x, k):
    result = []
    for i in range(q):
        count = 0
        for j in range(n):
            if a[j] == x[i]:
                count += 1
            if count == k[i]:
                result.append(j+1)
                break
        if count < k[i]:
            result.append(-1)
    return result

=======
Suggestion 8

def solve(n, q, a, xk):
    #print("n: {}, q: {}, a: {}, xk: {}".format(n, q, a, xk))
    #print("a: {}".format(a))
    #print("xk: {}".format(xk))
    #print("xk[0]: {}".format(xk[0]))
    #print("xk[0][0]: {}".format(xk[0][0]))
    #print("xk[0][1]: {}".format(xk[0][1]))
    #print("xk[1]: {}".format(xk[1]))
    #print("xk[1][0]: {}".format(xk[1][0]))
    #print("xk[1][1]: {}".format(xk[1][1]))
    #print("xk[2]: {}".format(xk[2]))
    #print("xk[2][0]: {}".format(xk[2][0]))
    #print("xk[2][1]: {}".format(xk[2][1]))
    #print("xk[3]: {}".format(xk[3]))
    #print("xk[3][0]: {}".format(xk[3][0]))
    #print("xk[3][1]: {}".format(xk[3][1]))
    #print("xk[4]: {}".format(xk[4]))
    #print("xk[4][0]: {}".format(xk[4][0]))
    #print("xk[4][1]: {}".format(xk[4][1]))
    #print("xk[5]: {}".format(xk[5]))
    #print("xk[5][0]: {}".format(xk[5][0]))
    #print("xk[5][1]: {}".format(xk[5][1]))
    #print("xk[6]: {}".format(xk[6]))
    #print("xk[6][0]: {}".format(xk[6][0]))
    #print("xk[6][1]: {}".format(xk[6][1]))
    #print("xk[7]: {}".format(xk[7]))
    #print("xk[7][0]: {}".format(xk[7][0]))
    #print("xk[7][1]: {}".format
