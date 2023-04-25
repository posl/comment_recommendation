Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    H.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, H[i+K-1]-H[i])
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    H.sort()
    ans = float("inf")
    for i in range(N-K+1):
        ans = min(ans, H[i+K-1]-H[i])
    print(ans)

=======
Suggestion 3

def   solve ( N ,   K ,   h ): 
     h . sort () 
     ans   =   10 ** 9 
     for   i   in   range ( N   -   K   +   1 ): 
         ans   =   min ( ans ,   h [ i   +   K   -   1 ]   -   h [ i ]) 
     return   ans

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    h = []
    for _ in range(N):
        h.append(int(input()))
    h.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, h[i+K-1] - h[i])
    print(ans)

=======
Suggestion 5

def solve(n, k, h):
    h.sort()
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans, h[i+k-1] - h[i])
    return ans

=======
Suggestion 6

def solve():
    n,k = map(int,input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans,h[i+k-1]-h[i])
    print(ans)

solve()

=======
Suggestion 7

def   solve ( N ,   K ,   H ): 
     H . sort () 
     min_diff   =   10 ** 9 
     for   i   in   range ( N   -   K   +   1 ): 
         min_diff   =   min ( min_diff ,   H [ i   +   K   -   1 ]   -   H [ i ]) 
     print ( min_diff )

=======
Suggestion 8

def   main () : 
     N ,   K   =   map ( int ,   input (). split ()) 
     h   =   sorted ( [ int ( input ())   for   i   in   range ( N )]) 
     ans   =   10 ** 9 
     for   i   in   range ( N - K   +   1 ): 
         ans   =   min ( ans ,   h [ i   +   K   -   1 ]   -   h [ i ]) 
     print ( ans )

=======
Suggestion 9

def   main (): 
     # Input 
     N ,   K   =   map ( int ,   input (). split ()) 
     H   =   sorted ( map ( int ,   input () for _   in   range ( N ))) 

     # Solve 
     ans   =   float ( 'inf' ) 
     for   i   in   range ( N   -   K   +   1 ): 
         ans   =   min ( ans ,   H [ i   +   K   -   1 ]   -   H [ i ]) 

     # Output 
     print ( ans )
