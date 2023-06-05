Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    A, B, C, D = map(int, input().split())
    if A < B:
        print(-1)
        return
    if D == 1:
        print(0)
        return
    # D > 1
    if B >= C * D:
        print(-1)
        return
    # B < C * D
    t1 = (A - B) // (C * D - B)
    t2 = t1 + 1
    if t1 * C * D + B >= A:
        print(t1)
    else:
        print(t2)

=======
Suggestion 2

def solve():
    a,b,c,d = map(int, input().split())
    if a < b:
        print(-1)
    else:
        if d == 1:
            print(0)
        else:
            x = (a * d - a) // (b * d - c)
            if (a * d - a) % (b * d - c) != 0:
                x += 1
            print(x)

=======
Suggestion 3

def main():
    a,b,c,d = map(int,input().split())
    if (a<b):
        print(-1)
    else:
        if (c*d-b<=0):
            print(-1)
        else:
            print((a+b-1)//(c*d-b))

=======
Suggestion 4

def main():
    a,b,c,d = map(int,input().split())
    if a < b:
        print(-1)
        return
    if b > c*d:
        print(-1)
        return
    if a <= c*d:
        print(1)
        return
    i = 1
    while a > c*d:
        a += b
        a -= c*d
        i += 1
    print(i)

=======
Suggestion 5

def main():
    a,b,c,d = [int(x) for x in input().split()]
    if a > b * c:
        print(-1)
    else:
        print((a + b - 1) // b)

=======
Suggestion 6

def main():
    #读入数据
    a,b,c,d=map(int,input().split())
    #判断是否有解
    if b>=a:
        print(-1)
        return
    #二分查找
    left=0
    right=10**18
    while right-left>1:
        mid=(left+right)//2
        if mid*d>=a:
            right=mid
        else:
            left=mid
    print(b*(right-1)+c*(right-1))

=======
Suggestion 7

def main():
    a,b,c,d = map(int, input().split())
    if a < b:
        print(-1)
    else:
        if c*d <= b:
            print(-1)
        else:
            print((a + b - 1) // b - 1)

=======
Suggestion 8

def main():
    a,b,c,d = map(int,input().split())
    if a > c*d:
        print(-1)
        return
    else:
        if a <= b:
            print(1)
            return
        else:
            print((a-b-1)//(b-c)+2)
            return

=======
Suggestion 9

def main():
    A,B,C,D = map(int,input().split())
    count = 0
    if A <= B:
        print(-1)
    else:
        while A > B*D:
            A += B
            A -= C
            count += 1
        print(count)

=======
Suggestion 10

def main():
    a,b,c,d = map(int,input().split())
    if a <= b * c:
        print(-1)
    else:
        print((a+d*b-1)//(d*b-c))
