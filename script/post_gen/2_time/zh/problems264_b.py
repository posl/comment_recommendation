Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    R, C = map(int, input().split())
    if (R + C) % 2 == 0:
        print("黑色")
    else:
        print("白色")

=======
Suggestion 2

def main():
    # 读取输入
    r, c = map(int, input().split())
    # 逻辑处理
    if r % 2 == 0:
        if c % 2 == 0:
            print('白色')
        else:
            print('黑色')
    else:
        if c % 2 == 0:
            print('黑色')
        else:
            print('白色')

=======
Suggestion 3

def main():
    r, c = map(int, input().split())
    if (r + c) % 2 == 0:
        print("黑色")
    else:
        print("白色")

=======
Suggestion 4

def main():
    row, col = map(int, input().split())
    if row % 2 == 0:
        if col % 2 == 0:
            print("black")
        else:
            print("white")
    else:
        if col % 2 == 0:
            print("white")
        else:
            print("black")

=======
Suggestion 5

def main():
    #读取输入
    r, c = map(int, input().split())

    #处理
    #判断是不是偶数行偶数列
    if r % 2 == 0 and c % 2 == 0:
        print('黑色')
    elif r % 2 != 0 and c % 2 != 0:
        print('黑色')
    else:
        print('白色')

=======
Suggestion 6

def main():
    r,c = map(int,input().split())
    if (r+c)%2 == 0:
        print('黑色')
    else:
        print('白色')

=======
Suggestion 7

def main():
    # 读入数据
    r, c = input().split()
    r = int(r)
    c = int(c)
    # 计算结果
    if r % 2 == 0:
        if c % 2 == 0:
            print("black")
        else:
            print("white")
    else:
        if c % 2 == 0:
            print("white")
        else:
            print("black")

main()

=======
Suggestion 8

def main():
    R,C = map(int,input().split())
    for i in range(R):
        if i%2 == 0:
            for j in range(C):
                if j%2 == 0:
                    print('#',end='')
                else:
                    print('.',end='')
        else:
            for j in range(C):
                if j%2 == 0:
                    print('.',end='')
                else:
                    print('#',end='')
        print()
