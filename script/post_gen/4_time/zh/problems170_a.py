Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = list(map(int, input().split()))
    for i in range(len(x)):
        if x[i] == 0:
            print(i+1)
            break

=======
Suggestion 2

def main():
    # 读取输入
    x = list(map(int, input().split()))
    # 找出0所在的下标
    print(x.index(0) + 1)

=======
Suggestion 3

def main():
    x = input()
    x = x.split()
    for i in range(5):
        if x[i] == '0':
            print(i+1)
            break

=======
Suggestion 4

def solve():
    x = list(map(int, input().split()))
    for i in range(5):
        if x[i] == 0:
            print(i+1)
            break

=======
Suggestion 5

def main():
    x = input().split()
    x = [int(i) for i in x]
    for i in range(5):
        if x[i] == 0:
            print(i+1)
            break

=======
Suggestion 6

def main():
    x = list(map(int, input().split()))
    for i in range(5):
        if x[i] == 0:
            print(i+1)
            break

=======
Suggestion 7

def main():
    # 读取输入
    x = input().split(" ")
    # print(x)
    # print(type(x))
    for i in range(0, 5):
        if x[i] == "0":
            print(i + 1)
            break

=======
Suggestion 8

def main():
    x = input().split(" ")
    for i in range(len(x)):
        if x[i] == "0":
            print(i + 1)

=======
Suggestion 9

def main():
    x = input().split()
    for i in range(5):
        if int(x[i]) == 0:
            print(i+1)
            break
