Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(1, 1001):
        for j in range(N):
            if A[j] <= i <= B[j]:
                if j == N-1:
                    ans += 1
            else:
                break
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    print(solve(n, a_list, b_list))

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    ans = 0
    for i in range(1,1001):
        if all(A[j]<=i and i<=B[j] for j in range(N)):
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for x in range(1, 1001):
        flag = True
        for i in range(n):
            if not a[i] <= x <= b[i]:
                flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    min = max(a)
    max = min(b)
    if min > max:
        print(0)
    else:
        print(max - min + 1)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a_max = max(a)
    b_min = min(b)
    
    if a_max > b_min:
        print(0)
    else:
        print(b_min - a_max + 1)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    min = 0
    max = 1000
    for i in range(n):
        if min < a[i]:
            min = a[i]
        if max > b[i]:
            max = b[i]
    
    if max < min:
        print(0)
    else:
        print(max - min + 1)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for x in range(1, 1001):
        for i in range(n):
            if not (a[i] <= x <= b[i]):
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    #print(n, a, b)
    ans = 0
    for x in range(1, 1001):
        flag = True
        for i in range(n):
            if not (a[i] <= x <= b[i]):
                flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    min = max(A)
    max = min(B)
    
    if max - min + 1 < 0:
        print(0)
    else:
        print(max - min + 1)
