Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A,B,N=map(int,input().split())
    x=min(B-1,N)
    print(int(A*x/B)-A*int(x/B))

=======
Suggestion 2

def main():
    # 读入数据
    a,b,n=map(int,input().split())
    # 计算结果
    x=min(n,b-1)
    ans=a*x//b-a*(x//b)
    # 输出结果
    print(ans)

=======
Suggestion 3

def main():
    a, b, n = map(int, input().split())
    x = min(b-1, n)
    print((a*x)//b - a*(x//b))

=======
Suggestion 4

def calc(A, B, N):
    max = 0
    for x in range(0, N+1):
        val = A*x//B - A*(x//B)
        if max < val:
            max = val
    return max

=======
Suggestion 5

def floor(a,b):
    return a//b

=======
Suggestion 6

def floor(A,B,N):
    x = 0
    max = 0
    while x <= N:
        if max < A*x/B - A*(x/B):
            max = A*x/B - A*(x/B)
        x += 1
    return max

=======
Suggestion 7

def solve(A,B,N):
    ans = 0
    x = min(B-1,N)
    ans = (A*x)//B - A*(x//B)
    return ans

=======
Suggestion 8

def f(A,B,N):
    max = 0
    for x in range(N+1):
        if max < int(A*x/B) - A*int(x/B):
            max = int(A*x/B) - A*int(x/B)
    return max

A,B,N = map(int,input().split())
print(f(A,B,N))

=======
Suggestion 9

def main():
    a,b,n = map(int,input().split())
    x = min(b-1,n)
    print((a*x)//b - a*(x//b))

main()

=======
Suggestion 10

def main():
    a,b,n = map(int,input().split())
    x = min(b-1,n)
    print(a*x//b)
