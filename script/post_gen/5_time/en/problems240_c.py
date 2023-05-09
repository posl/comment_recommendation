Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    count = 0
    for i in range(n):
        count += a[i]
        if count > x:
            print("No")
            exit()
        count += b[i]
    if count <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    sum = 0
    for i in range(N):
        if i % 2 == 0:
            sum += b[i]
        else:
            sum += a[i]
    if sum >= X:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    ans = "No"
    for i in range(n):
        if a[i] <= x and b[i] >= x:
            ans = "Yes"
    print(ans)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        c, d = map(int, input().split())
        a.append(c)
        b.append(d)
    s = 0
    for i in range(n):
        if i%2 == 0:
            s += b[i]
        else:
            s += a[i]
    if s >= x:
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
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    if sum(a) <= x and x <= sum(b):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    a = [0 for _ in range(n)]
    b = [0 for _ in range(n)]
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    if a[0] > x or b[0] < x:
        print("No")
        return
    for i in range(1, n):
        if a[i] > b[i-1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 7

def main():
    N,X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    print('Yes' if sum(a) <= X and X <= sum(b) else 'No')

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    jumps = [list(map(int, input().split())) for _ in range(N)]
    distance = 0
    for i in range(N):
        distance += jumps[i][0]
        if distance > X:
            print("No")
            return
        distance += jumps[i][1]
    if distance > X:
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(N)]

    distance = 0
    for i in range(N):
        distance += AB[i][0] * AB[i][1]
        if distance > X * 100:
            print("No")
            return

    print("Yes")

=======
Suggestion 10

def jump(n, x, ab):
    pos = 0
    for i in range(n):
        pos += ab[i][0]
        if pos > x:
            return False
        pos += ab[i][1]
    if pos > x:
        return False
    else:
        return True
