Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    ans = 0
    for i in range(N):
        ans += B[A[i]-1]
        if i > 0 and A[i] == A[i-1]+1:
            ans += C[A[i-1]-1]
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
        ans += B[A[i]-1]
        if i != N-1 and A[i+1] == A[i]+1:
            ans += C[A[i]-1]
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
        ans += B[A[i] - 1]
        if i < N - 1 and A[i] + 1 == A[i + 1]:
            ans += C[A[i] - 1]
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
        if i != N - 1 and A[i] + 1 == A[i + 1]:
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
        ans += B[A[i]-1]
        if i < N-1 and A[i+1] - A[i] == 1:
            ans += C[A[i]-1]
    print(ans)

=======
Suggestion 6

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
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        ans += B[A[i]-1]
        if i != N-1:
            if A[i] == A[i+1]-1:
                ans += C[A[i]-1]
    print(ans)

=======
Suggestion 8

def   main (): 
     # input 
     N   =   int ( input ()) 
     A   =   list ( map ( int ,   input (). split ())) 
     B   =   list ( map ( int ,   input (). split ())) 
     C   =   list ( map ( int ,   input (). split ())) 

     # initialize 
     ans   =   0 

     # count 
     for   i   in   range ( N ): 
         ans   +=   B [ A [ i ]   -   1 ] 
         if   i   !=   0   and   A [ i ]   -   A [ i   -   1 ]   ==   1 : 
             ans   +=   C [ A [ i   -   1 ]   -   1 ] 

     # output 
     print ( ans )

=======
Suggestion 9

def main():
    #read input
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    #initialize satisfaction points
    sat = 0
    
    #loop over dishes
    for i in range(N):
        #add satisfaction points from eating the dish
        sat += B[A[i]-1]
        
        #if the dish is not the last one and the next dish is consecutive
        if i < N-1 and A[i]+1 == A[i+1]:
            #add satisfaction points from eating consecutive dishes
            sat += C[A[i]-1]
    
    #print satisfaction points
    print(sat)
