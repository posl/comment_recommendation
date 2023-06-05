Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    n = len(a)
    ans = [0] * n
    for i in range(n):
        ans[i] = i
    for i in range(1, n):
        if a[i] == a[i-1]:
            ans[i] = ans[i-1]
    for i in range(n-2, -1, -1):
        if a[i] == a[i+1]:
            ans[i] = ans[i+1]
    for i in range(n):
        print(ans[i])

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max_A = A[-1]
    cnt = [0] * (max_A + 1)
    for i in range(N):
        if i == 0:
            cnt[A[i]] = 1
        else:
            if A[i] != A[i - 1]:
                cnt[A[i]] = 1
            else:
                cnt[A[i]] += 1
    ans = [0] * N
    for i in range(1, max_A + 1):
        if cnt[i] == 0:
            continue
        for j in range(i, max_A + 1, i):
            ans[cnt[i] - 1] += cnt[j]
    for i in range(N):
        print(ans[i])

solve()

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    for i in range(N):
        ans[i] = len(set(A[i:]))
    print(*ans, sep='\n')

=======
Suggestion 4

def solve(n, a):
    a.sort()
    s = set()
    ans = [0] * n
    for i in range(n-1, -1, -1):
        x = a[i]
        if x in s:
            ans[i] = ans[i+1]
        else:
            s.add(x)
            ans[i] = ans[i+1] + 1
    return ans

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    k = 0
    for i in range(n):
        if i == 0:
            print(0)
        else:
            if a[i] != a[i-1]:
                k += 1
                print(k)
            else:
                print(k)

=======
Suggestion 6

def problems273_c():
    pass

=======
Suggestion 7

def solve():
    return

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    k = 0
    for i in range(n):
        if i == 0:
            print(0)
        else:
            if a[i] != a[i-1]:
                k += 1
            print(k)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(10**10)
    k = 0
    ans = [0]*n
    for i in range(n):
        if a[i] != a[i+1]:
            ans[k] += 1
            k = 0
        else:
            k += 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    # print(A)
    ans = [0] * N
    for i in range(N):
        if i == 0:
            ans[i] = 1
        elif A[i] != A[i-1]:
            ans[i] = 1
        else:
            ans[i] = ans[i-1] + 1
    # print(ans)
    for i in range(N):
        print(ans[ans[i]-1])
