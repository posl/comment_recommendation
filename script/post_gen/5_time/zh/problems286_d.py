Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a_,b_ = map(int,input().split())
        a.append(a_)
        b.append(b_)
    for i in range(1,n):
        a[0] = a[0]*b[i]+a[i]*b[0]
        b[0] = b[0]*b[i]
    if x%a[0] == 0:
        print("Yes")
    else:
        print("No")
main()

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(n):
        if x % a[i] == 0:
            if x // a[i] <= b[i]:
                print('Yes')
                exit()
        else:
            if x // a[i] < b[i]:
                print('Yes')
                exit()
    print('No')

=======
Suggestion 3

def calc_num_of_coins(coins, x):
    num_of_coins = 0
    for i in range(len(coins)):
        num_of_coins += coins[i][1]
        if num_of_coins >= x:
            return i + 1
    return len(coins)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    if sum <= X:
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

    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    if sum >= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N,X = map(int,input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    #print(A)
    #print(B)
    sum = 0
    for i in range(N):
        sum += A[i]*B[i]
    if sum < X:
        print("No")
    else:
        print("Yes")

=======
Suggestion 7

def pay(x, a, b):
    if x == 0:
        return True
    elif x > 0 and a == 0:
        return False
    else:
        return pay(x - a, a, b - 1) or pay(x, a - 1, b)

=======
Suggestion 8

def main():
    n,x = map(int,input().split())
    coin = []
    for i in range(n):
        coin.append(list(map(int,input().split())))
    if x == 0:
        print('Yes')
    else:
        for i in range(n):
            if coin[i][1] >= x:
                print('Yes')
                break
            else:
                x -= coin[i][1]
                if x == 0:
                    print('Yes')
                    break
                elif i == n-1:
                    print('No')
                    break

=======
Suggestion 9

def solve():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(N):
        X -= A[i] * B[i]
    if X >= 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    A_list = []
    B_list = []
    for i in range(N):
        A, B = map(int, input().split())
        A_list.append(A)
        B_list.append(B)
    sum = 0
    for i in range(N):
        sum += A_list[i] * B_list[i]
    if sum <= X:
        print("Yes")
    else:
        print("No")
