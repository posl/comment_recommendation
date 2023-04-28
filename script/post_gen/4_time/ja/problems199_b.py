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
            if a[i] <= x <= b[i]:
                continue
            else:
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

    ans = 0
    for x in range(1, 1001):
        ok = True
        for i in range(n):
            if x < a[i] or x > b[i]:
                ok = False
        if ok:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
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
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    cnt = 0
    for i in range(1, 1001):
        flag = True
        for j in range(n):
            if not (a[j] <= i <= b[j]):
                flag = False
                break
        if flag:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    print(max(0, min(b) - max(a) + 1))

=======
Suggestion 6

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
        if flag == True:
            count += 1

    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_a = max(a)
    min_b = min(b)
    if min_b >= max_a:
        print(min_b - max_a + 1)
    else:
        print(0)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(1,1001):
        if all(a[j] <= i <= b[j] for j in range(n)):
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = 0
    for i in range(1, 1000 + 1):
        if all(a[j] <= i <= b[j] for j in range(n)):
            x += 1
    print(x)

=======
Suggestion 10

def f(n, a, b):
    #print(n, a, b)
    min_a = max(a)
    max_b = min(b)
    if min_a > max_b:
        return 0
    else:
        return max_b - min_a + 1
