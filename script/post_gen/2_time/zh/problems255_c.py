Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x,a,d,n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        if (x-a)%d == 0:
            if (x-a)//d >= 0:
                print((x-a)//d)
            else:
                print((x-a)//d+2)
        else:
            print(-1)

=======
Suggestion 2

def get_input():
    x,a,d,n = map(int,input().split())
    return x,a,d,n

=======
Suggestion 3

def solve(x, a, d, n):
    if d == 0:
        if x == a:
            return 0
        else:
            return -1
    if n == 1:
        if x == a:
            return 0
        else:
            return -1
    if d > 0:
        if x < a:
            return -1
        if x > a + (n - 1) * d:
            return -1
        if x == a:
            return 0
        if (x - a) % d == 0:
            return (x - a) // d
        else:
            return -1
    if d < 0:
        if x > a:
            return -1
        if x < a + (n - 1) * d:
            return -1
        if x == a:
            return 0
        if (x - a) % d == 0:
            return (x - a) // d
        else:
            return -1

=======
Suggestion 4

def solve(x,a,d,n):
    if d==0:
        if x==a:
            return 0
        else:
            return -1
    if n==1:
        if x==a:
            return 0
        else:
            return -1
    if (x-a)%d!=0:
        return -1
    else:
        return (x-a)//d

x,a,d,n=map(int,input().split())
print(solve(x,a,d,n))

=======
Suggestion 5

def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        if (x - a) % d == 0 and (x - a) // d >= 0:
            print((x - a) // d)
        else:
            print(-1)

=======
Suggestion 6

def main():
    # 读入数据
    x,a,d,n = map(int,input().split())
    # 判断d是否为0
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
        return
    # 判断是否为好数
    if (x-a)%d == 0:
        print(0)
        return
    # 判断是否为0
    if x == 0:
        print(1)
        return
    # 判断是否为正数
    if x > 0:
        # 判断是否为正数
        if d > 0:
            # 判断是否为奇数
            if n%2 == 0:
                if x < a:
                    print(a-x)
                else:
                    print(x-a)
            else:
                if x < a:
                    print(min(a-x,x-a+d))
                else:
                    print(min(x-a,x-a+d))
        else:
            # 判断是否为奇数
            if n%2 == 0:
                if x < a:
                    print(a-x)
                else:
                    print(x-a)
            else:
                if x < a:
                    print(min(a-x,x-a+d))
                else:
                    print(min(x-a,x-a+d))
    else:
        # 判断是否为正数
        if d > 0:
            # 判断是否为奇数
            if n%2 == 0:
                if x < a:
                    print(a-x)
                else:
                    print(x-a)
            else:
                if x < a:
                    print(min(a-x,x-a+d))
                else:
                    print(min(x-a,x-a+d))
        else:
            # 判断是否为奇数
            if n%2 == 0:
                if x < a:
                    print(a-x)
                else:
                    print(x-a)
            else:
                if x < a:
                    print(min(a-x,x-a+d))
                else:
                    print(min(x-a,x-a+d))

=======
Suggestion 7

def main():
    # 读取输入
    x, a, d, n = map(int, input().split())

    # 从x中减去a，得到x的偏移量
    x -= a

    # 如果x是d的倍数
    if x % d == 0:
        # 计算x的偏移量与d的商
        x //= d
        # 如果x是正数且n大于等于x
        if x >= 0 and n >= x:
            # 输出n-x
            print(n - x)
            # 退出程序
            exit()
        # 如果x是负数且n小于等于x
        elif x < 0 and n <= x:
            # 输出n-x
            print(n - x)
            # 退出程序
            exit()

    # 否则，输出n
    print(n)

=======
Suggestion 8

def main():
    X, A, D, N = map(int, input().split())
    print(X, A, D, N)
    return

=======
Suggestion 9

def main():
    X, A, D, N = map(int, input().split())
    #print(X, A, D, N)
    if D == 0:
        if X != A:
            print("NO")
            return
        else:
            print("YES")
            return
    if N == 1:
        if X == A:
            print("YES")
            return
        else:
            print("NO")
            return
    if (X - A) % D != 0:
        print("NO")
        return
    else:
        if (X - A) // D + 1 <= N:
            print("YES")
            return
        else:
            print("NO")
            return
