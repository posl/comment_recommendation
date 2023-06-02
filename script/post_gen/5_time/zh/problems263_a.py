Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    cards = list(map(int, input().split()))
    cards.sort()
    if cards[0] == cards[1] and cards[1] == cards[2] and cards[3] == cards[4]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a = input().split()
    a.sort()
    if a[0] == a[1] and a[1] == a[2] and a[3] == a[4]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a,b,c,d,e = map(int, input().split())
    if a==b and b==c:
        if d==e:
            print("Yes")
        else:
            print("No")
    elif a==b and b==d:
        if c==e:
            print("Yes")
        else:
            print("No")
    elif a==b and b==e:
        if c==d:
            print("Yes")
        else:
            print("No")
    elif a==c and c==d:
        if b==e:
            print("Yes")
        else:
            print("No")
    elif a==c and c==e:
        if b==d:
            print("Yes")
        else:
            print("No")
    elif a==d and d==e:
        if b==c:
            print("Yes")
        else:
            print("No")
    elif b==c and c==d:
        if a==e:
            print("Yes")
        else:
            print("No")
    elif b==c and c==e:
        if a==d:
            print("Yes")
        else:
            print("No")
    elif b==d and d==e:
        if a==c:
            print("Yes")
        else:
            print("No")
    elif c==d and d==e:
        if a==b:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 4

def main():
    cards = input().split()
    cards.sort()
    if cards[0] == cards[1] and cards[1] == cards[2] and cards[3] == cards[4]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    #从标准输入读取
    a,b,c,d,e = map(int,input().split())
    #定义一个字典，key是数字，value是出现的次数
    dict = {
        a:0,
        b:0,
        c:0,
        d:0,
        e:0
    }
    #遍历输入的数字，统计每个数字出现的次数
    for i in [a,b,c,d,e]:
        dict[i] += 1
    #判断是否满足满堂红的条件
    #如果字典中有一个元素出现3次，另一个元素出现2次，则满足条件
    if 3 in dict.values() and 2 in dict.values():
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def isFullHouse(a,b,c,d,e):
    if a==b and a==c and d==e:
        return True
    elif a==b and c==d and c==e:
        return True
    else:
        return False

=======
Suggestion 7

def check_if_full_house(a,b,c,d,e):
    if a == b and b == c and d == e:
        return True
    elif a == b and c == d and d == e:
        return True
    else:
        return False

=======
Suggestion 8

def main():
    cards = input()
    cards = cards.split(" ")
    cards = [int(i) for i in cards]
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
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[1] and a[1] == a[2] and a[3] == a[4]:
        print('Yes')
    elif a[0] == a[1] and a[2] == a[3] and a[3] == a[4]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    a,b,c,d,e = map(int,input().split())
    if a == b and a == c and a != d and a != e:
        print("Yes")
    elif a == b and a == d and a != c and a != e:
        print("Yes")
    elif a == b and a == e and a != c and a != d:
        print("Yes")
    elif a == c and a == d and a != b and a != e:
        print("Yes")
    elif a == c and a == e and a != b and a != d:
        print("Yes")
    elif a == d and a == e and a != b and a != c:
        print("Yes")
    elif b == c and b == d and b != a and b != e:
        print("Yes")
    elif b == c and b == e and b != a and b != d:
        print("Yes")
    elif b == d and b == e and b != a and b != c:
        print("Yes")
    elif c == d and c == e and c != a and c != b:
        print("Yes")
    else:
        print("No")
