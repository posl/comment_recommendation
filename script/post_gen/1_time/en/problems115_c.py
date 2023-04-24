Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    H.sort()
    print(min(H[i + K - 1] - H[i] for i in range(N - K + 1)))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = 10 ** 9
    for i in range(n - k + 1):
        ans = min(ans, h[i + k - 1] - h[i])
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    H.sort()
    ans = 10 ** 9
    for i in range(N - K + 1):
        ans = min(ans, H[i + K - 1] - H[i])
    print(ans)

=======
Suggestion 4

def   main (): 
     N ,   K   =   map ( int ,   input (). split ()) 
     H   =   sorted ([ int ( input ())   for   _   in   range ( N )]) 
     print ( min ( H [ i   +   K   -   1 ]   -   H [ i ]   for   i   in   range ( N   -   K   +   1 )))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    h.sort()
    ans = 10 ** 9
    for i in range(N - K + 1):
        ans = min(ans, h[i + K - 1] - h[i])
    print(ans)

=======
Suggestion 6

def solve():
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    h.sort()
    ans = 10**9
    for i in range(n-k+1):
        ans = min(ans, h[i+k-1] - h[i])
    print(ans)

=======
Suggestion 7

def solve(N, K, H):
    H.sort()
    ans = 10**9
    for i in range(N-K+1):
        ans = min(ans, H[i+K-1]-H[i])
    return ans

=======
Suggestion 8

def   main (): 
     N ,  K   =   map ( int ,  input (). split ()) 
     h   =   sorted ( list ( map ( int ,  input (). split ()))) 
     ans   =   10 ** 9 
     for   i   in   range ( N   -  K   +   1 ): 
         ans   =   min ( ans ,  h [ i   +  K   -   1 ]   -  h [ i ]) 
     print ( ans )

=======
Suggestion 9

def main():
    # Write your code here
    N, K = map(int, input().split())
    h = sorted([int(input()) for _ in range(N)])
    print(min(h[i + K - 1] - h[i] for i in range(N - K + 1)))

=======
Suggestion 10

def  main():
    N, K =  map ( int , input().split())
    H = [ int (input())  for  _  in   range (N)]
    H.sort()
    ans =  float ( 'inf' )
     for  i  in   range (N - K +  1 ):
        ans = min(ans, H[i + K -  1 ] - H[i])
    print(ans)
