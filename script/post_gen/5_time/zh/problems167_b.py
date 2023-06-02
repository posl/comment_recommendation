Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A,B,C,K = map(int,input().split())
    if K <= A:
        print(K)
    elif K <= A + B:
        print(A)
    else:
        print(A - (K - A - B))

=======
Suggestion 2

def main():
    a,b,c,k = map(int,input().split())
    if a >= k:
        print(k)
    elif a+b >= k:
        print(a)
    else:
        print(a-(k-a-b))

=======
Suggestion 3

def main():
    a,b,c,k = map(int, input().split())
    if k <= a:
        print(k)
    elif k <= a + b:
        print(a)
    else:
        print(a - (k - a - b))

=======
Suggestion 4

def main():
    A, B, C, K = map(int, input().split())
    #print(A, B, C, K)
    if A >= K:
        print(K)
    elif A + B >= K:
        print(A)
    else:
        print(A - (K - A - B))

=======
Suggestion 5

def main():
    # 读取输入
    A, B, C, K = map(int, input().split())
    # 计算和
    ans = min(A, K)
    K -= A
    K = max(K, 0)
    K -= B
    ans -= min(C, K)
    # 输出结果
    print(ans)

=======
Suggestion 6

def main():
    A,B,C,K = map(int,input().split())
    if A >= K:
        print(K)
    elif A+B >= K:
        print(A)
    else:
        print(A-(K-A-B))

=======
Suggestion 7

def main():
    A,B,C,K = map(int,input().split())
    if A >= K:
        print(K)
    elif A+B >= K:
        print(A)
    else:
        print(A-(K-A-B))
main()
