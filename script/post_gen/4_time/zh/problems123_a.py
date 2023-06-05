Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    if e - a > k:
        print(':(')
    else:
        print('Yay!')

=======
Suggestion 2

def problems123_a():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    if e - a > k:
        print(':(')
    else:
        print('Yay!')

=======
Suggestion 3

def main():
    # 读取输入
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    # 求出最大的距离
    max_distance = e - a

    # 输出结果
    if max_distance <= k:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 4

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if e - a <= k:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 5

def main():
    # 读取输入
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    # 比较
    if e - a > k:
        print(':(')
    else:
        print('Yay!')

=======
Suggestion 6

def problems123_a():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if e-a > k:
        print(":(")
    else:
        print("Yay!")
    return

=======
Suggestion 7

def main():
    # 读取输入
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    # 用列表保存天线坐标
    antenna = [a, b, c, d, e]

    # 用列表保存天线之间的距离
    distance = []

    # 计算天线之间的距离
    for i in range(len(antenna)):
        for j in range(i + 1, len(antenna)):
            distance.append(antenna[j] - antenna[i])

    # 如果存在天线之间的距离大于k，则输出 :(，否则输出 Yay!
    if max(distance) > k:
        print(':(')
    else:
        print('Yay!')
