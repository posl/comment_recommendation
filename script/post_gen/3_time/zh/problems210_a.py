Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    #获取输入
    n,a,x,y = map(int,input().split())
    #计算结果
    if n <= a:
        ans = n * x
    else:
        ans = a * x + (n-a) * y
    #输出结果
    print(ans)

=======
Suggestion 2

def main():
    n,a,x,y = map(int,input().split())
    if n <= a:
        print(n*x)
    else:
        print(a*x+(n-a)*y)

=======
Suggestion 3

def main():
    N, A, X, Y = map(int, input().split(" "))
    if N <= A:
        print(X*N)
    else:
        print(A*X + (N-A)*Y)

=======
Suggestion 4

def main():
    N,A,X,Y = map(int,input().split())
    if N <= A:
        print(N*X)
    else:
        print(A*X+(N-A)*Y)

=======
Suggestion 5

def main():
    N,A,X,Y = map(int,input().split())
    if N > A:
        print(A*X+(N-A)*Y)
    else:
        print(N*X)

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def cabbage(N,A,X,Y):
    if N <= A:
        return N * X
    else:
        return A * X + (N - A) * Y
