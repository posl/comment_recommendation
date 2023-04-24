Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if p[i] != i+1:
            cnt += 1
    if cnt <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
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
    sorted_p = sorted(p)
    count = 0
    for i in range(N):
        if p[i] != sorted_p[i]:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 4

def main():
    N = int(input())
    p = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if p[i] != i+1:
            count += 1
    if count == 2 or count == 0:
        print("YES")
    else:
        print("NO")

=======
Suggestion 5

def main():
    N = int(input())
    p = list(map(int, input().split()))
    q = sorted(p)
    count = 0
    for i in range(N):
        if p[i] != q[i]:
            count += 1
    if count == 2 or count == 0:
        print("YES")
    else:
        print("NO")

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if p[i] == i+1:
            count += 1
    if count == n:
        print("YES")
    elif count == n - 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [i for i in range(1, n+1)]
    count = 0
    for i in range(n):
        if p[i] != q[i]:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))
    if p == sorted(p):
        print("YES")
    else:
        print("NO")

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        if p[i] != i+1:
            ans += 1

    if ans == 0 or ans == 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 10

def swap(a, b):
    return b, a
