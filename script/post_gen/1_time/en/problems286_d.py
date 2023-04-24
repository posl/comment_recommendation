Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = "No"
    for i in range(N):
        if X == A[i] * B[i]:
            ans = "Yes"
            break
        elif X > A[i] * B[i]:
            X -= A[i] * B[i]
        else:
            ans = "No"
            break
    print(ans)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    total = 0
    for i in range(N):
        total += A[i] * B[i]
    if total >= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

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
Suggestion 4

def main():
    n,x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    sum = 0
    for i in range(n):
        sum += a[i]*b[i]
    if sum <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    ans = 0
    for i in range(n):
        ans = ans + a[i]*b[i]
    if ans <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        aa,bb = map(int,input().split())
        a.append(aa)
        b.append(bb)
    sum = 0
    for i in range(n):
        sum += a[i] * b[i]
    if sum <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    coin = []
    for i in range(N):
        A, B = map(int, input().split())
        coin.append([A, B])
    coin.sort(key=lambda x: x[0])
    count = 0
    for i in range(N):
        count += coin[i][0] * coin[i][1]
        if count > X:
            print('No')
            exit()
    if count >= X:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0])
    total = 0
    for i in range(N):
        total += AB[i][0] * AB[i][1]
        if total > X:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    coins = [list(map(int, input().split())) for i in range(n)]
    coins.sort(key=lambda x: x[0])

    for i in range(n):
        x -= coins[i][0] * coins[i][1]
        if x < 0:
            print("No")
            return

    print("Yes")

=======
Suggestion 10

def main():
    n,x = map(int, input().split())
    temp = []
    for i in range(n):
        temp.append(list(map(int, input().split())))
    sum = 0
    for i in range(n):
        sum += temp[i][0]*temp[i][1]
    if sum <= x:
        print("Yes")
    else:
        print("No")
