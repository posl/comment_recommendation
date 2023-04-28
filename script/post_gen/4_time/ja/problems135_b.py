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
    if cnt == 2 or cnt == 0:
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
        print('YES')
    else:
        print('NO')

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p_sorted = sorted(p)
    count = 0
    for i in range(n):
        if p[i] != p_sorted[i]:
            count += 1
    if count <= 2:
        print('YES')
    else:
        print('NO')

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if p[i] == i+1:
            cnt += 1
    if cnt == n-2 or cnt == n:
        print("YES")
    else:
        print("NO")

=======
Suggestion 5

def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if i + 1 != p[i]:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 6

def main():
    N = int(input())
    p = list(map(int,input().split()))
    p_sort = sorted(p)
    count = 0
    for i in range(N):
        if p[i] != p_sort[i]:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 7

def main():
    N = int(input())
    p = list(map(int, input().split()))
    p_sort = sorted(p)
    count = 0
    for i in range(N):
        if p[i] == p_sort[i]:
            count += 1
    if count == N - 2 or count == N:
        print("YES")
    else:
        print("NO")

=======
Suggestion 8

def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    for i, p in enumerate(P):
        if i+1 != p:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 9

def check(p):
    for i in range(len(p)-1):
        if p[i] > p[i+1]:
            return False
    return True

=======
Suggestion 10

def main():
    N = int(input())
    p = list(map(int, input().split()))
    answer = "YES"
    for i in range(N):
        if p[i] != i+1:
            answer = "NO"
    print(answer)
