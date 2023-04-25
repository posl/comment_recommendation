Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 10 ** 100
    sum = 0
    for i in range(len(B)):
        sum += B[i]
        if sum > X:
            print(i + 1)
            break

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 100
    total = 0
    for i in range(len(B)):
        total += B[i]
        if total > X:
            print(i+1)
            break

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    x = int(input())
    b = a * 10**100
    s = 0
    for i in range(len(b)):
        s += b[i]
        if s > x:
            print(i+1)
            break

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    s = sum(a)
    m = x // s
    ans = n * m
    x -= s * m
    for i in range(n):
        x -= a[i]
        ans += 1
        if x < 0:
            print(ans)
            exit()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())

    #print(N)
    #print(A)
    #print(X)

    #B = []
    #for i in range(10 ** 100):
    #    B.extend(A)
    B = A * (10 ** 100)

    #print(B)

    total = 0
    for i in range(len(B)):
        total += B[i]
        if total > X:
            print(i + 1)
            break

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    X = int(input())

    sumA = sum(A)
    sumB = sumA * (X // sumA)
    i = N * (X // sumA)
    while sumB <= X:
        sumB += A[i % N]
        i += 1
    print(i)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    #print(N, A, X)
    B = A*(10**100)
    #print(B)
    sum = 0
    for i in range(len(B)):
        sum += B[i]
        if sum > X:
            print(i+1)
            break

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    X = int(input())

    B = A*100
    sum = 0
    for i in range(0,len(B)):
        sum += B[i]
        if sum > X:
            print(i+1)
            break

=======
Suggestion 9

def main():
    num = int(input())
    list = [int(i) for i in input().split()]
    x = int(input())
    sum = 0
    count = 0
    while True:
        for i in range(num):
            sum += list[i]
            count += 1
            if sum > x:
                print(count)
                return

=======
Suggestion 10

def solve():
    pass
