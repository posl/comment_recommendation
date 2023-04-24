Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, p, q, r, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = a[:p-1] + a[r-1:s] + a[q-1:r-1] + a[p-1:q-1] + a[s:]
    print(' '.join(map(str, b)))

=======
Suggestion 2

def main():
    N,P,Q,R,S = map(int,input().split())
    A = list(map(int,input().split()))
    B = A[:P-1] + A[R-1:S] + A[P-1:R-1] + A[S:]
    print(' '.join(map(str,B)))

=======
Suggestion 3

def main():
    N,P,Q,R,S = map(int,input().split())
    A = list(map(int,input().split()))
    B = A[P-1:Q] + A[R-1:S]
    A[P-1:Q] = A[R-1:S]
    A[R-1:S] = B
    for i in range(N):
        print(A[i],end=" ")
    print()

=======
Suggestion 4

def main():
    n,p,q,r,s = map(int,input().split())
    a = list(map(int,input().split()))
    b = a[0:p-1] + a[r-1:s] + a[q-1:r-1] + a[p-1:q-1] + a[s:n]
    print(' '.join(map(str,b)))

=======
Suggestion 5

def main():
    n,p,q,r,s = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        if p <= i+1 <= q:
            b.append(a[r-1+i-q])
        elif r <= i+1 <= s:
            b.append(a[p-1+i-r])
        else:
            b.append(a[i])
    print(*b)

=======
Suggestion 6

def swap_array(array, p, q, r, s):
    array[p-1:q], array[r-1:s] = array[r-1:s], array[p-1:q]
    return array

=======
Suggestion 7

def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))

    # 1. P-QとR-Sを入れ替える
    # 2. P-RとQ-Sを入れ替える
    # 3. P-SとQ-Rを入れ替える
    # という操作を行う
    # つまり、PとQを入れ替えた後、QとRを入れ替えた後、RとSを入れ替えた後、PとSを入れ替える
    # これで、P-QとR-Sが入れ替わる
    # これを、P-QとR-Sが入れ替わるまで繰り返す
    while P < Q and R < S:
        # 1
        for i in range(P-1, Q-1):
            A[i], A[i+1] = A[i+1], A[i]
        # 2
        for i in range(Q-1, R-1):
            A[i], A[i+1] = A[i+1], A[i]
        # 3
        for i in range(R-1, S-1):
            A[i], A[i+1] = A[i+1], A[i]
        # 4
        for i in range(P-1, S-1):
            A[i], A[i+1] = A[i+1], A[i]
    print(*A)

=======
Suggestion 8

def swap(arr, p, q, r, s):
    #print(arr)
    #print(p, q, r, s)
    #print(arr[p-1:q])
    #print(arr[r-1:s])
    tmp = arr[p-1:q]
    arr[p-1:q] = arr[r-1:s]
    arr[r-1:s] = tmp
    return arr

=======
Suggestion 9

def swapList(numList, start, end):
    tmpList = numList[start:end]
    tmpList.reverse()
    numList = numList[:start] + tmpList + numList[end:]
    return numList

=======
Suggestion 10

def swap_array(a, b, c, d, e):
    for i in range(0, e):
        if i >= b and i <= c:
            a[i], a[d+i-b] = a[d+i-b], a[i]
    return a
