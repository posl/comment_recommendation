Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k, x = map(int, input().split())
    if k * 500 >= x:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    k,x = map(int, input().split())
    if k*500 >= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def is_enough(coin, money):
    if (coin * 500) >= money:
        return True
    else:
        return False

=======
Suggestion 4

def main():
    # 读取输入
    inputs = input()
    # 分割字符串
    inputs = inputs.split()
    # 转换为整数
    k = int(inputs[0])
    x = int(inputs[1])
    # 判断
    if k * 500 >= x:
        print("是")
    else:
        print("否")

=======
Suggestion 5

def main():
    # 1.输入
    # 2.处理
    # 3.输出
    # 1.输入
    k, x = map(int, input().split())
    # 2.处理
    if k * 500 >= x:
        print("Yes")
    else:
        print("No")
    # 3.输出

=======
Suggestion 6

def main():
    print("请输入硬币的个数和金钱数")
    k,x = map(int,input().split())
    if k*500 >= x:
        print("否")
    else:
        print("是")
