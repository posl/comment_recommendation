Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = input().split()
    for i in range(5):
        if x[i] == '0':
            print(i+1)
            break

=======
Suggestion 2

def find_zero():
    x = input().split()
    for i in range(len(x)):
        if x[i] == '0':
            return i + 1

print(find_zero())

=======
Suggestion 3

def main():
    x = list(map(int, input().split()))
    for i in range(5):
        if x[i] == 0:
            print(i+1)
            break

=======
Suggestion 4

def main():
    # 读取输入
    x = input()

    # 处理输入
    x = x.split(" ")
    x = [int(i) for i in x]

    # 处理输出
    print(x.index(0)+1)

=======
Suggestion 5

def main():
    str = input()
    str = str.split()
    for i in range(0, len(str)):
        if str[i] == '0':
            print(i+1)
            break

=======
Suggestion 6

def main():
    x = list(map(int,input().split()))
    print(x.index(0)+1)

=======
Suggestion 7

def main():
    import sys
    x = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(5):
        if x[i] == 0:
            print(i+1)
            break

=======
Suggestion 8

def main():
    #input
    x = list(map(int, input().split()))

    #search
    for i in range(5):
        if x[i] == 0:
            print(i+1)
            break

=======
Suggestion 9

def main():
    str = input()
    str_split = str.split()
    for i in range(0, 5):
        if str_split[i] == '0':
            print(i+1)
