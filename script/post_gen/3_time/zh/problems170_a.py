Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = list(map(int, input().split()))
    for i in range(5):
        if x[i] == 0:
            print(i+1)
            break

=======
Suggestion 2

def main():
    # 读入数据
    x = input().split()
    # 处理数据
    for i in range(0, 5):
        if x[i] == '0':
            print(i+1)
            break

=======
Suggestion 3

def main():
    x = list(map(int, input().split()))
    for i in range(5):
        if x[i] == 0:
            print(i+1)

=======
Suggestion 4

def main():
    # 读取输入
    x = list(map(int, input().split()))

    # 处理
    for i in range(5):
        if x[i] == 0:
            print(i + 1)
            break

=======
Suggestion 5

def main():
    x = list(map(int, input().split()))
    print(x.index(0)+1)

=======
Suggestion 6

def problems170_a():
    x = input().split()
    for i in range(len(x)):
        if x[i] == '0':
            print(i+1)
            break

=======
Suggestion 7

def main():
    x = input().split()
    for i in range(5):
        if x[i] == "0":
            print(i+1)
            break

=======
Suggestion 8

def main():
    x = input().split()
    for i in range(5):
        if x[i] == '0':
            print(i+1)
