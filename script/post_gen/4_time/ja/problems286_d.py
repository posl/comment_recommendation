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
    #print(A)
    #print(B)
    total = 0
    for i in range(N):
        total += A[i] * B[i]
    #print(total)
    if total <= X:
        print("Yes")
    else:
        print("No")

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
    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    if sum <= X:
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

    if sum >= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 0
    for i in range(n):
        ans += a[i] * b[i]
    if ans <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 'No'
    for i in range(n):
        if x == a[i] * b[i]:
            ans = 'Yes'
            break
        for j in range(n):
            if x == a[i] * b[i] + a[j] * b[j]:
                ans = 'Yes'
                break
    print(ans)

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        aa, bb = map(int, input().split())
        a.append(aa)
        b.append(bb)

    total = 0
    for i in range(n):
        total += a[i] * b[i]

    if total <= x:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    # print(n, x)
    # print(a)
    # print(b)
    # print(sum([a[i] * b[i] for i in range(n)]))
    if sum([a[i] * b[i] for i in range(n)]) >= x:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    N,X = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        ans += A[i]*B[i]
    if ans <= X:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def pay(N, X, A, B):
    for i in range(N):
        X -= A[i] * B[i]
    if X >= 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def check_payment(n, x, a, b):
    if n == 1:
        if x % a[0] == 0 and x / a[0] <= b[0]:
            return True
        else:
            return False
    else:
        for i in range(b[0]+1):
            if x - a[0] * i < 0:
                break
            elif x - a[0] * i == 0:
                return True
            else:
                if check_payment(n-1, x - a[0] * i, a[1:], b[1:]):
                    return True
        return False

n, x = map(int, input().split())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
