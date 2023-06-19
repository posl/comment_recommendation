Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取输入
    line = input()
    # 用空格分隔输入的字符串
    line = line.split()
    # 将字符串转换为数值
    line = [int(x) for x in line]
    # 找出0
    for i in range(len(line)):
        if line[i] == 0:
            print(i+1)
            break

=======
Suggestion 2

def main():
    x = list(map(int, input().split()))
    for i in range(5):
        if x[i] == 0:
            print(i+1)

=======
Suggestion 3

def main():
    x = list(map(int, input().split()))
    for i in range(5):
        if x[i] == 0:
            print(i + 1)
            break

main()

=======
Suggestion 4

def main():
    # 读入数据
    x = list(map(int, input().split()))
    # 计算结果
    for i in range(5):
        if x[i] == 0:
            print(i + 1)
            break

=======
Suggestion 5

def main():
    x = input()
    x = x.split()
    for i in range(0,5):
        if x[i] == '0':
            print(i+1)
            break

=======
Suggestion 6

def main():
    n = input().split()
    for i in range(len(n)):
        if n[i] == '0':
            print(i+1)
            break

=======
Suggestion 7

def problems170_a(x):
    for i in range(len(x)):
        if x[i] == 0:
            return i+1

=======
Suggestion 8

def main():
    x = input().split()
    for i in range(len(x)):
        if x[i] == '0':
            print(i+1)

=======
Suggestion 9

def main():
    x = input()
    x = x.split()
    for i in range(0, len(x)):
        if x[i] == '0':
            print(i+1)
            break

=======
Suggestion 10

def main():
    x = list(map(int,input().split()))
    print(x.index(0)+1)
