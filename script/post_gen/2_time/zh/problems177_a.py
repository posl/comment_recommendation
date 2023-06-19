Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    #input
    input_line = input()
    input_list = input_line.split(' ')
    D = int(input_list[0])
    T = int(input_list[1])
    S = int(input_list[2])
    #calc
    if D <= T * S:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    # 读取输入
    D, T, S = map(int, input().split())

    # 判断
    if T * S >= D:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def problem177_a():
    D, T, S = map(int, input().split())
    if D / S <= T:
        print("Yes")
    else:
        print("No")

problem177_a()

=======
Suggestion 4

def problem177_a():
    D,T,S = map(int,input().split())
    if D <= T*S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    D,T,S = map(int,input().split())
    if D/S <= T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    line = input().split()
    D = int(line[0])
    T = int(line[1])
    S = int(line[2])
    if D % S == 0:
        if D / S <= T:
            print("Yes")
        else:
            print("No")
    else:
        if D / S < T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    d,t,s = map(int,input().split())
    if d/s <= t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def problem177_a():
    d, t, s = map(int, input().split())
    if d <= t * s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    # 读取输入
    line = input()
    # 分割输入
    D, T, S = line.split()
    # 转换为数字
    D = int(D)
    T = int(T)
    S = int(S)
    # 计算
    if D <= T * S:
        print("Yes")
    else:
        print("No")
    return

=======
Suggestion 10

def problem177_a():

    D, T, S = map(int, input().split())

    if D / S <= T:
        print("Yes")
    else:
        print("No")
