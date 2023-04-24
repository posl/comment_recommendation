Synthesizing 10/10 solutions

=======
Suggestion 1

def   main (): 
     N   =   int ( input ()) 
     A   =   list ( map ( int ,   input (). split ())) 
     B   =   [] 
     C   =   [] 
     for   i   in   range ( N ): 
         if   A [ i ]   %   200   ==   0 : 
             B . append ( i   +   1 ) 
         else : 
             C . append ( i   +   1 ) 
     if   len ( B )   >   0   and   len ( C )   >   0   or   len ( B )   >=   2 : 
         print ( 'Yes' ) 
         if   len ( B )   >   0   and   len ( C )   >   0 : 
             print ( 1 ,   B [ 0 ]) 
             print ( 1 ,   C [ 0 ]) 
         else : 
             print ( 2 ,   B [ 0 ],   B [ 1 ]) 
             print ( 1 ,   C [ 0 ]) 
     else : 
         print ( 'No' )

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0] * (N+1)
    for i in range(N):
        S[i+1] = (S[i] + A[i]) % 200
    D = {}
    for i in range(N+1):
        if S[i] not in D:
            D[S[i]] = []
        D[S[i]].append(i)
    for k in D:
        if len(D[k]) > 1:
            print('Yes')
            print(len(D[k])-1, *D[k][1:])
            print(len(D[k])-1, *D[k][:-1])
            return
    print('No')
    return

main()

=======
Suggestion 3

def   main (): 
     N   =   int ( input ()) 
     A   =   list ( map ( int ,   input (). split ())) 
     M   =   200 
     dp   =   [ None   for   i   in   range ( M )] 
     dp [ A [ 0 ]   %   M ]   =   [ 0 ] 
     for   i   in   range ( 1 ,   N ): 
         if   dp [ A [ i ]   %   M ]   is   None : 
             dp [ A [ i ]   %   M ]   =   [ i ] 
         else : 
             print ( "Yes" ) 
             print ( len ( dp [ A [ i ]   %   M ]),   " " . join ( map ( str ,   map ( lambda   x :   x   +   1 ,   dp [ A [ i ]   %   M ]))),   sep = "

" ) 
             print ( 1 ,   i   +   1 ,   sep = "

" ) 
             exit () 
         for   j   in   range ( M ): 
             if   dp [ j ]   is   None : 
                 continue 
             if   dp [( j   +   A [ i ])   %   M ]   is   None : 
                 dp [( j   +   A [ i ])   %   M ]   =   dp [ j ]   +   [ i ] 
             else : 
                 print ( "Yes" ) 
                 print ( len ( dp [ j ]),   " " . join ( map ( str ,   map ( lambda   x :   x   +   1 ,   dp [ j ]))),   sep = "

" ) 
                 print ( len ( dp [( j   +   A [ i ])   %   M ]),   " " . join ( map ( str ,   map ( lambda   x :   x   +   1 ,   dp [( j   +   A [ i ])   %   M ]))),   sep = "

" ) 
                 exit () 
     print ( "No" )

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    d = {}
    for i in range(N):
        a = A[i]
        m = a % mod
        if m in d:
            d[m].append(i)
        else:
            d[m] = [i]
    for k, v in d.items():
        if len(v) > 1:
            print('Yes')
            print(len(v), ' '.join([str(i+1) for i in v]))
            print(1, v[0]+1)
            return
    for k, v in d.items():
        for k2, v2 in d.items():
            if k == k2:
                continue
            if (k + k2) % mod == 0:
                print('Yes')
                print(len(v), ' '.join([str(i+1) for i in v]))
                print(len(v2), ' '.join([str(i+1) for i in v2]))
                return
    print('No')
    return

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    c = [0] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if (a[i] + a[j]) % 200 == 0:
                print("Yes")
                print(1, i + 1)
                print(1, j + 1)
                return
            b[i] += a[j]
            c[j] += a[i]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if b[i] % 200 == c[j] % 200:
                print("Yes")
                print(i + 1, end=" ")
                for k in range(n):
                    if k == j:
                        continue
                    print(k + 1, end=" ")
                print()
                print(j + 1, end=" ")
                for k in range(n):
                    if k == i:
                        continue
                    print(k + 1, end=" ")
                print()
                return
    print("No")

main()

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    A = [a % 200 for a in A]
    D = {}
    for i in range(N):
        if A[i] in D:
            D[A[i]].append(i)
        else:
            D[A[i]] = [i]
    for a in D:
        if len(D[a]) >= 2:
            print("Yes")
            print(1, D[a][0]+1)
            print(1, D[a][1]+1)
            return
    for a in D:
        for b in D:
            if a == b: continue
            if (a+b) % 200 == 0:
                print("Yes")
                print(2, D[a][0]+1, D[b][0]+1)
                return
    print("No")

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))

    m = 200
    r = [None] * m
    for i in range(n):
        b = a[i] % m
        if r[b] is None:
            r[b] = [i]
        else:
            print("Yes")
            print(1, r[b][0] + 1)
            print(1, i + 1)
            return
    for i in range(m):
        if r[i] is not None and len(r[i]) == 2:
            print("Yes")
            print(2, r[i][0] + 1, r[i][1] + 1)
            return
    print("No")

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    MOD = 200
    dp = [[None] * MOD for _ in range(N + 1)]
    dp[0][0] = []
    for i in range(N):
        for j in range(MOD):
            if dp[i][j] is None:
                continue
            dp[i + 1][j] = dp[i][j]
            dp[i + 1][(j + A[i]) % MOD] = dp[i][j] + [i]
    for i in range(MOD):
        if dp[N][i] is None:
            continue
        if len(dp[N][i]) > 1:
            print("Yes")
            print(len(dp[N][i]))
            print(*[a + 1 for a in dp[N][i]])
            print(len(dp[N][i]) - 1)
            print(*[a + 1 for a in dp[N][i][1:]])
            return
    print("No")

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    mod = 200
    dp = [0] * mod
    dp[A[0]] = 1
    for i in range(1, N):
        for j in range(mod):
            dp[j] = max(dp[j], dp[(j - A[i]) % mod] + 1)
    if max(dp) < 2:
        print("No")
        return
    else:
        print("Yes")
        dp2 = [0] * mod
        dp2[A[0]] = 1
        for i in range(1, N):
            for j in range(mod):
                dp2[j] = max(dp2[j], dp2[(j - A[i]) % mod] + 1)
            if dp2[A[i]] == 2:
                print("2", i + 1)
                print("1", i + 1)
                return
            if dp2[A[i]] == 1:
                print("1", i + 1)
                for j in range(1, N):
                    if dp2[A[j]] == 2:
                        print("1", j + 1)
                        return
                return
        return

=======
Suggestion 10

def solve(n, A):
    # Write your code here
    # Return "Yes" or "No" and B and C
    # B = (B_1, B_2, ..., B_x)
    # C = (C_1, C_2, ..., C_y)
    # return "Yes", B, C
    return "No"
