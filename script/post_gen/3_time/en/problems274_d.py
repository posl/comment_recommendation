Synthesizing 10/10 solutions

=======
Suggestion 1

def readinput():
    n,x,y=list(map(int,input().split()))
    a=list(map(int,input().split()))
    return n,x,y,a

=======
Suggestion 2

def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(0)
    a.insert(0, 0)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if abs(a[j] - a[i]) == abs(j - i):
                print('No')
                exit()
    print('Yes')

=======
Suggestion 3

def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(0)
    a.insert(0, 0)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 2):
            if a[i] + a[j] <= x and abs(i - j) == a[i] + a[j]:
                print('Yes')
                return
            elif a[i] + a[j] <= y and abs(i - j) == a[i] + a[j]:
                print('Yes')
                return
    print('No')
    return

=======
Suggestion 4

def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n):
        for j in range(i+1, n):
            if (a[i] - a[j])**2 + (i - j)**2 == (a[i] - a[j])**2:
                print("Yes")
                exit()

    print("No")

=======
Suggestion 5

def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(abs(x - y))
    for i in range(n):
        for j in range(i+1, n+1):
            if a[i] + a[j] == abs(x - y):
                print('Yes')
                return
    print('No')

main()

=======
Suggestion 6

def solve():
    N, x, y = map(int, input().split())
    A = [int(n) for n in input().split()]
    for i in range(N):
        for j in range(i+1, N):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    A = [0] + A
    A.append(0)
    for i in range(N+1):
        if A[i] + A[i+1] > A[-1]:
            print("No")
            return
    print("Yes")
    return

solve()

=======
Suggestion 7

def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(N):
        if i == N-1:
            break
        if A[i] + A[i+1] == abs(x-y):
            print('Yes')
            exit()
    print('No')

=======
Suggestion 8

def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    print('Yes' if is_possible(N, x, y, A) else 'No')

=======
Suggestion 9

def solve(n, x, y, a):
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(i-j) == abs(a[i]-a[j]):
                return 'Yes'
    return 'No'

n, x, y = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, x, y, a))

=======
Suggestion 10

def check90deg(x1,y1,x2,y2,x3,y3):
    if (x1 == x2 and x2 == x3) or (y1 == y2 and y2 == y3):
        return False
    if x1 == x2:
        if y1 == y3:
            return True
        else:
            return False
    if x2 == x3:
        if y1 == y2:
            return True
        else:
            return False
    if x1 == x3:
        if y1 == y2:
            return True
        else:
            return False
    if y1 == y2:
        if x1 == x3:
            return True
        else:
            return False
    if y2 == y3:
        if x1 == x2:
            return True
        else:
            return False
    if y1 == y3:
        if x1 == x2:
            return True
        else:
            return False
    if abs((y2-y1)/(x2-x1)) == abs((y3-y2)/(x3-x2)):
        return True
    else:
        return False
        
N,x,y = map(int,input().split())
A = list(map(int,input().split()))

for i in range(N-1):
    if check90deg(0,0,A[i],0,A[i+1],0) == False:
        print("No")
        exit()
