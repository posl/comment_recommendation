Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    import sys
    try:
        input = sys.stdin.readline
        x = float(input())
        print(int(x+0.5))
    except:
        print("输入有误")

=======
Suggestion 2

def main():
    # 读取输入
    x = input()
    # 四舍五入
    x = round(float(x))
    # 打印结果
    print(x)

=======
Suggestion 3

def round(x):
    if x.isdecimal():
        return x
    else:
        if '.' in x:
            x = x.split('.')
            if x[1][0] >= '5':
                x[0] = str(int(x[0]) + 1)
            return x[0]
        else:
            return x

x = input()
print(round(x))

=======
Suggestion 4

def main():
    x = float(input())
    print(round(x))

=======
Suggestion 5

def main():
    x = input()
    if '.' in x:
        x = x.split('.')[0]
    print(x)

=======
Suggestion 6

def main():
    x = input()
    if '.' in x:
        print(int(float(x)+0.5))
    else:
        print(x)

=======
Suggestion 7

def main():
    x = input()
    x = float(x)
    print(round(x))

=======
Suggestion 8

def main():
    x = input()
    print(round(float(x)))

=======
Suggestion 9

def main():
    #get input
    x = input()
    #convert to float
    x = float(x)
    #round to nearest integer
    x = round(x)
    #print result
    print(x)

=======
Suggestion 10

def main():
    x = input()
    if x.find('.') == -1:
        print(x)
    else:
        x = x.split('.')
        if int(x[1][0]) >= 5:
            print(int(x[0]) + 1)
        else:
            print(int(x[0]))
