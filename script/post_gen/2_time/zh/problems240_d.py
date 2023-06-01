Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N,X = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    now = 0
    for i in range(N):
        if now + a[i] <= X and now + b[i] >= X:
            print('Yes')
            return
        now += b[i]
    print('No')

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    sum = 0
    for i in range(N):
        sum += a[i]
        if sum > X:
            print("No")
            return
        sum += b[i]
    if sum == X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N,X = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    sum = 0
    for i in range(N):
        sum += a[i]
        if sum > X:
            print("No")
            exit()
        sum += (b[i] - a[i])
    if sum > X:
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def solve():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    for i in range(n):
        if a[i] > x:
            print('No')
            return
        x += b[i] - a[i]
    print('Yes')

=======
Suggestion 5

def solve():
    # N X
    N, X = map(int, input().split())
    # a_1 b_1
    # .
    # .
    # .
    # a_N b_N
    a = []
    b = []
    for i in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    # print(N, X)
    # print(a)
    # print(b)

    # 求和
    sum = 0
    for i in range(N):
        sum += a[i]
        sum += b[i]

    # print(sum)

    # 判断
    if sum >= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def check(x):
    if x == 0:
        return True
    if x < 0:
        return False
    for i in range(N):
        if check(x - A[i]) or check(x - B[i]):
            return True
    return False

N, X = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    result = "No"
    for i in range(N):
        if a[i] <= X <= b[i]:
            result = "Yes"
            break
    print(result)

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    a_b = []
    for _ in range(n):
        a_b.append(list(map(int, input().split())))
    a_b.sort(key=lambda x: x[1])
    for i in range(n):
        if x < a_b[i][0]:
            print('No')
            return
        x += a_b[i][1] - a_b[i][0]
    print('Yes')

=======
Suggestion 9

def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    for j in range(n):
        if x == a[j] or x == b[j]:
            print("Yes")
            break
        else:
            print("No")
            break

=======
Suggestion 10

def solve():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = "No"
    for i in range(N):
        if A[i] <= X and X <= B[i]:
            ans = "Yes"
            break
    print(ans)
