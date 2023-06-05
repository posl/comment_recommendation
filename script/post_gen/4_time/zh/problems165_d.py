Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,n = map(int,input().split())
    print(int(a*min(b-1,n)/b))
main()

=======
Suggestion 2

def main():
    a,b,n = map(int,input().split())
    x = min(n,b-1)
    print(a*x//b-a*(x//b))

=======
Suggestion 3

def main():
    A, B, N = map(int, input().split())
    ans = 0
    x = min(B - 1, N)
    ans = (A * x) // B - A * (x // B)
    print(ans)

=======
Suggestion 4

def main():
    a,b,n = map(int,input().split())
    x = min(b-1,n)
    print(int((a*x)/b)-a*int(x/b))

=======
Suggestion 5

def solve(A,B,N):
    x = min(B-1,N)
    return (A*x)//B - A*(x//B)

A,B,N = map(int,input().split())
print(solve(A,B,N))

=======
Suggestion 6

def main():
    a,b,n=map(int,input().split())
    print((a*min(b-1,n))//b)

=======
Suggestion 7

def main():
    A,B,N = map(int,input().split())
    if A > B:
        print(B-1)
    else:
        print(int(A*N/B))

=======
Suggestion 8

def main():
    A, B, N = map(int, input().split())
    x = min(B-1, N)
    print((A*x)//B - A*(x//B))

=======
Suggestion 9

def main():
    # read input
    A, B, N = map(int, input().split())
    #print(A, B, N)

    # solve the problem
    ans = 0
    x = min(B-1, N)
    ans = (A*x)//B - A*(x//B)

    # output
    print(ans)
