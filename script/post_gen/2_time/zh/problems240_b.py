Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 2

def main():
    # 读取输入
    n = int(input())
    a = list(map(int, input().split()))
    # 用集合存储不同的整数
    s = set()
    for x in a:
        s.add(x)
    # 打印答案
    print(len(s))

=======
Suggestion 3

def main():
    # 读取输入
    input()
    num_list = input().split(" ")
    # 用集合去重
    num_set = set(num_list)
    # 输出集合元素个数
    print(len(num_set))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = set(a)
    print(len(b))

=======
Suggestion 5

def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    i = 0
    while i < n:
        count += 1
        while i + 1 < n and a[i] == a[i + 1]:
            i += 1
        i += 1
    print(count)
