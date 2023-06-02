Synthesizing 10/10 solutions

=======
Suggestion 1

def problems108_a():
    k = int(input())
    if k < 2 or k > 100:
        return
    print(int(k/2) * int((k+1)/2))

=======
Suggestion 2

def main():
    k = int(input())
    if k % 2 == 0:
        print(int((k / 2) * (k / 2)))
    else:
        print(int(((k - 1) / 2) * ((k + 1) / 2)))

=======
Suggestion 3

def main():
    K = int(input())
    if K % 2 == 0:
        print((K // 2) ** 2)
    else:
        print((K // 2) * (K // 2 + 1))

=======
Suggestion 4

def problems108_a(k):
    count = 0
    for i in range(1, k+1):
        for j in range(1, k+1):
            if i%2 == 0 and j%2 != 0:
                count += 1
    return count

=======
Suggestion 5

def main():
    k = int(input())
    print(int(k/2) * int((k+1)/2))

=======
Suggestion 6

def main():
    k = int(input())
    # print(k)
    count = 0
    for i in range(1, k + 1):
        for j in range(i + 1, k + 1):
            if i % 2 == 0 and j % 2 != 0:
                count += 1
            elif i % 2 != 0 and j % 2 == 0:
                count += 1
    print(count)

=======
Suggestion 7

def main():
    k = int(input())
    print((k//2)*((k+1)//2))

=======
Suggestion 8

def main():
    k = int(input())
    print(int(k/2 * (k - k/2)))

=======
Suggestion 9

def main():
    k = int(input())
    if k % 2 == 0:
        print(int(k / 2) * int(k / 2))
    else:
        print(int(k / 2) * int(k / 2 + 1))

=======
Suggestion 10

def main():
    # 从标准输入读取
    K = int(input())
    # 计算并打印答案
    print(int(K/2) * int(K/2 + 0.5))
