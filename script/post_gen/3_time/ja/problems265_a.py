Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, n = map(int, input().split())
    ans = 10**9
    for i in range(0, n+1):
        for j in range(0, n+1):
            if i*3 + j > n:
                break
            if i*3 + j == n:
                ans = min(ans, i*x + j*y)
    print(ans)

=======
Suggestion 2

def main():
    x,y,n = map(int,input().split())
    ans = 0
    if n%3 == 0:
        ans = (n//3)*y
    elif n%3 == 1:
        ans = ((n//3)*y)+x
    elif n%3 == 2:
        ans = ((n//3)*y)+y-x
    print(ans)

=======
Suggestion 3

def problem265_a():
    x, y, n = map(int, input().split())
    ans = 0
    if n % 3 == 0:
        ans = (n//3) * y
    elif n % 3 == 1:
        ans = (n//3) * y + x
    else:
        ans = (n//3) * y + x * 2
    print(ans)

=======
Suggestion 4

def main():
    x,y,n = map(int, input().split())
    result = n * x
    for i in range(n + 1):
        result = min(result, i * y + (n - i) * x)
    print(result)

=======
Suggestion 5

def main():
    X,Y,N = map(int,input().split())
    ans = 0
    if N >= 3:
        ans += (N//3)*Y
        N = N%3
    if N >= 1:
        ans += X
    print(ans)

=======
Suggestion 6

def main():
    x, y, n = map(int, input().split())

    # 1個ずつ買う場合
    min_price = x * n

    # 3個ずつ買う場合
    for i in range(n + 1):
        price = x * i + y * (n - i)
        if price < min_price:
            min_price = price

    print(min_price)

=======
Suggestion 7

def calc(N, X, Y):
    if N <= 3:
        return X*N
    else:
        return calc(N-3, X, Y) + Y

=======
Suggestion 8

def main():
    x,y,n = map(int,input().split())
    if x*3 > y:
        print(int(y*(n/3)))
    else:
        print(int(x*n))

=======
Suggestion 9

def main():
    X,Y,N = map(int,input().split())

    # 3個買う方がお得かどうか
    if X*3 < Y:
        print(N*X)
    else:
        # 3個買う方がお得なので、3個単位でまとめて買う
        # 3個単位で買うためには、Nを3で割ったあまりが0か1か2かで場合分け
        if N%3 == 0:
            print((N//3)*Y)
        elif N%3 == 1:
            print((N//3)*Y+X)
        else:
            print((N//3)*Y+X*2)

=======
Suggestion 10

def get_input():
    return [int(x) for x in input().split()]
