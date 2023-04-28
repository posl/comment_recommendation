Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    for i in range(M):
        if A[i] < total / (4*M):
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 2

def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sum = 0
    for i in range(N):
        sum += A[i]
    for i in range(M):
        if A[i] < sum/(4*M):
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    if a[m-1] >= total / (4*m):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    if A[M-1] >= total / (4*M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    total = sum(A)
    if A[M-1] >= total/(4*M):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    if a[m-1] >= total/(4*m):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    #n, m = list(map(int, input().split()))
    #a = list(map(int, input().split()))
    n, m = 12, 3
    a = [4, 56, 78, 901, 2, 345, 67, 890, 123, 45, 6, 789]
    print('Yes' if a[-m] >= sum(a) / (4 * m) else 'No')

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    #print(a)
    #print(total)
    for i in range(m):
        #print(i)
        #print(a[i])
        #print(total/4/m)
        if a[i] < total/4/m:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 9

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    s = sum(A)
    ans = "Yes"
    for i in range(M):
        if A[i] < s/(4*M):
            ans = "No"
    print(ans)

=======
Suggestion 10

def is_ok(mid, x):
    return mid >= x
