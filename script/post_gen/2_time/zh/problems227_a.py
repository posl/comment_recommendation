Synthesizing 9/10 solutions

=======
Suggestion 1

def get_last_card(n, k, a):
    card = 0
    for i in range(1, k+1):
        if card == 0:
            card = a
        else:
            card = (card + 1) % (n + 1)
            if card == 0:
                card = 1
    return card

=======
Suggestion 2

def main():
    N, K, A = map(int, input().split())
    print((K - A + N - 1) % N + 1)

=======
Suggestion 3

def main():
    n,k,a = map(int,input().split())
    res = (k+a-1) % n
    if res == 0:
        print(n)
    else:
        print(res)

=======
Suggestion 4

def main():
    n, k, a = map(int, input().split())
    if k % n == 0:
        print(a)
    else:
        print(a + k % n - 1)

=======
Suggestion 5

def main():
    # 输入
    n, k, a = map(int, input().split())
    #print(n, k, a)
    # 处理
    result = (k - (n - a + 1)) % n
    # 输出
    print(result)

=======
Suggestion 6

def main():
    N, K, A = map(int, input().split())
    print(K % N)

=======
Suggestion 7

def main():
    n,k,a = map(int,input().split())
    # n,k,a = map(int, "3 3 2".split())
    # n,k,a = map(int, "1 100 1".split())
    # n,k,a = map(int, "3 14 2".split())
    # print(n,k,a)
    # print(type(n),type(k),type(a))

    # for i in range(1,k+1):
    #     print("i:",i)
    #     if a < n:
    #         a += 1
    #     else:
    #         a = 1
    #     print("a:",a)
    # print(a)

    # for i in range(1,k+1):
    #     print("i:",i)
    #     a = (a + 1) if a < n else 1
    #     print("a:",a)
    # print(a)

    # print((a + k - 1) % n)

    # print(a + k - 1)
    # print((a + k - 1) % n)
    # print(((a + k - 1) % n) + 1)

    print((a + k - 1) % n + 1)

=======
Suggestion 8

def main():
    n,k,a = map(int,input().split())
    print((a+k-1)%n)

=======
Suggestion 9

def problem227_a():
    n, k, a = map(int, input().split())
    if k <= n:
        print(k)
    else:
        print(n - (k % n) + a)
