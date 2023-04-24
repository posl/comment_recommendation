Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if p[i] != i + 1:
            cnt += 1
    if cnt <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 2

def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if p[i] != i+1:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 3

def main():
    N = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if p[i] != i+1:
            cnt += 1
    print('YES' if cnt <= 2 else 'NO')

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(n - 1):
        if p[i] > p[i + 1]:
            cnt += 1
            if cnt > 1:
                print("NO")
                return
            if i + 2 < n and p[i + 2] < p[i]:
                p[i], p[i + 2] = p[i + 2], p[i]
            else:
                p[i], p[i + 1] = p[i + 1], p[i]
    print("YES")

=======
Suggestion 5

def main():
    N = int(input())
    p = list(map(int, input().split()))
    p2 = sorted(p)
    if p == p2:
        print("YES")
    else:
        count = 0
        for i in range(N):
            if p[i] == p2[i]:
                pass
            else:
                count += 1
        if count == 2:
            print("YES")
        else:
            print("NO")

=======
Suggestion 6

def main():
    N = int(input())
    p = list(map(int, input().split()))
    p.sort()
    if p == list(range(1, N+1)):
        print('YES')
    else:
        print('NO')

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    c = 0
    d = 0
    for i in range(n):
        if a[i] != b[i]:
            c += 1
        if a[i] == b[i]:
            d += 1
    if c == 2 or c == 0:
        print("YES")
    else:
        print("NO")
main()

=======
Suggestion 8

def main():
    N = int(input())
    p = list(map(int, input().split()))
    if p == sorted(p):
        print('YES')
    else:
        print('NO')

=======
Suggestion 9

def swap(x, i, j):
    x[i], x[j] = x[j], x[i]
