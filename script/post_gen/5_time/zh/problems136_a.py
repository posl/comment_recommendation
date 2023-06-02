Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A,B,C = map(int,input().split())
    print(max(0,C-(A-B)))

=======
Suggestion 2

def main():

    # read inputs
    A, B, C = map(int, input().split())

    # process
    if B >= A:
        print(C)
    else:
        print(C - (A - B))

=======
Suggestion 3

def water_transfer(a, b, c):
    # 1号瓶最多可以装A毫升的水，现在它装有B毫升的水。
    # 2号瓶里有C毫升的水。
    # 我们将尽可能地把水从瓶子2转移到瓶子1。
    # 2号瓶中还会有多少水？
    # 限制条件
    # 输入的所有数值都是整数。
    # 1 ≦ B ≦ A ≦ 20
    # 1 ≦ C ≦ 20
    # 输入
    # 输入是由标准输入提供的，格式如下：
    # A B C
    # 输出
    # 打印代表2号瓶中剩余水量的整数，单位是毫升。
    # 输入样本1
    # 6 4 3
    # 样本输出 1
    # 1
    # 我们将把2毫升的水从2号瓶转移到1号瓶，1毫升的水将留在2号瓶中。
    # 输入样本2
    # 8 3 9
    # 样品输出2
    # 4
    # 输入样本3
    # 12 3 7
    # 样品输出3
    # 0
    # 1. 2号瓶中的水量
    # 2. 从2号瓶中转移到1号瓶中的水量
    # 3. 2号瓶中剩余的水量
    # 4. 1号瓶中的水量
    # 5. 1号瓶中的剩余空间
    # 6. 2号瓶中的剩余空间
    # 7. 1号瓶中的剩余空间和2号瓶中的剩余空间中的较小值
    #

=======
Suggestion 4

def main():
    # 读取输入
    A, B, C = map(int, input().split())
    # 从瓶子2转移到瓶子1
    B = B + C
    # 瓶子2中剩余的水
    C = 0
    # 瓶子1中最多可以装多少水
    D = A
    # 瓶子1中剩余的水
    A = A - B
    # 瓶子1中剩余的水
    B = B - D
    # 瓶子2中剩余的水
    C = C + B
    # 输出结果
    print(C)
# 调用主函数

=======
Suggestion 5

def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 从瓶子2转移到瓶子1
    b += c
    # 2号瓶中还会有多少水？
    print(b if b < a else a)

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    print(c if a >= b+c else a+b-c)

=======
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    print(c - (a - b) if c > a - b else 0)

=======
Suggestion 8

def pour_water(a,b,c):
    if a >= b+c:
        return 0
    elif a >= b:
        return c-(a-b)
    else:
        return c-(a-b)

=======
Suggestion 9

def main():
    a,b,c = map(int,input().split())
    if a > b + c:
        print(0)
    else:
        print(c - (a - b))
