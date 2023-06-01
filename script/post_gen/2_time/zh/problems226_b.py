Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = float(input())
    if x < 0 or x >= 100:
        return
    y = x * 10
    if y % 10 >= 5:
        print(int(x) + 1)
    else:
        print(int(x))

=======
Suggestion 2

def main():
    x = float(input())
    print(round(x))

=======
Suggestion 3

def main():
    # 读取输入
    x = float(input())
    # 四舍五入
    # round()函数返回浮点数x的四舍五入值。
    # round(x,n)函数返回浮点数x的四舍五入值，n表示要保留的小数位数。
    # round()函数的返回值是一个浮点数，而不是一个整数。
    # round()函数的返回值是一个浮点数，而不是一个整数。
    # round()函数的返回值是一个浮点数，而不是一个整数。
    # 请记住这一点，以避免误解。
    print(round(x))

=======
Suggestion 4

def main():
    x = float(input())
    y = int(x*10)%10
    if y < 5:
        print(int(x))
    else:
        print(int(x)+1)

=======
Suggestion 5

def get_input():
    num = float(input())
    return num

=======
Suggestion 6

def main():
    x = float(input())
    x = x + 0.001
    print(int(x))
