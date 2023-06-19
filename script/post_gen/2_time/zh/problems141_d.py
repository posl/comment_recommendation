Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(m):
        a[0] = a[0]>>1
        a.sort(reverse=True)
    print(sum(a))

=======
Suggestion 2

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (2 ** (m - i))
    print(ans // (2 ** m))

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    for i in range(m):
        a[0] = a[0] // 2
        a.sort(reverse=True)
    print(sum(a))

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(M):
        A[0] = A[0] // 2
        A.sort(reverse=True)
    print(sum(A))

solve()

=======
Suggestion 5

def buy_goods(n, m, a):
    a.sort()
    cost = 0
    for i in range(n):
        cost += a[i]
    for i in range(m):
        cost = cost / 2
    return int(cost)

=======
Suggestion 6

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(m):
        a[-1] = a[-1]//2
        a.sort()
    print(sum(a))

=======
Suggestion 7

def solve(n,m,a):
    a.sort()
    for i in range(m):
        a[-1] = a[-1]//2
        a.sort()
    return sum(a)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(m):
        a[i] = a[i] // 2
    print(sum(a))

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    a.append(0)
    count = 0
    for i in range(n):
        if a[i] > a[i+1]:
            count += 1
        else:
            count += 1
            break
    print(count)
    return 0
