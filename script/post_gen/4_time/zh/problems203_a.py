Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a == b:
        print(c)
    elif a == c:
        print(b)
    elif b == c:
        print(a)
    else:
        print(0)

=======
Suggestion 2

def main():
    a = input().split()
    if a[0] == a[1]:
        print(a[2])
    elif a[0] == a[2]:
        print(a[1])
    elif a[1] == a[2]:
        print(a[0])
    else:
        print(0)

=======
Suggestion 3

def main():
    # 读取输入
    line = input()
    # 分割输入
    a, b, c = map(int, line.split())
    # 用列表来存储输入
    l = [a, b, c]
    # 用列表来存储不同的数字
    l2 = []
    # 用列表来存储相同的数字
    l3 = []
    # 用列表来存储最终结果
    l4 = []
    # 如果有两个相同的数字
    if l[0] == l[1] or l[1] == l[2] or l[2] == l[0]:
        # 遍历列表
        for i in l:
            # 如果列表中不存在该数字
            if i not in l2:
                # 将该数字添加到列表中
                l2.append(i)
            # 如果列表中存在该数字
            else:
                # 将该数字添加到列表中
                l3.append(i)
        # 遍历列表
        for i in l:
            # 如果i不在列表l3中
            if i not in l3:
                # 将i添加到列表l4中
                l4.append(i)
        # 遍历列表
        for i in l4:
            # 打印列表中的数字
            print(i)
    # 如果没有两个相同的数字
    else:
        # 打印0
        print(0)

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif a == c:
        print(b)
    else:
        print(0)

=======
Suggestion 5

def main():
    # 读取输入
    a, b, c = map(int, input().split())

    # 逻辑处理 & 结果输出
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif a == c:
        print(b)
    else:
        print(0)

=======
Suggestion 6

def main():
    # 读取输入
    a, b, c = map(int, input().split())

    # 检查是否有两个数字相同
    if a == b:
        print(c)
    elif a == c:
        print(b)
    elif b == c:
        print(a)
    else:
        print(0)
