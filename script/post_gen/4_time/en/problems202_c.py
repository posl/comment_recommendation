Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))

    a_count = [0] * n
    for i in range(n):
        a_count[a[i] - 1] += 1

    c_count = [0] * n
    for i in range(n):
        c_count[c[i]] += 1

    count = 0
    for i in range(n):
        count += a_count[i] * c_count[i]

    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x)-1, input().split()))
    d = [0]*n
    for i in range(n):
        d[b[c[i]]] += 1
    ans = 0
    for i in range(n):
        ans += d[a[i]]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    #print(N)
    #print(A)
    #print(B)
    #print(C)

    # create a dictionary with keys as the values in C and values as the count of each value
    C_dict = {}
    for c in C:
        if c in C_dict:
            C_dict[c] += 1
        else:
            C_dict[c] = 1

    #print(C_dict)

    # create a dictionary with keys as the values in B and values as the count of each value
    B_dict = {}
    for b in B:
        if b in B_dict:
            B_dict[b] += 1
        else:
            B_dict[b] = 1

    #print(B_dict)

    # create a dictionary with keys as the values in A and values as the count of each value
    A_dict = {}
    for a in A:
        if a in A_dict:
            A_dict[a] += 1
        else:
            A_dict[a] = 1

    #print(A_dict)

    count = 0
    for key in C_dict.keys():
        if key in B_dict.keys():
            count += C_dict[key] * B_dict[key]

    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    #print(N, A, B, C)

    count = 0
    for i in range(N):
        count += B[C[i]-1] == A[i]
    print(count)

=======
Suggestion 5

def p202_c():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))
    d = [0] * n
    for i in range(n):
        d[c[i]] += 1
    ans = 0
    for i in range(n):
        ans += d[b[a[i] - 1] - 1]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B_C = [0]*N
    for i in range(N):
        B_C[C[i]-1] += 1

    ans = 0
    for i in range(N):
        ans += B_C[B[A[i]-1]-1]

    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B = [B[C[i]-1] for i in range(N)]

    A.sort()
    B.sort()

    count = 0
    i = 0
    j = 0
    while i < N and j < N:
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            count += 1
            i += 1
            j += 1
    print(count)

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A = [a-1 for a in A]
    B = [b-1 for b in B]
    C = [c-1 for c in C]

    count = [0] * N
    for c in C:
        count[B[c]] += 1

    print(sum([count[a] for a in A]))

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    print(sum([B[C[i]-1] == A[i] for i in range(N)]))

=======
Suggestion 10

def solve(n, a, b, c):
    ans = 0
    d = {}
    for i in range(n):
        if c[b[i]-1] in d:
            d[c[b[i]-1]] += 1
        else:
            d[c[b[i]-1]] = 1

    for i in range(n):
        if a[i] in d:
            ans += d[a[i]]

    return ans
