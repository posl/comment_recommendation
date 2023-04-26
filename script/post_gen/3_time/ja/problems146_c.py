Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, X = map(int, input().split())
    N = 0
    for i in range(10, 0, -1):
        if A * i + B * len(str(i)) <= X:
            N = i
            break
    print(N)

=======
Suggestion 2

def main():
    a, b, x = map(int, input().split())

    def d(n):
        return len(str(n))

    def f(n):
        return a * n + b * d(n)

    left = 0
    right = 10 ** 9 + 1
    while right - left > 1:
        mid = (left + right) // 2
        if f(mid) <= x:
            left = mid
        else:
            right = mid

    print(left)

=======
Suggestion 3

def main():
    A, B, X = map(int, input().split())
    max = 0
    for i in range(1,10):
        if A * i + B * len(str(i)) <= X:
            max = i
    print(max)

=======
Suggestion 4

def main():
    a,b,x = map(int, input().split())
    ans = 0
    for i in range(1, 10):
        if a * i + b * len(str(i)) <= x:
            ans = max(ans, i)
    print(ans)

=======
Suggestion 5

def main():
    # 標準入力から A, B, X を取得する
    A, B, X = map(int, input().split())

    # X を買うことのできる最大の整数を出力する
    if A + B > X:
        print(0)
    elif A * 10 + B * 10 <= X:
        print(10 ** 9)
    else:
        #10 ** 9 以下の整数の中で、X を買うことのできる最大の整数を出力する
        #10 ** 9以下の整数の中で、X を買うことのできる最大の整数を出力する
        #10 ** 9以下の整数の中で、X を買うことのできる最大の整数を出力する
        #10 ** 9以下の整数の中で、X を買うことのできる最大の整数を出力する
        #10 ** 9以下の整数の中で、X を買うことのできる最大の整数を出力する
        #10 ** 9以下の整数の中で、X を買うことのできる最大の整数を出力する
        #10 ** 9以下の整数の中で、X を買うことのできる最大の整数を出力する
        #10 ** 9以下の整数の中で、X を買うことのできる最大の整数を出力する
        print((X - B) // A)

=======
Suggestion 6

def main():
    a, b, x = map(int, input().split())
    if a*10**9 + b*10 < x:
        print(10**9)
    else:
        if a*10**9 + b*1 > x:
            print(0)
        else:
            for i in range(2, 10**9):
                if a*i + b*len(str(i)) > x:
                    print(i-1)
                    break

=======
Suggestion 7

def main():
    a,b,x = map(int,input().split())
    if a * 10**9 + b * 10 > x:
        print(0)
    else:
        print(10**9)

=======
Suggestion 8

def main():
    a, b, x = map(int, input().split())
    #print("a,b,x:", a, b, x)
    #print("x / a:", x / a)
    #print("x / b:", x / b)
    if x / a > 10**9:
        print(10**9)
    elif x / b > 10**9:
        print(10**9)
    else:
        print(0)

=======
Suggestion 9

def main():
    a, b, x = map(int, input().split())
    print(int((x - b) / a)) if x >= a else print(0)

=======
Suggestion 10

def calc_price(a,b,n):
    return a*n + b*len(str(n))
