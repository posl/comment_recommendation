Synthesizing 10/10 solutions

=======
Suggestion 1

def problem158_b():
    pass

=======
Suggestion 2

def main():
    n, a, b = map(int, input().split())
    print(min(a*n//(a+b), n))

=======
Suggestion 3

def main():
    n,a,b = map(int,input().split())
    if a+b == 0:
        print(0)
        return
    else:
        if n%(a+b) > a:
            print(a*(n//(a+b))+a)
        else:
            print(a*(n//(a+b))+n%(a+b))

=======
Suggestion 4

def blue_ball(n, a, b):
    if n == 0:
        return 0
    elif n == 1:
        return a
    elif n == 2:
        return a + b
    else:
        return blue_ball(n-1, a, b) + blue_ball(n-2, a, b)

n, a, b = map(int, input().split())
print(blue_ball(n, a, b))

=======
Suggestion 5

def solve(n, a, b):
    if n<=a:
        return n
    else:
        return a + (n-a)%b

n, a, b = map(int, input().split())
print(solve(n, a, b))

=======
Suggestion 6

def main():
    n,a,b = map(int,input().split())
    # print(n,a,b)
    if n==1:
        if a==0 and b==0:
            print(0)
        elif a==0 and b==1:
            print(1)
        elif a==1 and b==0:
            print(0)
        else:
            print(1)
    elif a==0 and b==0:
        print(0)
    elif a==0 and b==1:
        print(1)
    elif a==1 and b==0:
        print(0)
    elif a==1 and b==1:
        print(1)
    else:
        if n==2:
            print(1)
        elif n==3:
            print(2)
        elif n==4:
            print(2)
        elif n==5:
            print(3)
        elif n==6:
            print(3)
        elif n==7:
            print(4)
        elif n==8:
            print(4)
        elif n==9:
            print(5)
        elif n==10:
            print(5)
        elif n==11:
            print(6)
        elif n==12:
            print(6)
        elif n==13:
            print(7)
        elif n==14:
            print(7)
        elif n==15:
            print(8)
        elif n==16:
            print(8)
        elif n==17:
            print(9)
        elif n==18:
            print(9)
        elif n==19:
            print(10)
        elif n==20:
            print(10)
        elif n==21:
            print(11)
        elif n==22:
            print(11)
        elif n==23:
            print(12)
        elif n==24:
            print(12)
        elif n==25:
            print(13)
        elif n==26:
            print(13)
        elif n==27:
            print(14)
        elif n==28:
            print(14)
        elif n==29:
            print(15)
        elif n==30:
            print(15)
        elif n==31:
            print(16)
        elif n==32:
            print(16)
        elif n==33:
            print(17)
        elif n==34:

=======
Suggestion 7

def main():
    # 读取标准输入
    n, a, b = map(int, input().split())

    #计算蓝球数量
    blue = (n // (a + b)) * a
    blue += min(a, n % (a + b))

    #打印输出
    print(blue)

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    print(N // (A + B) * A + min(N % (A + B), A))

=======
Suggestion 9

def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif N <= A:
        print(1)
    elif A < N <= A + B:
        print(2)
    else:
        a = (N - A) // (A + B)
        b = (N - A) % (A + B)
        print(A + a * A + b)

=======
Suggestion 10

def main():
    n,a,b = map(int,input().split())
    if a == 0:
        print(0)
        return
    if a+b >= n:
        print(a)
    else:
        print(a*(n//(a+b))+min(a,n%(a+b)))
