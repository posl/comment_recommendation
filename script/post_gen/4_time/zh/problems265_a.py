Synthesizing 10/10 solutions

=======
Suggestion 1

def problem265_a():
    x,y,n = map(int,input().split())
    if n%3 == 0:
        print(n//3*y)
    elif n%3 == 1:
        print((n//3)*y+x)
    else:
        print((n//3)*y+y)

=======
Suggestion 2

def problems265_a():
    x,y,n=map(int,input().split())
    if n%3==0:
        print((n//3)*y)
    elif n%3==1:
        print(((n//3)*y)+x)
    elif n%3==2:
        print(((n//3)*y)+y)

=======
Suggestion 3

def get_min_price(x, y, n):
    # 用25日元买三个苹果，买三次，用10日元买一个苹果，你将得到正好10个苹果，总价为85日元。
    # 你不可能以更低的价格获得正好10个苹果，所以答案是85日元。

    # 用10日元买一个苹果10次是最好的。
    # 用100日元买一个苹果两次。

    if n % 3 == 0:
        return min(x * n, y * (n // 3))
    elif n % 3 == 1:
        return min(x * n, y * (n // 3) + x)
    elif n % 3 == 2:
        return min(x * n, y * (n // 3) + y)

=======
Suggestion 4

def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(int(n / 3 * y))
    elif n % 3 == 1:
        print(int((n - 1) / 3 * y + x))
    else:
        print(int((n - 2) / 3 * y + 2 * x))

=======
Suggestion 5

def buy_apple(x,y,n):
    if x==y:
        return x*n
    if x>y:
        return y*n
    if x<y:
        if n%3==0:
            return n//3*y
        else:
            return (n//3+1)*y

=======
Suggestion 6

def main():
    x, y, n = map(int, input().split())
    print((n//3)*2*y + (n%3)*x if n%3 != 0 else (n//3)*2*y)

=======
Suggestion 7

def problem265_a(x, y, n):
    if x >= y:
        return n * x
    else:
        return (n // 3) * y + (n % 3) * x

=======
Suggestion 8

def buy_apple(x,y,n):
    if n%3==0:
        return min(x*n/3,y*n/3)
    elif n%3==1:
        return min(x*(n-1)/3+y,y*(n-1)/3+x)
    else:
        return min(x*(n-2)/3+2*y,y*(n-2)/3+2*x)

=======
Suggestion 9

def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print((n // 3) * y)
    elif n % 3 == 1:
        print(((n // 3) * y) + x)
    else:
        print(((n // 3) * y) + (2 * x))

=======
Suggestion 10

def main():
    x,y,n = map(int, input().split())
    if n%3 == 0:
        print(int(n/3*y))
    elif n%3 == 1:
        print(int((n-1)/3*y+x))
    else:
        print(int((n-2)/3*y+x*2))
