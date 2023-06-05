Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读取输入
    x = float(input())
    # 输出结果
    print(round(x))

=======
Suggestion 2

def round_off(x):
    if x < 0.25:
        return 0
    elif x < 0.75:
        return 0.5
    else:
        return 1

=======
Suggestion 3

def main():
    x = float(input())
    if x - int(x) >= 0.5:
        print(int(x) + 1)
    else:
        print(int(x))

=======
Suggestion 4

def round(x):
    if 0 <= x and x < 100:
        if x < 10:
            return 0
        elif x < 100:
            return 1
        else:
            return 2
    else:
        return -1

=======
Suggestion 5

def main():
    x = float(input())
    print(round(x))

=======
Suggestion 6

def round():
    x = float(input())
    print(round(x))
    return

round()

=======
Suggestion 7

def main():
    x = float(input())
    if x < 0:
        print("输入错误")
    elif x >= 100:
        print("输入错误")
    else:
        if x >= 0 and x < 0.5:
            print(0)
        elif x >= 0.5 and x < 1:
            print(1)
        elif x >= 1 and x < 1.5:
            print(1)
        elif x >= 1.5 and x < 2:
            print(2)
        elif x >= 2 and x < 2.5:
            print(2)
        elif x >= 2.5 and x < 3:
            print(3)
        elif x >= 3 and x < 3.5:
            print(3)
        elif x >= 3.5 and x < 4:
            print(4)
        elif x >= 4 and x < 4.5:
            print(4)
        elif x >= 4.5 and x < 5:
            print(5)
        elif x >= 5 and x < 5.5:
            print(5)
        elif x >= 5.5 and x < 6:
            print(6)
        elif x >= 6 and x < 6.5:
            print(6)
        elif x >= 6.5 and x < 7:
            print(7)
        elif x >= 7 and x < 7.5:
            print(7)
        elif x >= 7.5 and x < 8:
            print(8)
        elif x >= 8 and x < 8.5:
            print(8)
        elif x >= 8.5 and x < 9:
            print(9)
        elif x >= 9 and x < 9.5:
            print(9)
        elif x >= 9.5 and x < 10:
            print(10)
        elif x >= 10 and x < 10.5:
            print(10)
        elif x >= 10.5 and x < 11:
            print(11)
        elif x >= 11 and x < 11.5:
            print(11)
        elif x >= 11.5 and x < 12:
            print(12)
        elif x >= 12 and
