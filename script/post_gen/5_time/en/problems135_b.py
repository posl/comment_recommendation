Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p_sorted = sorted(p)
    count = 0
    for i in range(n):
        if p[i] != p_sorted[i]:
            count += 1
    if count == 2 or count == 0:
        print("YES")
    else:
        print("NO")

=======
Suggestion 2

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
Suggestion 3

def main():
    N = int(input())
    p = list(map(int,input().split()))
    p_sorted = sorted(p)
    count = 0
    for i in range(N):
        if p[i] != p_sorted[i]:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 4

def main():
    N = int(input())
    p = [int(x) for x in input().split()]
    count = 0
    for i in range(N):
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
    p = list(map(int, input().split()))
    q = sorted(p)
    if p == q:
        print("YES")
        return
    for i in range(n):
        for j in range(i + 1, n):
            r = p.copy()
            r[i], r[j] = r[j], r[i]
            if r == q:
                print("YES")
                return
    print("NO")

=======
Suggestion 6

def main():
    N = int(input())
    p = list(map(int, input().split()))
    p_sorted = sorted(p)
    if p == p_sorted:
        print('YES')
    else:
        for i in range(N):
            for j in range(i+1, N):
                p[i], p[j] = p[j], p[i]
                if p == p_sorted:
                    print('YES')
                    return
                p[i], p[j] = p[j], p[i]
        print('NO')

=======
Suggestion 7

def swap(i, j, p):
    tmp = p[i]
    p[i] = p[j]
    p[j] = tmp
    return p

=======
Suggestion 8

def main():
    N = int(input())
    p = [int(x) for x in input().split()]
    if all(p[i] == i+1 for i in range(N)):
        print("YES")
    else:
        print("NO")

=======
Suggestion 9

def check(p):
    for i in range(1, len(p)):
        if p[i] < p[i-1]:
            return False
    return True

=======
Suggestion 10

def main():
    N = int(input())
    p = [int(x) for x in input().split()]
    p = [0] + p
    for i in range(1, N):
        if p[i] > p[i+1]:
            for j in range(i+1, N+1):
                if p[i] > p[j]:
                    print("NO")
                    return
            print("YES")
            return
    print("YES")
    return
