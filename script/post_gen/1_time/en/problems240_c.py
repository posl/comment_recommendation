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
    #print(a)
    #print(b)
    ans = "No"
    current = 0
    for i in range(n):
        current += a[i]
        if current > x:
            break
        current += b[i]
        if current == x:
            ans = "Yes"
            break
    print(ans)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    distance = 0
    for i in range(n):
        distance += a[i]
        if distance > x:
            print("No")
            exit()
        distance += b[i]

    if distance > x:
        print("No")
    else:
        print("Yes")

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

    #print(n, x)
    #print(a)
    #print(b)

    for i in range(n):
        x -= a[i]
        if x < 0:
            print("No")
            return
        x += b[i]
        #print(x)

    print("Yes")
    return

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
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
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(n):
        x -= a[i]
        if x < 0:
            print("No")
            return
        x += b[i]
    if x < 0:
        print("No")
    else:
        print("Yes")
    return

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    sum = 0
    for i in range(n):
        if i == 0:
            sum += a[i]
        else:
            sum += a[i] - b[i-1]
    sum += b[n-1]
    if sum <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    ans = 'No'
    for i in range(n):
        if a[i] <= x <= b[i]:
            ans = 'Yes'
    print(ans)

=======
Suggestion 8

def solve():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    total = 0
    for i in range(N):
        if i % 2 == 0:
            total += a[i]
        else:
            total += b[i]

    if total <= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    sum = 0
    for i in range(N):
        a, b = map(int, input().split())
        sum += a * b
        if sum > X * 100:
            print('Yes')
            return
    print('No')

=======
Suggestion 10

def main():
    n, x = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 'No'
    for i in range(n):
        x -= a[i][0]
        if x < 0:
            ans = 'No'
            break
        if x == 0:
            ans = 'Yes'
            break
        x += a[i][1]
    print(ans)
