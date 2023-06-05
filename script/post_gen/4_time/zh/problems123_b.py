Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读入数据
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    # 计算最后一道菜的最早送达时间
    print((a+9)//10*10 + (b+9)//10*10 + (c+9)//10*10 + (d+9)//10*10 + (e+9)//10*10)

=======
Suggestion 2

def solve(A,B,C,D,E):
    return ((A+9)//10)*10 + ((B+9)//10)*10 + ((C+9)//10)*10 + ((D+9)//10)*10 + ((E+9)//10)*10

=======
Suggestion 3

def problems123_b():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    if a%10==0:
        a=a
    else:
        a=a+(10-a%10)
    if b%10==0:
        b=b
    else:
        b=b+(10-b%10)
    if c%10==0:
        c=c
    else:
        c=c+(10-c%10)
    if d%10==0:
        d=d
    else:
        d=d+(10-d%10)
    if e%10==0:
        e=e
    else:
        e=e+(10-e%10)
    if a>=b and a>=c and a>=d and a>=e:
        print(a)
    elif b>=a and b>=c and b>=d and b>=e:
        print(b)
    elif c>=a and c>=b and c>=d and c>=e:
        print(c)
    elif d>=a and d>=b and d>=c and d>=e:
        print(d)
    else:
        print(e)
problems123_b()

=======
Suggestion 4

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    if A % 10 == 0:
        a = A
    else:
        a = (A // 10 + 1) * 10
    if B % 10 == 0:
        b = B
    else:
        b = (B // 10 + 1) * 10
    if C % 10 == 0:
        c = C
    else:
        c = (C // 10 + 1) * 10
    if D % 10 == 0:
        d = D
    else:
        d = (D // 10 + 1) * 10
    if E % 10 == 0:
        e = E
    else:
        e = (E // 10 + 1) * 10

    print(a+b+c+d+e)

main()

=======
Suggestion 5

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    a = (a+9)//10*10
    b = (b+9)//10*10
    c = (c+9)//10*10
    d = (d+9)//10*10
    e = (e+9)//10*10
    print(a+b+c+d+e)

=======
Suggestion 6

def main():
    # 读入数据
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    # 计算最后一道菜的最早送达时间
    # 1. 计算所有菜品的最早送达时间
    # 2. 取最大值
    # 3. 按10的倍数取上限
    print(max([((A+9)//10)*10,((B+9)//10)*10,((C+9)//10)*10,((D+9)//10)*10,((E+9)//10)*10]))

=======
Suggestion 7

def get_time():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    time = [A,B,C,D,E]
    min_time = min(time)
    if min_time%10 == 0:
        return min_time
    else:
        return (10 - min_time%10 + min_time)

=======
Suggestion 8

def solve():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    t = 0
    if A % 10 != 0:
        t += (A // 10 + 1) * 10
    else:
        t += A
    if B % 10 != 0:
        t += (B // 10 + 1) * 10
    else:
        t += B
    if C % 10 != 0:
        t += (C // 10 + 1) * 10
    else:
        t += C
    if D % 10 != 0:
        t += (D // 10 + 1) * 10
    else:
        t += D
    if E % 10 != 0:
        t += (E // 10 + 1) * 10
    else:
        t += E
    print(t)

=======
Suggestion 9

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    time = 0
    time += (A-1)//10*10 + A
    time += (B-1)//10*10 + B
    time += (C-1)//10*10 + C
    time += (D-1)//10*10 + D
    time += (E-1)//10*10 + E
    print(time)

=======
Suggestion 10

def main():
    # 读入数据
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    # 计算最后一道菜的最早送达时间
    # 从所有菜品中选出最多时间的菜品
    max_time = max(A, B, C, D, E)

    # 计算最后一道菜的最早送达时间
    # 从所有菜品中选出最少时间的菜品
    min_time = min(A, B, C, D, E)

    # 计算最后一道菜的最早送达时间
    # 从所有菜品中选出最多时间的菜品
    max_time = max(A, B, C, D, E)

    # 计算最后一道菜的最早送达时间
    # 从所有菜品中选出最少时间的菜品
    min_time = min(A, B, C, D, E)

    # 计算最后一道菜的最早送达时间
    # 从所有菜品中选出最多时间的菜品
    max_time = max(A, B, C, D, E)

    # 计算最后一道菜的最早送达时间
    # 从所有菜品中选出最少时间的菜品
    min_time = min(A, B, C, D, E)

    # 计算最后一道菜的最早送达时间
    # 从所有菜品中选出最多时间的菜品
    max_time = max(A, B, C, D, E)

    # 计算最后一道菜的最早送达时间
    # 从所有菜品中选出最少时间的菜品
    min_time = min(A, B, C, D, E)

    # 计算最后一道菜的最早送达时间
    # 从所有菜品中选出最多时间的菜品
