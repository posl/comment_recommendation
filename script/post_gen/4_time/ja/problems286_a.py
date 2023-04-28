Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = a[:p-1] + a[r-1:s] + a[q-1:r-1] + a[p-1:q-1] + a[s:]
    print(*b)

=======
Suggestion 2

def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[0:P-1] + A[R-1:S] + A[Q-1:R-1] + A[P-1:Q-1] + A[S:]
    print(*B)

=======
Suggestion 3

def main():
    # N P Q R S
    # A_1 A_2 ... A_N
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))

    # A_1 A_2 ... A_P-1 A_P A_P+1 ... A_Q-1 A_Q A_Q+1 ... A_R-1 A_R A_R+1 ... A_S-1 A_S A_S+1 ... A_N
    # B_1 B_2 ... B_P-1 B_P B_P+1 ... B_Q-1 B_Q B_Q+1 ... B_R-1 B_R B_R+1 ... B_S-1 B_S B_S+1 ... B_N
    # B_1 B_2 ... B_R-1 B_R B_R+1 ... B_S-1 B_S B_S+1 ... B_Q-1 B_Q B_Q+1 ... B_P-1 B_P B_P+1 ... B_N
    B = A[:P-1] + A[R-1:S] + A[Q-1:R-1] + A[P-1:Q-1] + A[S:]
    print(*B)

=======
Suggestion 4

def main():
    N,P,Q,R,S = map(int,input().split())
    A = list(map(int,input().split()))
    B = A.copy()
    for i in range(P-1,Q):
        B[R-1+i-Q] = A[i]
    for i in range(R-1,S):
        B[P-1+i-R] = A[i]
    for i in range(N):
        print(B[i],end=' ')

=======
Suggestion 5

def main():
    n,p,q,r,s = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        if (i+1) >= p and (i+1) <= q:
            b.append(a[i+(s-r)])
        elif (i+1) >= r and (i+1) <= s:
            b.append(a[i-(s-r)])
        else:
            b.append(a[i])
    print(*b)

=======
Suggestion 6

def solve():
    N,P,Q,R,S = map(int,input().split())
    A = list(map(int,input().split()))
    B = A.copy()
    for i in range(P-1,Q):
        B[R-1+i-Q] = A[i]
    for i in range(R-1,S):
        B[P-1+i-R+Q] = A[i]
    print(*B)

=======
Suggestion 7

def swap_list(list, p, q, r, s):
    list[p-1:q], list[r-1:s] = list[r-1:s], list[p-1:q]
    return list

=======
Suggestion 8

def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp
    return arr

=======
Suggestion 9

def swap(array, start, end):
    for i in range(start, end):
        array[i], array[i + 1] = array[i + 1], array[i]

=======
Suggestion 10

def swap(a, b):
    return b, a
