Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))

    a = sorted(a)
    b = sorted(b)
    c = sorted(c)

    count = 0
    for i in range(n):
        count += sum([1 for j in range(n) if a[i] == b[c[j]]])
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort()
    B.sort()
    C.sort()

    #print(A)
    #print(B)
    #print(C)

    count = 0
    for i in range(N):
        a = A[i]
        c = C[i]
        #print(a)
        #print(c)
        #print("-----")
        for j in range(N):
            b = B[j]
            #print(b)
            if a < b and b > c:
                count += 1
                #print("count up")
                #print(count)
                #print("-----")
                break

    print(count)

=======
Suggestion 3

def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # compute
    A.sort()
    B.sort()
    C.sort()
    cnt = 0
    i = 0
    j = 0
    k = 0
    while i<N and j<N and k<N:
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            cnt += 1
            i += 1
            j += 1
    print(cnt)

=======
Suggestion 4

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))

    a_count = [0] * 100001
    c_count = [0] * 100001
    for i in range(n):
        a_count[a_list[i]] += 1
        c_count[c_list[i]] += 1

    b_count = [0] * 100001
    for i in range(n):
        b_count[b_list[c_list[i] - 1]] += 1

    ans = 0
    for i in range(100001):
        ans += a_count[i] * b_count[i]

    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B_C = {}
    for i in range(N):
        if B[i] in B_C:
            B_C[B[i]] += 1
        else:
            B_C[B[i]] = 1

    C_A = {}
    for i in range(N):
        if C[i] in C_A:
            C_A[C[i]] += 1
        else:
            C_A[C[i]] = 1

    ans = 0
    for i in range(N):
        if A[i] in B_C and C[i] in C_A:
            ans += B_C[A[i]] * C_A[C[i]]

    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [int(x) - 1 for x in input().split()]

    d = [0] * n
    for i in range(n):
        d[b[c[i]] - 1] += 1

    ans = 0
    for i in range(n):
        ans += d[a[i] - 1]

    print(ans)

=======
Suggestion 7

def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    from collections import Counter
    A = Counter(A)
    C = Counter(C)

    ans = 0
    for key in A.keys():
        ans += A[key] * C[B[key]]

    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))

    ans = 0
    for i in range(N):
        ans += B.count(C[A[i]-1])
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    cnt = [0 for _ in range(N+1)]
    for i in range(N):
        cnt[B[C[i]-1]] += 1
    ans = 0
    for i in range(N):
        ans += cnt[A[i]]
    print(ans)

=======
Suggestion 10

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # Bの各要素の出現回数を数える
    b_count = {}
    for b in B:
        if b in b_count:
            b_count[b] += 1
        else:
            b_count[b] = 1

    # Aの各要素に対して、b_countの中に対応する要素があれば、その要素の値を出力する
    ans = 0
    for a in A:
        if a in b_count:
            ans += b_count[a]
    print(ans)
