Synthesizing 10/10 solutions

=======
Suggestion 1

def floor(a,b):
    return int(a/b)

=======
Suggestion 2

def main():
    # 读入数据
    A, B, N = map(int, input().split())
    # 计算结果
    ans = int(A * min(B - 1, N) / B)
    # 输出结果
    print(ans)

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

def get_max(a, b, n):
    max = 0
    for x in range(0, n+1):
        temp = (a * x // b) - a * (x // b)
        if temp > max:
            max = temp
    return max

=======
Suggestion 5

def main():
    a,b,n = map(int,input().split())
    x = min(b-1,n)
    print((a*x)//b)

=======
Suggestion 6

def main():
    A,B,N = map(int,input().split())
    if B > N:
        print((A*N)//B)
    else:
        print((A*(B-1))//B)

=======
Suggestion 7

def floor(a,b):
    return a//b

=======
Suggestion 8

def main():
    A,B,N = map(int,input().split())
    x = min(B-1,N)
    print(A*x//B - A*(x//B))

=======
Suggestion 9

def main():
    A,B,N = map(int,input().split())
    x = min(N,B-1)
    print(int(A*x/B)-A*int(x/B))

=======
Suggestion 10

def main():
    A,B,N = map(int,input().split())
    # print(A,B,N)
    x = min(B-1,N)
    print((A*x)//B - A*(x//B))
    # print((A*x)//B - A*(x//B))
    # print((A*x)//B)
    # print(A*(x//B))
