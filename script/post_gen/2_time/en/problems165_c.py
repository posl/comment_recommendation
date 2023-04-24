Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, Q = map(int, input().split())
    a = [0] * Q
    b = [0] * Q
    c = [0] * Q
    d = [0] * Q
    for i in range(Q):
        a[i], b[i], c[i], d[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
    ans = 0
    A = [0] * N
    def dfs(x):
        global ans
        if x == N:
            score = 0
            for i in range(Q):
                if A[b[i]] - A[a[i]] == c[i]:
                    score += d[i]
            ans = max(ans, score)
            return
        for i in range(A[x - 1], M + 1):
            A[x] = i
            dfs(x + 1)
    dfs(0)
    print(ans)

=======
Suggestion 2

def solve():
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(Q)]
    ans = 0
    def dfs(A):
        global ans
        if len(A) == N:
            score = 0
            for a, b, c, d in abcd:
                if A[b-1] - A[a-1] == c:
                    score += d
            ans = max(ans, score)
        else:
            for i in range(A[-1], M+1):
                dfs(A + [i])
    dfs([1])
    print(ans)

=======
Suggestion 3

def   main ():
    n ,  m ,  q  =  map ( int ,  input (). split ())
    abcd  =  [ list ( map ( int ,  input (). split ()))  for  _  in   range ( q )]

    ans  =   0 
     for  a  in   range ( 1 ,  m  +   1 ):
        A  =   [ a ]  +   [ 0 ] * ( n  -   1 )
         for  i  in   range ( 1 ,  n ):
            A [ i ]  =   max ( A [ i - 1 ],  m  -  ( n  -  i ))
             if  A [ i ]  ==  m  -  ( n  -  i ):
                 break 
         for  b  in   range ( A [ i ],  m  +   1 ):
            A [ i ]  =  b
             for  j  in   range ( i + 1 ,  n ):
                A [ j ]  =   max ( A [ j - 1 ],  m  -  ( n  -  j ))
                 if  A [ j ]  ==  m  -  ( n  -  j ):
                     break 
             for  c  in   range ( A [ j ],  m  +   1 ):
                A [ j ]  =  c
                 for  k  in   range ( j + 1 ,  n ):
                    A [ k ]  =   max ( A [ k - 1 ],  m  -  ( n  -  k ))
                     if  A [ k ]  ==  m  -  ( n  -  k ):
                         break 
                 for  d  in   range ( A [ k ],  m  +   1 ):
                    A [ k ]  =  d
                    score  =   0 
                     for  a_i ,  b_i ,  c_i ,  d_i  in  abcd:
                         if  A [ b_i  -   1 ]  -  A [ a_i  -   1 ]  ==  c_i:
                            score  +=  d_i
                    ans  =   max ( ans ,  score )
    print ( ans )

=======
Suggestion 4

def main():
    N, M, Q = map(int, input().split())
    questions = [list(map(int, input().split())) for _ in range(Q)]
    print(solver(N, M, Q, questions))

=======
Suggestion 5

def main():
    N, M, Q = map(int, input().split())
    A = [0] * N
    A[0] = 1
    A[-1] = M
    for i in range(N - 2):
        A[i + 1] = M - N + 2 + i
    max_score = 0
    while True:
        score = 0
        for i in range(Q):
            a, b, c, d = map(int, input().split())
            if A[b - 1] - A[a - 1] == c:
                score += d
        max_score = max(max_score, score)
        if not next_permutation(A):
            break
    print(max_score)

=======
Suggestion 6

def main():
    N, M, Q = map(int, input().split())
    A = [0] * (N + 1)
    d = [0] * (N + 1)
    for i in range(Q):
        a, b, c, dd = map(int, input().split())
        if A[a] == 0:
            A[a] = c
            d[a] = dd
        else:
            if A[a] > c:
                A[a] = c
                d[a] = dd
    print(A)
    print(d)

=======
Suggestion 7

def main():
    N, M, Q = map(int, input().split())
    A = [1] * N
    ans = 0
    def dfs(i):
        nonlocal ans
        if i == N:
            score = 0
            for a, b, c, d in abcd:
                if A[b - 1] - A[a - 1] == c:
                    score += d
            ans = max(ans, score)
            return
        for j in range(A[i - 1], M + 1):
            A[i] = j
            dfs(i + 1)
    abcd = [list(map(int, input().split())) for _ in range(Q)]
    dfs(1)
    print(ans)

=======
Suggestion 8

def main():
    N, M, Q = map(int, input().split())
    # print(N, M, Q)
    quad = []
    for i in range(Q):
        quad.append(list(map(int, input().split())))
    # print(quad)
    ans = 0
    for i in range(M):
        A = [i+1]
        ans = max(ans, dfs(N, M, Q, quad, A))
    print(ans)

=======
Suggestion 9

def main():
    N, M, Q = map(int, input().split())
    A = [0] * N
    A[0] = 1
    A[N-1] = M
    print(A)
    # for i in range(Q):
    #     a, b, c, d = map(int, input().split())
    #     if A[b-1] - A[a-1] == c:
    #         score += d
    # print(score)

=======
Suggestion 10

def read_int():
    return int(input())
