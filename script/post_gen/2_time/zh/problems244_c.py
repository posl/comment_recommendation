Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n=int(input())
    m=2*n+1
    l=[i for i in range(1,m+1)]
    for i in range(n):
        a=int(input())
        l.remove(a)
        b=max([j for j in l if j<a])
        l.remove(b)
        print(b)
        c=int(input())
        l.remove(c)
        d=max([j for j in l if j<c])
        l.remove(d)
        print(d)
main()

=======
Suggestion 2

def main():
    n = int(input())
    a = 1
    b = 2*n
    while True:
        print(a)
        a = int(input())
        if a == 0:
            exit()
        elif a > b:
            print(a)
            exit()
        else:
            b = 2*a+1
main()

=======
Suggestion 3

def main():
    n = int(input())
    # 1
    print(1)
    # 3
    num = int(input())
    if num == 2:
        print(3)
    else:
        print(2)
    # 5
    num = int(input())
    if num == 4:
        print(5)
    else:
        print(4)
    # 7
    num = int(input())
    if num == 6:
        print(7)
    else:
        print(6)

=======
Suggestion 4

def main():
    n = int(input())
    num = n*2+1
    i = 1
    while True:
        print(i)
        i = int(input())
        if i == 0:
            break
        else:
            i = num-i
            num = i
main()
#解题思路
#高桥和青木将互相进行以下游戏。
#从高桥开始，两人交替宣布1到2N+1（包括）之间的一个整数，直到游戏结束。
#任何一方宣布的整数都不能被任何一方再次宣布。
#不再能宣布整数的一方输了；没输的一方赢了。
#在这个游戏中，高桥将永远是赢家。
#你的任务是代表高桥实际进行游戏并赢得游戏。

=======
Suggestion 5

def get_input():
    n = int(input())
    return n

=======
Suggestion 6

def main():
    # 读取输入
    n = int(input())
    # 处理
    # 输出
    print(1)
    # 读取输入
    n = int(input())
    # 处理
    # 输出
    print(2)
    # 读取输入
    n = int(input())
    # 处理
    # 输出
    print(5)
    # 读取输入
    n = int(input())
    # 处理
    # 输出
    print(6)
    # 读取输入
    n = int(input())
    # 处理
    # 输出
    print(8)
    # 读取输入
    n = int(input())
    # 处理
    # 输出
    print(9)
    # 读取输入
    n = int(input())
    # 处理
    # 输出
    print(11)
    # 读取输入
    n = int(input())
    # 处理
    # 输出
    print(12)
    # 读取输入
    n = int(input())
    # 处理
    # 输出
    print(14)
    # 读取输入
    n = int(input())
    # 处理
    # 输出
    print(15)
    # 读取输入
    n = int(input())
    # 处理
    # 输出
    print(17)
    # 读取输入
    n = int(input())
    # 处理
    # 输出
    print(18)
    # 读取输入
    n = int(input())
    # 处理
    # 输出
    print(20)
    # 读取输入
    n = int(input())
    # 处理
    # 输出
    print(21)
    # 读取输入
    n = int(input())
    # 处理
    # 输出
    print(23)
    # 读取输入
    n = int(input())
    # 处理
    # 输出
    print(24)
    # 读取输入
    n = int(input())
    # 处理
    # 输出
    print(26)
    # 读取输入
    n = int(input())
    # 处理
    # 输出

=======
Suggestion 7

def main():
    n = int(input())
    a = 1
    b = 2*n+1
    while True:
        print(a)
        a = int(input())
        if a == 0:
            break
        print(b)
        b = int(input())
        if b == 0:
            break
        if a < b:
            a = b
        else:
            b = a
main()

=======
Suggestion 8

def main():
    n = int(input())
    i = 1
    while True:
        print(i)
        x = int(input())
        if x == 0:
            break
        i = x
        if i >= 2 * n + 1:
            break

=======
Suggestion 9

def main():
    n = int(input())
    #print(1)
    #print(2)
    #print(3)
    #print(4)
    #print(5)
    #print(6)
    #print(7)
    #print(8)
    #print(9)
    #print(10)
    #print(11)
    #print(12)
    #print(13)
    #print(14)
    #print(15)
    #print(16)
    #print(17)
    #print(18)
    #print(19)
    #print(20)
    #print(21)
    #print(22)
    #print(23)
    #print(24)
    #print(25)
    #print(26)
    #print(27)
    #print(28)
    #print(29)
    #print(30)
    #print(31)
    #print(32)
    #print(33)
    #print(34)
    #print(35)
    #print(36)
    #print(37)
    #print(38)
    #print(39)
    #print(40)
    #print(41)
    #print(42)
    #print(43)
    #print(44)
    #print(45)
    #print(46)
    #print(47)
    #print(48)
    #print(49)
    #print(50)
    #print(51)
    #print(52)
    #print(53)
    #print(54)
    #print(55)
    #print(56)
    #print(57)
    #print(58)
    #print(59)
    #print(60)
    #print(61)
    #print(62)
    #print(63)
    #print(64)
    #print(65)
    #print(66)
    #print(67)
    #print(68)
    #print(69)
    #print(70)
    #print(71)
    #print(72)
    #print(73)
    #print(74)
    #print(75)
    #print(76)
    #print(77)
    #print(78)
    #print(79)
    #print(80)
    #print(81)
    #print(82)
