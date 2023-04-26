Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[:P-1] + A[R-1:S] + A[Q-1:R-1] + A[S:]
    print(*B)

main()

=======
Suggestion 2

def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[:P-1] + A[R-1:S] + A[Q-1:R-1] + A[P-1:Q-1] + A[S:]
    print(*B)

=======
Suggestion 3

def main():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = a[p-1:q] + a[r-1:s]
    for i in range(n):
        if i < p-1 or s <= i:
            b.append(a[i])
    print(*b)

=======
Suggestion 4

def main():
    N,P,Q,R,S = map(int,input().split())
    A = list(map(int,input().split()))
    B = A[:P-1]+A[R-1:S]+A[Q:S-1]+A[P-1:Q-1]+A[S:]
    print(*B)

=======
Suggestion 5

def main():
    n,p,q,r,s = map(int,input().split())
    a = list(map(int,input().split()))
    b = a[p-1:q] + a[r-1:s]
    c = a[:p-1] + a[q:r-1] + a[s:]
    c = c[::-1]
    c = c[:p-1] + b + c[p-1:]
    for i in c:
        print(i,end=" ")

=======
Suggestion 6

def swap(a, p, q, r, s):
    a[p-1:q], a[r-1:s] = a[r-1:s], a[p-1:q]
    return a

n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))
b = swap(a, p, q, r, s)
print(*b)

=======
Suggestion 7

def main():
    N,P,Q,R,S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A.copy()
    for i in range(N):
        if i+1 >= P and i+1 <= Q:
            B[i] = A[i+(S-R)]
        elif i+1 >= R and i+1 <= S:
            B[i] = A[i-(S-R)]
    print(*B)

=======
Suggestion 8

def main():
    n,p,q,r,s = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0]*n
    for i in range(n):
        if i+1 in range(p,q+1):
            b[i] = a[i+r-q-1]
        elif i+1 in range(r,s+1):
            b[i] = a[i+q-p+1]
        else:
            b[i] = a[i]
    print(*b)

=======
Suggestion 9

def swap(a, b):
    a, b = b, a
    return a, b

=======
Suggestion 10

def input_to_list():
    return list(map(int, input().split()))
