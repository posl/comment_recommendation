Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = [int(x) for x in input().split()]
    for i in range(3):
        a = [a[x] for x in a]
    print(a[0])

=======
Suggestion 2

def problems241_a():
    a = raw_input()
    a = a.split()
    a = map(int, a)
    k = 0
    for i in range(3):
        k = a[k]
    print k

=======
Suggestion 3

def problems241_a(a):
    n = 0
    for i in range(10):
        n = a[n]
    return n

=======
Suggestion 4

def main():
    a = input().split()
    b = []
    for i in range(10):
        b.append(int(a[i]))
    c = []
    d = 0
    while True:
        if not b[d] in c:
            c.append(b[d])
        else:
            break
        d = b[d]
    print(d)

=======
Suggestion 5

def get_next_number(number):
    return number_list[number]

number_list = list(map(int, input().split()))
number = 0
for _ in range(3):
    number = get_next_number(number)
print(number)

=======
Suggestion 6

def get_next_num(num):
    return a[num]

=======
Suggestion 7

def get_next_value(value, array):
    return array[value]

=======
Suggestion 8

def cal(a):
    if a==0:
        return 9
    else:
        return a-1

=======
Suggestion 9

def main():
    a = list(map(int, input().split()))
    b = [0] * 10
    for i in range(10):
        b[a[i]] = i
    for i in range(3):
        b = [b[a[i]] for i in range(10)]
    print(b[0])

=======
Suggestion 10

def problems241_a():
    #读取输入
    a = [int(x) for x in input().split()]
    #初始化
    #k为屏幕上显示的数字
    k = 0
    #循环
    for i in range(3):
        k = a[k]
    #输出
    print(k)
