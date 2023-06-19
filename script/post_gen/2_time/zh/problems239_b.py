Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读入数据
    x = int(input())
    # 计算结果
    result = int(x / 10)
    # 输出结果
    print(result)

main()

=======
Suggestion 2

def main():
    num = int(input())
    print(num//10)

=======
Suggestion 3

def floor(x):
    if x>=0:
        return x//10
    else:
        return -(-x//10)

=======
Suggestion 4

def main():
    X = int(input())
    print(X//10)

=======
Suggestion 5

def main():
    x = int(input())
    print(x // 10)

=======
Suggestion 6

def floor(x):
    if x >= 0:
        return x // 10
    else:
        return -((-x + 9) // 10)


x = int(input())
print(floor(x))

=======
Suggestion 7

def floor(x):
    if x >= 0:
        return int(x)
    else:
        return int(x) - 1

print(floor(int(input()) / 10))

=======
Suggestion 8

def main():
    x = int(input())
    print(int(x/10))
