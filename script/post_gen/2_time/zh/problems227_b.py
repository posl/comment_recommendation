Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k,a = map(int,input().split())
    if k < n:
        print(k+a)
    else:
        k = k-n
        a = a-1
        print((a+k)%n+1)

=======
Suggestion 2

def main():
    # 读取输入
    n, k, a = map(int, input().split())
    # 模拟发卡
    cards = [i for i in range(1, k + 1)]
    for i in range(k):
        # 人数循环
        if i % n + 1 == a:
            # 该人拿到最后一张牌
            print(i % n + 1)
            break
        else:
            # 该人拿不到最后一张牌
            cards[i % n] = 0

=======
Suggestion 3

def main():
    # N,K,A = map(int,input().split())
    N,K,A = 3,14,2
    print(N,K,A)
    print('hello world')

=======
Suggestion 4

def get_last_card(n,k,a):
    # n,k,a = input().split()
    # n = int(n)
    # k = int(k)
    # a = int(a)
    n = int(n)
    k = int(k)
    a = int(a)
    if n == 1:
        return 1
    if a+k <= n:
        return a+k
    else:
        return a+k-n

=======
Suggestion 5

def main():
    n, k, a = map(int, input().split())
    print((k - a + 1) % n)

=======
Suggestion 6

def main():
    # 读取输入
    input_line = input()
    input_line = input_line.split(" ")
    # print(input_line)
    n = int(input_line[0])
    k = int(input_line[1])
    a = int(input_line[2])

    # print(n, k, a)

    # 开始处理
    # 用一个数组表示每个人的卡片数量
    card_nums = [0 for i in range(n)]
    # print(card_nums)

    # 从a开始发牌，循环k次
    for i in range(k):
        # print(i)
        # print(a)
        # print(card_nums)
        card_nums[a-1] += 1
        # print(card_nums)
        # print("-----")
        a += 1
        if a > n:
            a = 1
    # print(card_nums)

    # 找到最大值
    max_num = max(card_nums)
    # print(max_num)

    # 找到最大值的索引
    max_index = card_nums.index(max_num)
    # print(max_index)

    # print(max_index + 1)

    # 输出结果
    print(max_index + 1)

=======
Suggestion 7

def get_last_person(n,k,a):
    if a + k <= n:
        return a + k - 1
    else:
        return a + k - n - 1

=======
Suggestion 8

def main():
    n, k, a = map(int, input().split())
    k = k % n
    if a + k <= n:
        print(a + k)
    else:
        print(a + k - n)

=======
Suggestion 9

def main():
    n, k, a = map(int, input().split())
    print((k - n + a - 1) % n + 1)

=======
Suggestion 10

def main():
    N,K,A = input().split()
    N = int(N)
    K = int(K)
    A = int(A)
    if N == 1:
        print(1)
        return
    else:
        if K % N == 0:
            if A == N:
                print(1)
                return
            else:
                print(A + K % N - 1)
                return
        else:
            if A + K % N - 1 <= N:
                print(A + K % N - 1)
                return
            else:
                print(A + K % N - 1 - N)
                return
