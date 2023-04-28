Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += B[A[i] - 1]
        if i != N - 1 and A[i] + 1 == A[i + 1]:
            ans += C[A[i] - 1]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += B[A[i] - 1]
        if i > 0 and A[i - 1] + 1 == A[i]:
            ans += C[A[i - 1] - 1]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += B[A[i]-1]
        if i > 0 and A[i] == A[i-1]+1:
            ans += C[A[i-1]-1]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += B[A[i] - 1]
        if i != N - 1 and A[i] == A[i + 1] - 1:
            ans += C[A[i] - 1]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += B[A[i] - 1]
        if i < N - 1 and A[i + 1] == A[i] + 1:
            ans += C[A[i] - 1]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += b[a[i] - 1]
        if i != 0 and a[i] == a[i - 1] + 1:
            ans += c[a[i - 1] - 1]
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += b[a[i] - 1]
        if i != n - 1 and a[i] + 1 == a[i + 1]:
            ans += c[a[i] - 1]
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = sum(b)
    for i in range(n-1):
        if a[i+1] - a[i] == 1:
            ans += c[a[i]-1]
    print(ans)

=======
Suggestion 9

def   main (): 
     # Input 
     n   =   int ( input ()) 
     a   =   list ( map ( int ,   input (). split ())) 
     b   =   list ( map ( int ,   input (). split ())) 
     c   =   list ( map ( int ,   input (). split ())) 

     # Solve 
     ans   =   0 
     for   i   in   range ( n ): 
         ans   +=   b [ a [ i ]   -   1 ] 
         if   i   >   0   and   a [ i ]   ==   a [ i   -   1 ]   +   1 : 
             ans   +=   c [ a [ i   -   1 ]   -   1 ] 

     # Output 
     print ( ans )
