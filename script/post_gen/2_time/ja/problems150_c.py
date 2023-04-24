Synthesizing 10/10 solutions

=======
Suggestion 1

def   main (): 
     n   =   int ( input ()) 
     p   =   list ( map ( int ,   input (). split ())) 
     q   =   list ( map ( int ,   input (). split ())) 
     from   itertools   import   permutations 
     x   =   0 
     y   =   0 
     for   i ,   j   in   enumerate ( permutations ( range ( 1 ,   n   +   1 ))): 
         if   list ( j )   ==   p : 
             x   =   i 
         if   list ( j )   ==   q : 
             y   =   i 
     print ( abs ( x   -   y ))

=======
Suggestion 2

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    P = [x - 1 for x in P]
    Q = [x - 1 for x in Q]
    a = 0
    b = 0
    for i in range(N):
        a += P[i] * math.factorial(N - i - 1)
        b += Q[i] * math.factorial(N - i - 1)
    print(abs(a - b))

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    x = 0
    y = 0
    for i in range(N):
        p = 1
        q = 1
        for j in range(i+1, N):
            if P[i] > P[j]:
                p += 1
            if Q[i] > Q[j]:
                q += 1
        x += (p - 1) * factorial(N - i - 1)
        y += (q - 1) * factorial(N - i - 1)
    print(abs(x - y))

=======
Suggestion 4

def main():
    N = int(input())
    P = [int(i) for i in input().split()]
    Q = [int(i) for i in input().split()]
    perm = [i for i in range(1, N+1)]
    P_index = 0
    Q_index = 0
    for i, p in enumerate(permutations(perm)):
        if list(p) == P:
            P_index = i
        if list(p) == Q:
            Q_index = i
    print(abs(P_index - Q_index))

=======
Suggestion 5

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    import itertools
    X = list(itertools.permutations(range(1,N+1)))
    print(abs(X.index(tuple(P)) - X.index(tuple(Q))))

=======
Suggestion 7

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    # 順列を列挙
    from itertools import permutations
    perms = permutations(range(1, N+1))

    # 辞書順でソート
    perms = sorted(perms)

    # 何番目かを調べる
    print(abs(perms.index(tuple(P)) - perms.index(tuple(Q))))

=======
Suggestion 8

def main():
    N = int(input())
    P = list(map(int,input().split()))
    Q = list(map(int,input().split()))
    #N!通りの順列を作成
    import itertools
    a = list(itertools.permutations(range(1,N+1),N))
    #a.index(P)は、Pがaの何番目かを返す
    print(abs(a.index(tuple(P))-a.index(tuple(Q))))

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    import itertools
    from itertools import permutations

    #順列の生成
    li = []
    for i in range(1, N+1):
        li.append(i)

    #順列の生成
    li = list(permutations(li))
    #print(li)

    #順列を辞書順に並び替える
    li.sort()
    #print(li)

    #P,Qの順列を辞書順に並び替える
    P.sort()
    Q.sort()
    #print(P)
    #print(Q)

    #P,Qの順列の辞書順の番号を取得
    a = li.index(tuple(P)) + 1
    b = li.index(tuple(Q)) + 1
    #print(a)
    #print(b)

    #答えを出力
    print(abs(a - b))

=======
Suggestion 10

def permutation(N, P, Q):
    #N:順列の数
    #P:順列
    #Q:順列
    #P,Qの辞書順の差を返す
    #N = int(input())
    #P = list(map(int, input().split()))
    #Q = list(map(int, input().split()))
    #N = 3
    #P = [1,3,2]
    #Q = [3,1,2]
    #N = 8
    #P = [7,3,5,4,2,1,6,8]
    #Q = [3,8,2,5,4,6,7,1]
    #N = 3
    #P = [1,2,3]
    #Q = [1,2,3]
    #P,Qの辞書順の差を返す
    import itertools
    import bisect
    L = list(itertools.permutations(range(1,N+1)))
    #print(L)
    P = tuple(P)
    Q = tuple(Q)
    #print(P)
    #print(Q)
    a = bisect.bisect_left(L, P)
    b = bisect.bisect_left(L, Q)
    #print(a)
    #print(b)
    return abs(a-b)
