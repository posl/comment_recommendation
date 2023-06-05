Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))

    print(h.index(max(h)) + 1)

=======
Suggestion 2

def main():
    num = int(input())
    list = input().split()
    max = 0
    for i in range(num):
        if int(list[i]) > max:
            max = int(list[i])
            max_index = i + 1
    print(max_index)

=======
Suggestion 3

def problems275_a():
    n = int(input())
    heights = list(map(int, input().split()))
    print(heights.index(max(heights)) + 1)

=======
Suggestion 4

def main():
    # 读取输入
    n = int(input())
    h = list(map(int, input().split()))

    # 计算并打印结果
    print(h.index(max(h)) + 1)

=======
Suggestion 5

def main():
    n = int(input())
    h = [int(i) for i in input().split()]
    print(h.index(max(h))+1)
