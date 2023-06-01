Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C, K = map(int, input().split())
    if A >= K:
        print(K)
    elif A + B >= K:
        print(A)
    else:
        print(A - (K - A - B))

=======
Suggestion 2

def main():
    a,b,c,k = map(int,input().split())
    if k <= a:
        print(k)
    elif k <= a+b:
        print(a)
    else:
        print(a-(k-a-b))

=======
Suggestion 3

def main():
    #读取输入
    a, b, c, k = map(int, input().split())
    #计算
    if k <= a:
        ans = k
    elif k <= a + b:
        ans = a
    else:
        ans = a - (k - a - b)
    #打印输出
    print(ans)

=======
Suggestion 4

def main():
    A,B,C,K = map(int,input().split())
    if A >= K:
        print(K)
    elif A+B >= K:
        print(A)
    else:
        print(A-(K-(A+B)))

=======
Suggestion 5

def main():
    A,B,C,K = map(int, input().split())
    if K <= A:
        print(K)
    elif K <= A + B:
        print(A)
    else:
        print(A - (K - A - B))

=======
Suggestion 6

def main():
    a,b,c,k = map(int,input().split())
    if a >= k:
        print(k)
    elif a+b >= k:
        print(a)
    else:
        print(a-(k-a-b))

=======
Suggestion 7

def solve(a, b, c, k):
    if a >= k:
        return k
    elif a + b >= k:
        return a
    else:
        return a - (k - a - b)
