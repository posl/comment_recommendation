Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def replace1with9(n):
    return int(str(n).replace('1','x').replace('9','1').replace('x','9'))

=======
Suggestion 2

def replace_1_9(n):
    return int(str(n).replace('1', 'a').replace('9', '1').replace('a', '9'))

=======
Suggestion 3

def swap(num):
    num = str(num)
    num = num.replace('1','x')
    num = num.replace('9','1')
    num = num.replace('x','9')
    return num

=======
Suggestion 4

def problems111_a():
    n = input("请输入一个三位数：")
    if 111 <= int(n) <= 999:
        result = ''
        for i in n:
            if i == '1':
                result += '9'
            else:
                result += '1'
        print(result)
    else:
        print("输入的数字不符合要求，请重新输入！")
        problems111_a()

problems111_a()

=======
Suggestion 5

def main():
    n = int(input())
    print(1110-n)

=======
Suggestion 6

def main():
    n = input()
    for i in range(len(n)):
        if n[i] == '1':
            print('9', end='')
        else:
            print('1', end='')
main()

=======
Suggestion 7

def main():
    n = input()
    n = n.replace('1','x')
    n = n.replace('9','1')
    n = n.replace('x','9')
    print(n)

=======
Suggestion 8

def main():
    n = input()
    for i in range(len(n)):
        if n[i] == '1':
            print('9', end='')
        elif n[i] == '9':
            print('1', end='')
        else:
            print(n[i], end='')
