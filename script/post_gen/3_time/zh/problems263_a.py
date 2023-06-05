Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    input_str = input()
    input_list = input_str.split()
    input_list = [int(x) for x in input_list]
    input_list.sort()
    if input_list[0] == input_list[1] and input_list[1] == input_list[2] and input_list[3] == input_list[4]:
        print("Yes")
    elif input_list[0] == input_list[1] and input_list[2] == input_list[3] and input_list[3] == input_list[4]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    # 读入数据
    line = input()
    # 分割数据
    line = line.split()
    # 数据转换
    line = list(map(int, line))
    # 排序
    line.sort()
    # 判断是否为满堂红
    if line[0] == line[1] and line[3] == line[4] and (line[0] != line[3] or line[0] != line[4]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a = input().split()
    a.sort()
    if a[0] == a[1] and a[1] == a[2] and a[3] == a[4]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    a,b,c,d,e = map(int,input().split())
    if a == b and b == c:
        if d == e:
            print('Yes')
        else:
            print('No')
    elif b == c and c == d:
        if a == e:
            print('Yes')
        else:
            print('No')
    elif c == d and d == e:
        if a == b:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 5

def main():
    #读取输入
    a,b,c,d,e = map(int,input().split())
    #定义一个列表，存放5张牌
    list1 = [a,b,c,d,e]
    #定义一个字典，存放每张牌出现的次数
    dict1 = {}
    #遍历列表，统计每张牌出现的次数
    for i in list1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    #如果字典中有三个key，且每个key对应的value都为3，则满足条件
    if len(dict1) == 3 and max(dict1.values()) == 3 and min(dict1.values()) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    #input
    a = input()
    b = input()
    c = input()
    d = input()
    e = input()
    #output
    if a == b and b == c:
        if d == e:
            print('Yes')
        else:
            print('No')
    elif a == b and b == d:
        if c == e:
            print('Yes')
        else:
            print('No')
    elif a == b and b == e:
        if c == d:
            print('Yes')
        else:
            print('No')
    elif a == c and c == d:
        if b == e:
            print('Yes')
        else:
            print('No')
    elif a == c and c == e:
        if b == d:
            print('Yes')
        else:
            print('No')
    elif a == d and d == e:
        if b == c:
            print('Yes')
        else:
            print('No')
    elif b == c and c == d:
        if a == e:
            print('Yes')
        else:
            print('No')
    elif b == c and c == e:
        if a == d:
            print('Yes')
        else:
            print('No')
    elif b == d and d == e:
        if a == c:
            print('Yes')
        else:
            print('No')
    elif c == d and d == e:
        if a == b:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 7

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[1] and a[1] == a[2] and a[3] == a[4]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    cards = input().split()
    cards.sort()
    if cards[0] == cards[1] and cards[1] == cards[2] and cards[3] == cards[4]:
        print("Yes")
    elif cards[0] == cards[1] and cards[2] == cards[3] and cards[3] == cards[4]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    a,b,c,d,e = map(int,input().split())
    if a == b == c:
        if d == e:
            print('Yes')
        else:
            print('No')
    elif a == b == d:
        if c == e:
            print('Yes')
        else:
            print('No')
    elif a == b == e:
        if c == d:
            print('Yes')
        else:
            print('No')
    elif a == c == d:
        if b == e:
            print('Yes')
        else:
            print('No')
    elif a == c == e:
        if b == d:
            print('Yes')
        else:
            print('No')
    elif a == d == e:
        if b == c:
            print('Yes')
        else:
            print('No')
    elif b == c == d:
        if a == e:
            print('Yes')
        else:
            print('No')
    elif b == c == e:
        if a == d:
            print('Yes')
        else:
            print('No')
    elif b == d == e:
        if a == c:
            print('Yes')
        else:
            print('No')
    elif c == d == e:
        if a == b:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

main()

=======
Suggestion 10

def main():
    # 读取输入
    a, b, c, d, e = map(int, input().split())

    # 计算
    if a == b == c:
        if d == e:
            print("Yes")
        else:
            print("No")
    elif a == b == d:
        if c == e:
            print("Yes")
        else:
            print("No")
    elif a == b == e:
        if c == d:
            print("Yes")
        else:
            print("No")
    elif a == c == d:
        if b == e:
            print("Yes")
        else:
            print("No")
    elif a == c == e:
        if b == d:
            print("Yes")
        else:
            print("No")
    elif a == d == e:
        if b == c:
            print("Yes")
        else:
            print("No")
    elif b == c == d:
        if a == e:
            print("Yes")
        else:
            print("No")
    elif b == c == e:
        if a == d:
            print("Yes")
        else:
            print("No")
    elif b == d == e:
        if a == c:
            print("Yes")
        else:
            print("No")
    elif c == d == e:
        if a == b:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
