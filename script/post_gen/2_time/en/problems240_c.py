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
    print('Yes' if sum(A) <= X and X <= sum(B) else 'No')

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    print("Yes" if sum(b) >= x - (n - 1) else "No")

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = "No"
    s = 0
    for i in range(n):
        s += a[i]
        if s <= x and x <= s + b[i]:
            ans = "Yes"
            break
    print(ans)

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
        if i%2 == 0:
            sum += b[i]
        else:
            sum += a[i]
    if sum >= X:
        print('Yes')
    else:
        print('No')

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
    sum = 0
    for i in range(N):
        if X < a[i]:
            sum += a[i]
        else:
            sum += b[i]
    if sum <= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    a, b = [], []
    for i in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 'No'
    for i in range(N):
        if X >= a[i] and X <= b[i]:
            ans = 'Yes'
    print(ans)

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        tmp1, tmp2 = map(int, input().split())
        a.append(tmp1)
        b.append(tmp2)
    s = 0
    for i in range(n):
        if i % 2 == 0:
            s += a[i]
        else:
            s += b[i]
    if s <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(0,n):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    print(a)
    print(b)
    for i in range(0,n):
        if x >= a[i] and x <= b[i]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 9

def solve():
    # Implement solution here
    N, X = map(int, input().split())
    a = []
    b = []
    for _ in range(N):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    current = 0
    for i in range(N):
        current += a[i]
        if current > X:
            print('No')
            return
        if current == X:
            print('Yes')
            return
        current += b[i]
    if current == X:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    n, x = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort(key=lambda x: x[1])
    for i in range(n):
        if a[i][0] <= x <= a[i][1]:
            print("Yes")
            return
    print("No")
