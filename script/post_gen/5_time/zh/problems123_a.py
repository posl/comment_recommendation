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

    if e - a <= k:
        print('Yay!')
    else:
        print(':(')

=======
Suggestion 2

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
Suggestion 3

def main():
    # 读取输入
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    # 计算距离
    if e - a > k:
        print(':(')
    else:
        print('Yay!')

=======
Suggestion 4

def main():
    # 读取输入
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())

    # 用列表存储天线坐标
    antenna = [a, b, c, d, e]

    # 遍历列表，判断是否有天线间距大于k
    for i in range(0, 4):
        for j in range(i+1, 5):
            if antenna[j] - antenna[i] > k:
                print(':(')
                return

    # 若没有天线间距大于k，则输出Yay!
    print('Yay!')

=======
Suggestion 5

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    k = int(input())
    if e - a > k:
        print(":(")
    else:
        print("Yay!")

=======
Suggestion 6

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
