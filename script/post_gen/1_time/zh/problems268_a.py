Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C, D, E = map(int, input().split())
    print(len(set([A, B, C, D, E])))

=======
Suggestion 2

def main():
    a, b, c, d, e = map(int, input().split())
    print(len(set([a, b, c, d, e])))

=======
Suggestion 3

def get_diff_num(a, b, c, d, e):
    return len(set([a, b, c, d, e]))

=======
Suggestion 4

def main():
    a = input().split()
    b = []
    for i in range(5):
        if a[i] not in b:
            b.append(a[i])
    print(len(b))

=======
Suggestion 5

def solve():
    num = input().split()
    num = set(num)
    print(len(num))

solve()

=======
Suggestion 6

def main():
    nums = [int(x) for x in input().split()]
    print(len(set(nums)))

=======
Suggestion 7

def main():
    # 读取输入
    input_line = input().split()
    # 初始化一个空列表
    list = []
    # 遍历输入的每一个值
    for i in range(len(input_line)):
        # 将每一个值转换为int类型，并添加到列表中
        list.append(int(input_line[i]))
    # 将列表转换为集合，并打印集合的长度
    print(len(set(list)))
