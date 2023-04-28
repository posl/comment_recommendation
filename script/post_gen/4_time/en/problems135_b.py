Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    p = list(map(int, input().split()))
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
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = sorted(p)
    cnt = 0
    for i in range(n):
        if p[i] != q[i]:
            cnt += 1
    if cnt <= 2:
        print("YES")
    else:
        print("NO")

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n):
        if p[i-1] != i:
            count += 1
    if count <= 2:
        print('YES')
    else:
        print('NO')

=======
Suggestion 4

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    if p == sorted(p):
        print("YES")
        return
    for i in range(n):
        for j in range(i+1, n):
            p[i], p[j] = p[j], p[i]
            if p == sorted(p):
                print("YES")
                return
            p[i], p[j] = p[j], p[i]
    print("NO")
    return
solve()

=======
Suggestion 5

def main():
    N = int(input())
    p = list(map(int, input().split()))
    sorted_p = sorted(p)
    if p == sorted_p:
        print("YES")
        return
    for i in range(N-1):
        for j in range(i+1, N):
            if p[i] > p[j]:
                p[i], p[j] = p[j], p[i]
                if p == sorted_p:
                    print("YES")
                    return
                p[i], p[j] = p[j], p[i]
    print("NO")

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))
    sorted_p = sorted(p)
    if p == sorted_p:
        print('YES')
        exit()
    for i in range(n):
        for j in range(i+1, n):
            p[i], p[j] = p[j], p[i]
            if p == sorted_p:
                print('YES')
                exit()
            p[i], p[j] = p[j], p[i]
    print('NO')

=======
Suggestion 7

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    p_sorted = sorted(p)
    diff_count = 0
    for i in range(n):
        if p[i] != p_sorted[i]:
            diff_count += 1
    if diff_count <= 2:
        print('YES')
    else:
        print('NO')

=======
Suggestion 8

def main():
    N = int(input())
    P = list(map(int, input().split()))
    P_sorted = sorted(P)
    if P == P_sorted:
        print("YES")
    else:
        for i in range(N):
            for j in range(i+1, N):
                P_temp = P.copy()
                P_temp[i], P_temp[j] = P_temp[j], P_temp[i]
                if P_temp == P_sorted:
                    print("YES")
                    return
        print("NO")

=======
Suggestion 9

def main():
    N = int(input())
    p = list(map(int, input().split()))

    p_sorted = sorted(p)

    if p_sorted == p:
        print("YES")
    else:
        for i in range(N):
            for j in range(i + 1, N):
                p_swapped = p[:]
                p_swapped[i], p_swapped[j] = p_swapped[j], p_swapped[i]
                if p_swapped == p_sorted:
                    print("YES")
                    return
        print("NO")

=======
Suggestion 10

def main():
    N = int(input())
    p = list(map(int, input().split()))
    q = list(range(1, N+1))
    if p == q:
        print('YES')
    else:
        for i in range(N):
            for j in range(i+1, N):
                r = p[:]
                r[i], r[j] = r[j], r[i]
                if r == q:
                    print('YES')
                    return
        print('NO')
