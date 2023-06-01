Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读入数据
    a,b,n = map(int, input().split())

    # 计算结果
    x = min(b-1,n)
    ans = (a*x)//b - a*(x//b)

    # 打印结果
    print(ans)

=======
Suggestion 2

def solve():
    A, B, N = map(int, input().split())
    x = min(B - 1, N)
    print((A * x // B) - A * (x // B))

=======
Suggestion 3

def calc(A,B,N):
    max = 0
    for x in range(0, N+1):
        temp = A*x/B - A*(x/B)
        if max < temp:
            max = temp
    return max

=======
Suggestion 4

def main():
    a,b,n = map(int, input().split())
    if b > n:
        x = n
    else:
        x = b-1
    print((a*x)//b - a*(x//b))

=======
Suggestion 5

def main():
    A, B, N = map(int, input().split())
    x = min(B-1, N)
    print((A*x)//B - A*(x//B))

=======
Suggestion 6

def main():
    A,B,N = map(int,input().split())
    x = min(B-1,N)
    print(A*x//B-A*(x//B))

=======
Suggestion 7

def floor(a,b):
    return int(a/b)

=======
Suggestion 8

def floor(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return int(x)

=======
Suggestion 9

def getFloor(A,B,N):
    max = 0
    for x in range(0, N+1):
        if (A*x/B)-A*(x/B) > max:
            max = (A*x/B)-A*(x/B)
    return max

A,B,N = input().split()
A = int(A)
B = int(B)
N = int(N)
print(getFloor(A,B,N))

=======
Suggestion 10

def main():
    a,b,n = map(int, input().split())

    x = min(b-1, n)
    print(a*x//b - a*(x//b))
