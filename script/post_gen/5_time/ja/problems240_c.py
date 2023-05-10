Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    c = 0
    for i in range(n):
        if a[i] <= x:
            c += 1
            x -= a[i]
        else:
            break
    for i in range(n-c):
        x -= b[i+c]
    if x == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def solve():
    N,X = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    ans = 0
    for i in range(N):
        ans += a[i] * b[i]
    if ans >= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    # print(a)
    # print(b)

    sum = 0
    for i in range(N):
        if a[i] <= X and b[i] >= X:
            sum = sum + 1

    if sum == 0:
        print('No')
    else:
        print('Yes')

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    ans = "No"
    pos = 0
    for i in range(N):
        a, b = map(int, input().split())
        pos += a
        if pos >= X:
            ans = "Yes"
            break
        pos += b
        if pos >= X:
            ans = "Yes"
            break
    print(ans)

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    pos = 0
    for i in range(n):
        if a[i] <= x:
            pos += 1
        else:
            pos -= 1

    if pos >= 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    pos = 0
    for i in range(N):
        pos += a[i]
        if pos > X:
            print("No")
            return
        pos += b[i]
    if pos == X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    # print(n,x,a,b)

    pos = 0
    for i in range(n):
        pos += a[i]
        if pos == x:
            print('Yes')
            return
        pos += b[i]
        if pos == x:
            print('Yes')
            return
    print('No')

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    pos = 0
    for i in range(n):
        if i % 2 == 0:
            pos += a[i]
        else:
            pos += b[i]
    if pos == x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def check(N,X,ab):
    pos = 0
    for i in range(N):
        pos += ab[i][1]
        if pos > X:
            return False
        pos -= ab[i][0]
        if pos < 0:
            return False
    return True

N,X = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(N)]
print('Yes' if check(N,X,ab) else 'No')

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    result = "No"
    for i in range(N):
        a, b = map(int, input().split())
        if a <= X and X <= b:
            result = "Yes"
            break
    print(result)
