Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b,c,k = map(int,input().split())
    if k <= a:
        print(k)
    elif k <= a+b:
        print(a)
    else:
        print(a-(k-a-b))

=======
Suggestion 2

def get_input():
    a,b,c,k = map(int,input().split())
    return a,b,c,k

=======
Suggestion 3

def main():
    A, B, C, K = map(int, input().split())
    if A >= K:
        print(K)
    elif A + B >= K:
        print(A)
    else:
        print(A - (K - A - B))

=======
Suggestion 4

def main():
    #读取输入
    A, B, C, K = map(int, input().split())
    #最大可能的和
    sum = 0
    #先从A中取出K张
    if A >= K:
        sum += K
        K = 0
    else:
        sum += A
        K -= A
    #再从B中取出K张
    if B >= K:
        K = 0
    else:
        K -= B
    #最后从C中取出K张
    if C >= K:
        sum -= K
    else:
        sum -= C
    #打印结果
    print(sum)

=======
Suggestion 5

def main():
    a,b,c,k = map(int,input().split())
    if a >= k:
        print(k)
    elif a+b >= k:
        print(a)
    else:
        print(a-(k-a-b))
main()

=======
Suggestion 6

def main():
    a, b, c, k = map(int, input().split())
    if a >= k:
        print(k)
    elif a + b >= k:
        print(a)
    else:
        print(a - (k - a - b))

=======
Suggestion 7

def main():
    a,b,c,k = map(int,input().split())
    if a > k:
        print(k)
    elif a+b > k:
        print(a)
    else:
        print(a-(k-a-b))
main()

=======
Suggestion 8

def main():
    A, B, C, K = map(int, input().split())
    if K <= A:
        print(K)
    elif K <= A + B:
        print(A)
    else:
        print(A - (K - A - B))
