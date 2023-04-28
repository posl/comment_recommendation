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

    sum = 0
    for i in range(N):
        if i % 2 == 0:
            sum += A[i]
        else:
            sum += B[i]

    if sum >= X:
        print("Yes")
    else:
        print("No")

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

    current = 0
    for i in range(n):
        current += a[i]
        if current > x:
            print("No")
            return
        current += b[i]
    if current > x:
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
    sum = 0
    for i in range(n):
        if (i+1) % 2 == 0:
            sum += a[i]
        else:
            sum += b[i]
    if sum <= x:
        print('Yes')
    else:
        print('No')
    return

=======
Suggestion 4

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
        if (i % 2 == 0):
            sum += a[i]
        else:
            sum += b[i]
    if (sum >= X):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(N):
        X -= a[i]
        if X < 0:
            print("No")
            return
        X += b[i]
    if X < 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 6

def solve():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    count = 0
    for i in range(N):
        if X >= a[i] and X <= b[i]:
            count += 1
    if count > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N,X = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        a_,b_ = map(int,input().split())
        a.append(a_)
        b.append(b_)
    distance = 0
    for i in range(N):
        distance += a[i]
        if distance > X:
            print('No')
            return
        distance += b[i]
    if distance > X:
        print('No')
        return
    print('Yes')
    return

=======
Suggestion 8

def solve():
    N,X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    pos = 0
    for i in range(N):
        pos += a[i]
        if pos > X:
            print("No")
            return
        pos += b[i]
    if pos > X:
        print("No")
        return
    print("Yes")

=======
Suggestion 9

def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        temp_a,temp_b = map(int,input().split())
        a.append(temp_a)
        b.append(temp_b)
    #print(n,x)
    #print(a)
    #print(b)
    current_position = 0
    for i in range(n):
        current_position = current_position + a[i]
        if current_position > x:
            print("No")
            return
        current_position = current_position + (b[i] - a[i])
        if current_position > x:
            print("No")
            return
    if current_position == x:
        print("Yes")
    else:
        print("No")
    return

=======
Suggestion 10

def solve(n, x, a, b):
    for i in range(n):
        x -= a[i]
        if x < 0:
            return False
        x += b[i]
    return True
