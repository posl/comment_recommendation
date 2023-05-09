Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, N = map(int, input().split())
    x = min(B-1, N)
    ans = (A*x)//B - A*(x//B)
    print(ans)

=======
Suggestion 2

def main():
    a, b, n = map(int, input().split())
    x = min(b-1, n)
    print((a*x)//b - a*(x//b))

=======
Suggestion 3

def main():
    A, B, N = map(int, input().split())
    x = min(B-1, N)
    print((A*x)//B - A*(x//B))

=======
Suggestion 4

def main():
    a, b, n = map(int, input().split())
    x = min(n, b-1)
    print((a*x)//b - a*(x//b))

=======
Suggestion 5

def main():
    A, B, N = map(int, input().split())
    x = min(N, B-1)
    print((A*x)//B - A*(x//B))

=======
Suggestion 6

def main():
    a, b, n = map(int, input().split())
    if n < b:
        x = n
    else:
        x = b - 1
    print(int(a*x/b) - a*int(x/b))

=======
Suggestion 7

def main():
    a,b,n = map(int,input().split())
    x = min(n,b-1)
    print(int(a*x/b)-a*int(x/b))

=======
Suggestion 8

def main():
    A, B, N = map(int, input().split())
    max = 0
    for i in range(0, N + 1):
        if (A * i // B) - A * (i // B) > max:
            max = (A * i // B) - A * (i // B)
    print(max)
main()

=======
Suggestion 9

def floor(a,b):
    if a%b==0:
        return a//b
    else:
        return (a-a%b)//b

a,b,n=map(int,input().split())
