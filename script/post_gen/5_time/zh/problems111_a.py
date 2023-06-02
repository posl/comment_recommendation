Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    #读取一个字符串
    n = input()
    #替换
    n = n.replace('1', 'a')
    n = n.replace('9', '1')
    n = n.replace('a', '9')
    #输出结果
    print(n)

=======
Suggestion 2

def replace(n):
    return int(str(n).replace('1','2').replace('9','1').replace('2','9'))

=======
Suggestion 3

def exchange(num):
    num = str(num)
    num = num.replace('1','a')
    num = num.replace('9','1')
    num = num.replace('a','9')
    return int(num)

=======
Suggestion 4

def main():
    n = input()
    print(n.replace('1', 'x').replace('9', '1').replace('x', '9'))

=======
Suggestion 5

def replace1with9and9with1(n):
    n1 = n // 100
    n2 = n // 10 % 10
    n3 = n % 10
    n1 = 9 if n1 == 1 else 1
    n2 = 9 if n2 == 1 else 1
    n3 = 9 if n3 == 1 else 1
    return n1 * 100 + n2 * 10 + n3

=======
Suggestion 6

def main():
    n = int(input())
    print(1110 - n)

=======
Suggestion 7

def problem111_a():
    n = input()
    print(n.replace('1', 'a').replace('9', '1').replace('a', '9'))

=======
Suggestion 8

def problem111_a():
    n = input()
    n = n.replace('1','2')
    n = n.replace('9','1')
    n = n.replace('2','9')
    print(n)

=======
Suggestion 9

def main():
    num = input()
    num = num.replace('1','a').replace('9','1').replace('a','9')
    print(num)
