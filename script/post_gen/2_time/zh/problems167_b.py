Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A,B,C,K = map(int, input().split())
    if A >= K:
        print(K)
    elif A + B >= K:
        print(A)
    else:
        print(A - (K - A - B))

=======
Suggestion 2

def main():
    # 读取输入
    a, b, c, k = map(int, input().split())

    # 可以用a张1的卡片
    if k <= a:
        print(k)
        return

    # 可以用a+b张卡片
    if k <= a + b:
        print(a)
        return

    # 其他情况
    print(a - (k - a - b))

=======
Suggestion 3

def main():
    a,b,c,k = map(int,input().split())
    if k <= a:
        print(k)
    elif k <= a + b:
        print(a)
    else:
        print(a - (k - a - b))

=======
Suggestion 4

def main():
    a,b,c,k = map(int,input().split())
    if a >= k:
        print(k)
    elif a+b >= k:
        print(a)
    else:
        print(a-(k-a-b))

=======
Suggestion 5

def main():
    a,b,c,k = map(int,input().split())
    if a >= k:
        print(k)
        return
    k = k - a
    if b >= k:
        print(a)
        return
    k = k - b
    print(a-k)
