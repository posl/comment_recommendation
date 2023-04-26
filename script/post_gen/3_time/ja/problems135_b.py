Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    N = int(input())
    p = list(map(int, input().split()))
    sorted_p = sorted(p)
    count = 0
    for i in range(N):
        if p[i] != sorted_p[i]:
            count += 1
    if count == 0 or count == 2:
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
        print('YES')
    else:
        print('NO')

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n-1):
        if p[i] != i+1:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int,input().split()))
    cnt = 0
    for i in range(n-1):
        if p[i] != i+1:
            cnt += 1
    if cnt <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 6

def main():
    N = int(input())
    p = list(map(int,input().split()))
    p2 = sorted(p)
    count = 0
    for i in range(N):
        if p[i] != p2[i]:
            count += 1

    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    for i in range(n):
        if i+1 != p[i]:
            for j in range(i+1, n):
                if j+1 == p[i]:
                    p[i], p[j] = p[j], p[i]
                    break
            else:
                print("NO")
                break
    else:
        print("YES")

=======
Suggestion 8

def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 'YES'
    for i in range(N):
        if p[i] != i + 1:
            ans = 'NO'
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))
    P.sort()
    if P == list(range(1, N+1)):
        print("YES")
    else:
        print("NO")

=======
Suggestion 10

def swap(a, b, p):
    tmp = p[a]
    p[a] = p[b]
    p[b] = tmp
