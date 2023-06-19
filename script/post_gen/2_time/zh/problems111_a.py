Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读取输入
    n = int(input("请输入一个由数字1和9组成的整数(111 ≦ n ≦ 999)："))
    # 计算
    n = 1110 - n
    # 输出结果
    print(n)

=======
Suggestion 2

def replace(n):
    n = str(n)
    n = n.replace('1', 'x')
    n = n.replace('9', '1')
    n = n.replace('x', '9')
    return int(n)

n = int(input())
print(replace(n))

=======
Suggestion 3

def main():
    n = int(input())
    n = str(n)
    n = n.replace('1','a')
    n = n.replace('9','1')
    n = n.replace('a','9')
    print(n)

=======
Suggestion 4

def main():
    n = input()
    n = n.replace('1', 'a')
    n = n.replace('9', '1')
    n = n.replace('a', '9')
    print(n)

=======
Suggestion 5

def replace(n):
    n = str(n)
    n = n.replace("1","x")
    n = n.replace("9","1")
    n = n.replace("x","9")
    return int(n)

n = input()
print(replace(n))

=======
Suggestion 6

def main():
    n = input()
    s = ""
    for i in n:
        if i == '1':
            s += '9'
        elif i == '9':
            s += '1'
    print(s)

=======
Suggestion 7

def reverse(n):
    n = str(n)
    n = n[::-1]
    return n

=======
Suggestion 8

def main():
    n = int(input())
    print(1110-n)

=======
Suggestion 9

def main():
    n = input()
    for i in range(len(n)):
        if n[i] == '1':
            print(9, end='')
        else:
            print(1, end='')
