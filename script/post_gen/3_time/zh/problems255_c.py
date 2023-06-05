Synthesizing 10/10 solutions

=======
Suggestion 1

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
    if (x - a) % d != 0:
        return -1
    else:
        return (x - a) // d + 1

=======
Suggestion 2

def func(x, a, d, n):
    if d == 0:
        if a == x:
            return 0
        else:
            return 1
    if n == 1:
        if a == x:
            return 0
        else:
            return 1
    if n == 2:
        if a == x:
            return 0
        else:
            return 1
    if n == 3:
        if a == x:
            return 0
        else:
            return 1
    if n == 4:
        if a == x:
            return 0
        else:
            return 1
    if n == 5:
        if a == x:
            return 0
        else:
            return 1
    if n == 6:
        if a == x:
            return 0
        else:
            return 1
    if n == 7:
        if a == x:
            return 0
        else:
            return 1
    if n == 8:
        if a == x:
            return 0
        else:
            return 1
    if n == 9:
        if a == x:
            return 0
        else:
            return 1
    if n == 10:
        if a == x:
            return 0
        else:
            return 1
    if n == 11:
        if a == x:
            return 0
        else:
            return 1
    if n == 12:
        if a == x:
            return 0
        else:
            return 1
    if n == 13:
        if a == x:
            return 0
        else:
            return 1
    if n == 14:
        if a == x:
            return 0
        else:
            return 1
    if n == 15:
        if a == x:
            return 0
        else:
            return 1
    if n == 16:
        if a == x:
            return 0
        else:
            return 1
    if n == 17:
        if a == x:
            return 0
        else:
            return 1
    if n == 18:
        if a == x:
            return 0
        else:
            return

=======
Suggestion 3

def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        if (x - a) % d == 0 and (x - a) / d >= 0:
            print(int((x - a) / d))
        else:
            print(1 + int((x - a) / d))

=======
Suggestion 4

def solve(x,a,d,n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if d == 0:
        if x == a:
            return 0
        else:
            return 1
    if n % 2 == 0:
        return 2
    else:
        return 1

=======
Suggestion 5

def main():
    X,A,D,N = map(int, input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(1)
        return

    if X == A:
        print(0)
        return

    if D < 0:
        A, D = -A, -D
        X = -X

    if X < A:
        print((A-X)//D if (A-X)%D == 0 else (A-X)//D+1)
    else:
        print((X-A)//D+1 if (X-A)%D == 0 else (X-A)//D+2)

=======
Suggestion 6

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
            print(1 + min((a - x) // d + (a - x) % d != 0, (x - a) // d + (x - a) % d != 0))

=======
Suggestion 7

def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print(1)
    else:
        if (X-A)%D == 0:
            if (X-A)//D >= 0:
                print((X-A)//D)
            else:
                print(1)
        else:
            print(1)

=======
Suggestion 8

def main():
    x,a,d,n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
            return
        else:
            print(1)
            return
    if n == 1:
        if x == a:
            print(0)
            return
        else:
            print(1)
            return
    if d < 0:
        d = -d
        a = -a
    if x < a:
        if (a-x) % d == 0:
            print((a-x)//d)
            return
        else:
            print((a-x)//d+1)
            return
    if x > a:
        if (x-a) % d == 0:
            print((x-a)//d)
            return
        else:
            print((x-a)//d+1)
            return
    if x == a:
        print(0)
        return

=======
Suggestion 9

def solve(X,A,D,N):
    if N==1:
        return 0
    if D==0:
        if X==A:
            return 0
        else:
            return 1
    if N%2==0:
        if X%2==0:
            if (X-A)%D==0:
                return 0
            else:
                return 1
        else:
            return 1
    else:
        if X%2==0:
            return 1
        else:
            if (X-A)%D==0:
                return 0
            else:
                return 1

=======
Suggestion 10

def main():
    # 读入数据
    X, A, D, N = map(int, input().split())
    # 从A开始往后N个数，组成一个等差数列
    # 用等差数列的求和公式求出最大值
    max = A + (N - 1) * D
    # 用等差数列的求和公式求出最小值
    min = A
    # 如果X在这个区间内，就直接输出0
    if X >= min and X <= max:
        print(0)
        return
    # 如果X小于最小值，就用最小值减去X
    if X < min:
        print(min - X)
        return
    # 如果X大于最大值，就用X减去最大值
    if X > max:
        print(X - max)
        return

main()
