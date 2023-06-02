Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n,k,a = map(int, input().split())
    if (k-n)%(n-1) == 0:
        print(a)
    else:
        print((k-n)%(n-1)+a)

=======
Suggestion 2

def last_card(n,k,a):
    if n == 1:
        return 1
    else:
        if k == 1:
            return a
        elif k == 2:
            if a == 1:
                return 2
            else:
                return 1
        else:
            if a == 1:
                return last_card(n,k-1,n)
            else:
                return last_card(n,k-1,a-1)

=======
Suggestion 3

def problem227_a():
    n,k,a = map(int,input().split())
    print((k-1+a-1) % n + 1)
    return

=======
Suggestion 4

def main():
    N, K, A = map(int, input().split())
    if N == A:
        print(K % N)
    else:
        if K % N >= A:
            print(A + K % N - 1)
        else:
            print(K % N)

=======
Suggestion 5

def main():
    n,k,a = map(int, input().split())
    print((k - a + 1) % n)

=======
Suggestion 6

def problem227_a():
    n,k,a = map(int,input().split())
    print((k - a + 1) % n)

problem227_a()

=======
Suggestion 7

def main():
    # 读取输入
    n, k, a = map(int, input().split())
    # print(n, k, a)
    print((k - a) % n)

=======
Suggestion 8

def main():
    n,k,a = map(int,input().split())
    if (n-a+1) >= k:
        print(a+k-1)
    else:
        print(k-(n-a+1) % n)

=======
Suggestion 9

def main():
    # 读取输入
    input_str = input()
    input_list = input_str.split(' ')
    N = int(input_list[0])
    K = int(input_list[1])
    A = int(input_list[2])

    # 算法
    # 从A开始，我们将按以下顺序把卡片逐一发给大家：A, A+1, A+2, ..., N, 1, 2, ....谁会得到最后一张牌？
    # 从形式上看，在人x(1 ≦ x < N)得到一张牌后，人x+1会得到一张牌。在N人得到一张牌后，1人得到一张牌。
    # 1. 人x得到一张牌，人x+1会得到一张牌
    # 2. N人得到一张牌，1人得到一张牌
    # 3. 从A开始，我们将按以下顺序把卡片逐一发给大家：A, A+1, A+2, ..., N, 1, 2, ....谁会得到最后一张牌？
    # 4. 从形式上看，在人x(1 ≦ x < N)得到一张牌后，人x+1会得到一张牌。在N人得到一张牌后，1人得到一张牌。
    # 5. 从A开始，按顺序发牌，求最后一张牌的人
    # 6. 从A开始，按顺序发牌，求最后一张牌的人
    # 7. 从A开始，按顺序发牌，求最后一张牌的人
    # 8. 从A开始，按顺序发牌，求最后一张牌的人
    # 9. 从A开始，按顺序发牌，求最后一张牌的人
    # 10. 从A开始，

=======
Suggestion 10

def main():
    n,k,a = map(int,input().split())
    print((k-(n-a+1))%n+1)
