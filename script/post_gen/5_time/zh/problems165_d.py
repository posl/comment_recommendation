Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A,B,N = map(int,input().split())
    ans = 0
    x = min(B-1,N)
    ans = max(ans,A*x//B-A*(x//B))
    print(ans)

=======
Suggestion 2

def main():
    a,b,n = map(int, input().split())
    x = min(n,b-1)
    print((a*x)//b - a*(x//b))

=======
Suggestion 3

def solution():
    A,B,N = map(int, input().split())
    ans = 0
    x = min(B-1,N)
    ans = (A*x)//B - A*(x//B)
    return ans

=======
Suggestion 4

def main():
    a, b, n = map(int, input().split())
    x = min(n, b - 1)
    print(a * x // b - a * (x // b))

=======
Suggestion 5

def main():
    a,b,n=map(int,input().split())
    max=0
    for x in range(0,n+1):
        if (a*x//b)-(a*(x//b))>max:
            max=(a*x//b)-(a*(x//b))
    print(max)
    return

=======
Suggestion 6

def floor(x,y):
    return int(x/y)

=======
Suggestion 7

def solve():
    A,B,N = map(int, input().split())
    ans = 0
    if B > N:
        ans = min(A-1, N)
    else:
        ans = min(A-1, B-1)
        ans = ans * (N // B)
        ans += (N % B) // A
    print(ans)

=======
Suggestion 8

def get_input():
    input = raw_input()
    input_list = input.split(' ')
    return int(input_list[0]), int(input_list[1]), int(input_list[2])

=======
Suggestion 9

def main():
    A,B,N = map(int,input().split())
    x = min(B-1,N)
    print(A*x//B - A*(x//B))

=======
Suggestion 10

def floor(x):
    return int(x)
