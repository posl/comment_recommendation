Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))

    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1

    ans = 0
    for i in range(n):
        for j in range(n):
            if a[i] % a[j] != 0:
                continue
            k = a[i] // a[j]
            if k in d:
                ans += d[k]

    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    for i in range(N):
        for j in range(N):
            if A[j] == 0:
                continue
            if A[i] % A[j] == 0:
                if A[i] // A[j] in d:
                    cnt += d[A[i] // A[j]]
    print(cnt)

=======
Suggestion 3

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    for i in range(n):
        for j in range(n):
            if a[i] == a[j]:
                continue
            if a[i] % a[j] != 0:
                continue
            if a[i] // a[j] not in d:
                continue
            cnt += d[a[i] // a[j]]
    print(cnt)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    cnt = [0] * (10**6+1)
    for i in range(N):
        ans += cnt[A[i]]
        cnt[A[i]] += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if A[i] == A[j]:
                continue
            if A[i] % A[j] != 0:
                continue
            if A[i] // A[j] in A:
                cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A_set = set(A)
    A_dict = {}
    for i in range(N):
        if A[i] not in A_dict:
            A_dict[A[i]] = []
        A_dict[A[i]].append(i)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i]*A[j] in A_set:
                ans += len(A_dict[A[i]*A[j]])
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    b = [0]*(n+1)
    for i in range(n):
        b[a[i]] += 1
    c = [0]*(n+1)
    for i in range(1,n+1):
        c[i] = c[i-1]+b[i]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i]*a[j] > n:
                break
            else:
                ans += c[n//a[i]//a[j]]
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.insert(0, 0)
    A.append(0)
    L = 0
    R = 0
    ans = 0
    for i in range(1, N+1):
        for j in range(i+1, N+2):
            while A[L] * A[j] < A[i] * A[R]:
                L += 1
            while A[L] * A[j] > A[i] * A[R]:
                R += 1
            if A[L] * A[j] == A[i] * A[R]:
                ans += R - L
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()

    #print(A)

    # 1 ≦ i, j, k ≦ N
    # ((A_i)/(A_j)) = A_k
    # 1 ≦ A_i ≦ 2 × 10^5  (1 ≦ i ≦ N)

    # 1 ≦ A_i ≦ 2 × 10^5  (1 ≦ i ≦ N)
    # 1 ≦ A_i ≦ 10^5  (1 ≦ i ≦ N)
    # 1 ≦ A_i ≦ 10^5  (1 ≦ i ≦ N)
    # 1 ≦ A_i ≦ 10^5  (1 ≦ i ≦ N)
    # 1 ≦ A_i ≦ 10^5  (1 ≦ i ≦ N)

    # 1 ≦ A_i ≦ 10^5  (1 ≦ i ≦ N)
    # 1 ≦ A_i ≦ 10^5  (1 ≦ i ≦ N)
    # 1 ≦ A_i ≦ 10^5  (1 ≦ i ≦ N)
    # 1 ≦ A_i ≦ 10^5  (1 ≦ i ≦ N)
    # 1 ≦ A_i ≦ 10^5  (1 ≦ i ≦ N)

    # 1 ≦ A_i ≦ 10^5  (1 ≦ i ≦ N)
    # 1 ≦ A_i ≦ 10^5  (1 ≦ i ≦ N)

    # 1 ≦ A_i ≦ 10^5  (1 ≦ i ≦ N)
    # 1 ≦ A_i ≦ 10^5  (1 ≦ i ≦ N)

    # 1 ≦ A_i ≦ 10^5  (1 ≦ i ≦ N)
    # 1 ≦ A_i ≦ 10^5  (1 ≦ i ≦ N)

    # 1 ≦ A_i ≦ 10^5  (1 ≦ i ≦ N)
    #

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print('-----')

    #A.sort()
    #print(A)

    #A.sort()
    #print(A)
    #pri
