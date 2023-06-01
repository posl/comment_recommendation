Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    R,C=map(int,input().split())
    if R%2==0:
        if C%2==0:
            print("白色")
        else:
            print("黑色")
    else:
        if C%2==0:
            print("黑色")
        else:
            print("白色")
main()

=======
Suggestion 2

def main():
    # 读取输入
    r, c = map(int, input().split())

    # 判断
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
    R, C = map(int, input().split())
    if (R + C) % 2 == 0:
        print("黑色")
    else:
        print("白色")

=======
Suggestion 4

def main():
    R, C = input().split()
    R = int(R)
    C = int(C)
    if (R + C) % 2 == 0:
        print('黑色')
    else:
        print('白色')

=======
Suggestion 5

def main():
    r,c = map(int,input().split())
    if (r + c) % 2 == 0:
        print("黑色")
    else:
        print("白色")

=======
Suggestion 6

def main():
    R, C = input().split()
    R = int(R)
    C = int(C)
    if (R + C) % 2 == 0:
        print("黑色")
    else:
        print("白色")

=======
Suggestion 7

def get_color(r,c):
    return "黑色" if (r+c)%2 == 0 else "白色"

=======
Suggestion 8

def main():
    r,c = map(int,input().split())
    if r%2==0:
        if c%2==0:
            print("白色")
        else:
            print("黑色")
    else:
        if c%2==0:
            print("黑色")
        else:
            print("白色")

=======
Suggestion 9

def main():
    R,C = map(int,input().split())
    if R%2 == 0 and C%2 == 0:
        print("白色")
    elif R%2 == 0 and C%2 != 0:
        print("黑色")
    elif R%2 != 0 and C%2 == 0:
        print("黑色")
    elif R%2 != 0 and C%2 != 0:
        print("白色")
