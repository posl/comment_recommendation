Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, n = map(int, input().split())
    print(min(x * n, y * (n // 3) + x * (n % 3)))

=======
Suggestion 2

def main():
    X, Y, N = map(int, input().split())
    ans = N * X
    for i in range(0, N + 1):
        for j in range(0, N - i + 1):
            if i + j == N:
                ans = min(ans, i * Y + j * X)
    print(ans)

=======
Suggestion 3

def main():
    x,y,n = map(int,input().split())
    m = n % 3
    if m == 0:
        print(n//3*y)
    elif m == 1:
        print(n//3*y+x)
    else:
        print(n//3*y+x+x)
main()

I am trying to make a program that will take a list of numbers and print out the numbers that are less than 5. I am new to python and am having trouble with the syntax. Any help would be appreciated.

=======
Suggestion 4

def main():
    x,y,n = map(int,input().split())
    if n%2==0:
        if x<y:
            print(x*(n//2))
        else:
            print(y*(n//2))
    else:
        if x<y:
            print(x*(n//2)+x)
        else:
            print(y*(n//2)+x)

=======
Suggestion 5

def main():
    X, Y, N = [int(x) for x in input().split()]
    result = 0
    for i in range(0, N+1):
        if (i % 3 == 0):
            result += X
        else:
            result += Y
    print(result)

=======
Suggestion 6

def main():
    X, Y, N = map(int, input().split())
    min_cost = 100 * N
    for i in range(N+1):
        for j in range(N+1):
            if i + j <= N:
                cost = X * i + Y * j
                if cost < min_cost:
                    min_cost = cost
    print(min_cost)

=======
Suggestion 7

def main():
    X,Y,N = map(int,input().split())
    if X*3 < Y:
        print(X*N)
    else:
        print(Y*(N//3)+min(X*(N%3),Y))
main()

=======
Suggestion 8

def main():
    x, y, n = map(int, input().split())
    ans = 0
    for i in range(0, n+1):
        ans = min(ans, n*i*x + (n-i)//3*y)
    print(ans)

=======
Suggestion 9

def main():
    X, Y, N = map(int, input().split())
    #print(X,Y,N)
    min_cost = N*X
    #print(min_cost)
    for i in range(0, N+1):
        #print(i)
        cost = i*X + (N-i)*Y//3
        #print(cost)
        if cost < min_cost:
            min_cost = cost
    print(min_cost)

=======
Suggestion 10

def main():
    #input
    x,y,n = map(int,input().split())
    #calculations
    ans = 0
    if x * n < y:
        ans = x * n
    else:
        ans = y * (n // 3)
        if x * (n % 3) < y:
            ans += x * (n % 3)
        else:
            ans += y
    #output
    print(ans)
