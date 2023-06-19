Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    order = [A,B,C,D,E]
    order.sort()
    #print(order)
    for i in range(5):
        if order[i] % 10 != 0:
            order[i] = order[i] + 10 - order[i] % 10
    #print(order)
    print(order[0]+order[1]+order[2]+order[3]+order[4])

=======
Suggestion 2

def main():
    # 读入数据
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    # 计算
    # 1.计算最后一道菜的最早送达时间
    # 2.计算最后一道菜的最早送达时间
    # 3.计算最后一道菜的最早送达时间
    # 4.计算最后一道菜的最早送达时间
    # 5.计算最后一道菜的最早送达时间
    # 6.计算最后一道菜的最早送达时间
    # 7.计算最后一道菜的最早送达时间
    # 8.计算最后一道菜的最早送达时间
    # 9.计算最后一道菜的最早送达时间
    # 10.计算最后一道菜的最早送达时间
    # 11.计算最后一道菜的最早送达时间
    # 12.计算最后一道菜的最早送达时间
    # 13.计算最后一道菜的最早送达时间
    # 14.计算最后一道菜的最早送达时间
    # 15.计算最后一道菜的最早送达时间
    # 16.计算最后一道菜的最早送达时间
    # 17.计算最后一道菜的最早送达时间
    # 18.计算最后一道菜的最早送达时间
    # 19.计算最后一道菜的最早送达时间
    # 20.计算最后一道菜的最早送达时间
    # 21.计算最后一道菜的最早送达时间
    # 22.计算最后一道菜的

=======
Suggestion 3

def main():
    # input
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    # compute
    # 1. 10的倍数的时间下单
    # 2. 每次只能点一道菜
    # 3. 当一个订单已经下了，而菜品仍未送达时，不能再下新的订单，但可以在菜品送达的确切时间下新的订单
    # 4. E869120在时间0到达这家餐厅，他将订购全部五道菜。找出最后一道菜的最早送达时间。
    # 5. 在这里，他可以按他喜欢的任何顺序点菜，而且他可以在时间0时已经下单。
    # 6. A，B，C，D和E是1到123之间的整数（包括在内）。

    # output
    print(10 * ((A + 9) // 10) + 10 * ((B + 9) // 10) + 10 * ((C + 9) // 10) + 10 * ((D + 9) // 10) + 10 * ((E + 9) // 10) - 10)

=======
Suggestion 4

def main():
    a,b,c,d,e = map(int,input().split())
    print(max((a+9)//10*10,(b+9)//10*10,(c+9)//10*10,(d+9)//10*10,(e+9)//10*10)+e)

=======
Suggestion 5

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(10 * ((a - 1) // 10 + 1) + 10 + (b - 1) % 10 + (c - 1) % 10 + (d - 1) % 10 + (e - 1) % 10)

=======
Suggestion 6

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    #print(a,b,c,d,e)
    t = [a,b,c,d,e]
    #print(t)
    t.sort()
    #print(t)
    for i in range(5):
        if t[i]%10 == 0:
            continue
        else:
            t[i] = (t[i]//10 + 1)*10
    #print(t)
    print(sum(t))

=======
Suggestion 7

def problem123_b():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    a1 = a%10
    b1 = b%10
    c1 = c%10
    d1 = d%10
    e1 = e%10
    if a1 == 0:
        a2 = a
    else:
        a2 = a + (10 - a1)
    if b1 == 0:
        b2 = b
    else:
        b2 = b + (10 - b1)
    if c1 == 0:
        c2 = c
    else:
        c2 = c + (10 - c1)
    if d1 == 0:
        d2 = d
    else:
        d2 = d + (10 - d1)
    if e1 == 0:
        e2 = e
    else:
        e2 = e + (10 - e1)
    if a2 >= b2 and a2 >= c2 and a2 >= d2 and a2 >= e2:
        print(a2)
    elif b2 >= a2 and b2 >= c2 and b2 >= d2 and b2 >= e2:
        print(b2)
    elif c2 >= a2 and c2 >= b2 and c2 >= d2 and c2 >= e2:
        print(c2)
    elif d2 >= a2 and d2 >= b2 and d2 >= c2 and d2 >= e2:
        print(d2)
    elif e2 >= a2 and e2 >= b2 and e2 >= c2 and e2 >= d2:
        print(e2)

problem123_b()

=======
Suggestion 8

def problem123_b():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    if A % 10 != 0:
        A = (A // 10 + 1) * 10
    if B % 10 != 0:
        B = (B // 10 + 1) * 10
    if C % 10 != 0:
        C = (C // 10 + 1) * 10
    if D % 10 != 0:
        D = (D // 10 + 1) * 10
    if E % 10 != 0:
        E = (E // 10 + 1) * 10
    print(A + B + C + D + E)

=======
Suggestion 9

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    a = A
    b = B
    c = C
    d = D
    e = E
    if a % 10 != 0:
        a = a + 10 - a % 10
    if b % 10 != 0:
        b = b + 10 - b % 10
    if c % 10 != 0:
        c = c + 10 - c % 10
    if d % 10 != 0:
        d = d + 10 - d % 10
    if e % 10 != 0:
        e = e + 10 - e % 10
    print(a + b + c + d + e)
main()

=======
Suggestion 10

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #print(A, B, C, D, E)
    a = [A, B, C, D, E]
    #print(a)
    b = list(map(lambda x: x % 10, a))
    #print(b)
    c = list(map(lambda x: 10 if x == 0 else x, b))
    #print(c)
    d = list(map(lambda x, y: x - y, c, b))
    #print(d)
    e = list(map(lambda x, y: x + y, a, d))
    #print(e)
    print(max(e))

main()
