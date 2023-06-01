Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = float(input())
    print(round(x))

=======
Suggestion 2

def solve():
    x = input()
    if '.' in x:
        x = x.split('.')[0]
    print(x)

=======
Suggestion 3

def main():
    X = input()
    print(round(float(X)))

=======
Suggestion 4

def solve():
    x = float(input())
    print(round(x))

=======
Suggestion 5

def main():
    # 读取输入
    input = raw_input()
    # 处理输入
    # 输出结果
    print int(round(float(input)))

=======
Suggestion 6

def main():
    x = input()
    if x.find('.') != -1:
        x = x[:x.find('.')]
    print(x)

=======
Suggestion 7

def round_up(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

x = float(input())
print(round_up(x))

=======
Suggestion 8

def round(x):
    if x == int(x):
        print(int(x))
    else:
        print(round(x))
