Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    min_num = max(a)
    max_num = min(b)

    print(max_num - min_num + 1 if max_num >= min_num else 0)

=======
Suggestion 2

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    for i in range(1, 1001):
        flag = True
        for j in range(n):
            if i < a[j] or i > b[j]:
                flag = False
        if flag:
            count += 1
    print(count)

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for x in range(1, 1001):
        for i in range(N):
            if A[i] <= x <= B[i]:
                pass
            else:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    num = int(input())
    a = input().split()
    b = input().split()
    count = 0
    for i in range(num):
        a[i] = int(a[i])
        b[i] = int(b[i])
    for i in range(1,1001):
        flag = True
        for j in range(num):
            if i < a[j] or i > b[j]:
                flag = False
        if flag:
            count += 1
    print(count)

=======
Suggestion 5

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    print(len([x for x in range(1, 1001) if all([a <= x <= b for a, b in zip(A, B)])]))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = 0
    for i in range(1, 1001):
        flag = True
        for j in range(n):
            if i < a[j] or i > b[j]:
                flag = False
                break
        if flag:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(1000):
        flag = True
        for j in range(n):
            if i < a[j] or b[j] < i:
                flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for x in range(1, 1001):
        for i in range(n):
            if x < a[i] or b[i] < x:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 9

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(1, 1001):
        ok = True
        for j in range(n):
            if not (a[j] <= i <= b[j]):
                ok = False
        if ok:
            ans += 1
    print(ans)

solve()

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    min = 0
    max = 1000
    for i in range(N):
        if A[i] > min:
            min = A[i]
        if B[i] < max:
            max = B[i]

    if min > max:
        print(0)
    else:
        print(max - min + 1)
