Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for x in range(1, 1001):
        for i in range(n):
            if a[i] > x or b[i] < x:
                break
        else:
            ans += 1

    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    count = 0
    for i in range(1, 1001):
        flag = True
        for j in range(n):
            if i < a[j] or i > b[j]:
                flag = False
                break
        if flag:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count = 0
    for x in range(1, 1001):
        flag = True
        for i in range(n):
            if x < a[i] or b[i] < x:
                flag = False
                break
        if flag:
            count += 1

    print(count)

=======
Suggestion 4

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(1, 1001):
        for j in range(n):
            if i < a[j] or i > b[j]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count = 0
    for i in range(1, 1001):
        for j in range(n):
            if i < a[j] or i > b[j]:
                break
        else:
            count += 1

    print(count)
main()

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ans = 0
    for i in range(n):
        ans += max(0, min(b) - max(a) + 1)
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0

    for i in range(1, 1001):
        flag = True
        for j in range(n):
            if i < a[j] or i > b[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    mi = max(a)
    ma = min(b)

    print(max(0, ma - mi + 1))

=======
Suggestion 9

def main():
    num = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(1, 1001):
        for j in range(num):
            if i < a[j] or i > b[j]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    min = 0
    max = 100000
    for i in range(N):
        if A[i] > min:
            min = A[i]
        if B[i] < max:
            max = B[i]

    if max < min:
        print(0)
    else:
        print(max - min + 1)
