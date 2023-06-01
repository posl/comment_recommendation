Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # print(A)
    # print(B)
    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    if sum <= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N,X=map(int,input().split())
    A=[]
    B=[]
    for i in range(N):
        a,b=map(int,input().split())
        A.append(a)
        B.append(b)
    sum=0
    for i in range(N):
        sum=sum+A[i]*B[i]
    if sum>=X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def solve(n, x, ab):
    # n: number of coins
    # x: target
    # ab: list of (a, b)
    # return: True/False
    # print(n, x, ab)
    if n == 0:
        return False
    a, b = ab[0]
    if a * b == x:
        return True
    if a * b > x:
        return solve(n - 1, x, ab[1:])
    else:
        return solve(n - 1, x - a * b, ab[1:])

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    sum = 0

    for i in range(n):
        a, b = map(int, input().split())
        sum += a * b

    if sum <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def solve():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        ans += A[i] * B[i]
    if ans <= X:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def coin_pay(coin_list, pay):
    coin_list.sort(key=lambda x: x[0], reverse=True)
    pay_list = []
    for coin in coin_list:
        for i in range(coin[1]):
            pay_list.append(coin[0])
    pay_list.sort(reverse=True)
    pay_sum = 0
    for coin in pay_list:
        pay_sum += coin
        if pay_sum == pay:
            return True
    return False

=======
Suggestion 7

def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    sum = 0
    for i in range(n):
        sum += a[i]*b[i]
    if sum >= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def solve():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    #print(n,x,a,b)
    #print(sum([a[i]*b[i] for i in range(n)]))
    if sum([a[i]*b[i] for i in range(n)]) >= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def solve():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = "No"
    for i in range(2 ** n):
        sum = 0
        for j in range(n):
            if i >> j & 1 == 1:
                sum += a[j] * b[j]
        if sum == x:
            ans = "Yes"
            break
    print(ans)

solve()

=======
Suggestion 10

def pay(coin, price):
    if coin == 0:
        return False
    if coin == 1:
        return price == 0
    if coin == 2:
        return price % 2 == 0
    if coin == 5:
        return price % 5 == 0
    if coin == 10:
        return price % 10 == 0
    if coin == 50:
        return price % 50 == 0
    if coin == 100:
        return price % 100 == 0
    if coin == 500:
        return price % 500 == 0
    if coin == 1000:
        return price % 1000 == 0
    return False
