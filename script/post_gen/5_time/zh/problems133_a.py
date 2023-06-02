Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读入数据
    n, a, b = map(int, input().split())
    # 计算最小值
    print(min(n*a, b))

=======
Suggestion 2

def main():
    n,a,b = map(int,input().split())
    print(min(n*a,b))

=======
Suggestion 3

def min_cost(N,A,B):
    if N*A > B:
        return B
    else:
        return N*A

=======
Suggestion 4

def min_trip_cost(n,a,b):
    return min(n*a,b)

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    print(min(A*N,B))

=======
Suggestion 6

def main():
    n,a,b = map(int,input().split())
    if a*n < b:
        print(a*n)
    else:
        print(b)

=======
Suggestion 7

def main():
    n,a,b = map(int,input().split())
    if n*a < b:
        print(n*a)
    else:
        print(b)

=======
Suggestion 8

def cost(n, a, b):
    return min(n * a, b)
