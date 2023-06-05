Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读取输入
    x, y = map(int, input().split())

    # 求解并输出
    print((y + 1) % 3)

=======
Suggestion 2

def main():
    x,y = map(int,input().split())
    if x == y:
        print(x)
    else:
        print(3-x-y)

=======
Suggestion 3

def main():
    x = input()
    y = input()
    if x == y:
        print(x)
    else:
        print(3 - int(x) - int(y))

main()

=======
Suggestion 4

def solve(x, y):
    if x == y:
        return x
    else:
        return 3 - x - y

=======
Suggestion 5

def rsp(x,y):
    if x == 0:
        if y == 0:
            return 0
        elif y == 1:
            return 2
        else:
            return 1
    elif x == 1:
        if y == 0:
            return 1
        elif y == 1:
            return 0
        else:
            return 2
    else:
        if y == 0:
            return 2
        elif y == 1:
            return 1
        else:
            return 0

x,y = map(int,input().split())
print(rsp(x,y))

=======
Suggestion 6

def get_input():
    x, y = map(int, input().split())
    return x, y

=======
Suggestion 7

def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        print(3-x-y)

main()

=======
Suggestion 8

def main():
    x, y = map(int, input().split())
    print((x - y + 3) % 3)
