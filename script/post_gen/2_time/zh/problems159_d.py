Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = [0] * n
    for i in range(n):
        ans[a[i]-1] += 1
    ans = [i*(i-1)//2 for i in ans]
    total = sum(ans)
    for i in range(n):
        print(total - ans[a[i]-1] + 1)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * (N + 1)
    for a in A:
        cnt[a] += 1
    ans = sum([c * (c - 1) // 2 for c in cnt])
    for a in A:
        print(ans - (cnt[a] - 1))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] += 1
    ans = 0
    for i in range(N):
        ans += B[i] * (B[i] - 1) // 2
    for i in range(N):
        print(ans - (B[A[i] - 1] - 1))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0]*(N+1)
    count = 0
    for i in range(N):
        B[A[i]] += 1
    for i in range(N):
        count += B[i]*(B[i]-1)/2
    for i in range(N):
        print(int(count-(B[A[i]]-1)))

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    c = [0] * (n+1)
    for x in a:
        c[x] += 1
    ans = 0
    for x in c:
        ans += x * (x-1) // 2
    for x in a:
        print(ans - c[x] + 1)

=======
Suggestion 6

def f(n):
    return n*(n-1)//2

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * N
    for i in range(N):
        cnt[A[i] - 1] += 1
    ans = 0
    for i in range(N):
        ans += cnt[i] * (cnt[i] - 1) // 2
    for i in range(N):
        print(ans - (cnt[A[i] - 1] - 1))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0] * N
    for a in A:
        count[a - 1] += 1
    ans = 0
    for i in range(N):
        ans += count[i] * (count[i] - 1) // 2
    for i in range(N):
        print(ans - (count[A[i] - 1] - 1))

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    cnt = 0
    ans = 0
    for i in range(n):
        if a[i] == a[i+1]:
            cnt += 1
        else:
            ans += cnt * (cnt + 1) // 2
            cnt = 0
    for i in range(n):
        print(ans)
        ans += 1
        if i == n - 1 or a[i] != a[i+1]:
            ans -= 1
    return

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 1. 遍历所有A[i]，找到相同的A[i]的索引，索引差记为d
    # 2. 从N-1个球中选出两个，不考虑顺序，即N-1选2，记为C(N-1,2)
    # 3. 从d个相同的球中选出2个，不考虑顺序，记为C(d,2)
    # 4. 从N-1个球中选出两个，不考虑顺序，即N-1选2，记为C(N-1,2)
    # 5. 从d个相同的球中选出2个，不考虑顺序，记为C(d,2)
    # 6. 从N-1个球中选出两个，不考虑顺序，即N-1选2，记为C(N-1,2)
    # 7. 从d个相同的球中选出2个，不考虑顺序，记为C(d,2)
    # 8. 从N-1个球中选出两个，不考虑顺序，即N-1选2，记为C(N-1,2)
    # 9. 从d个相同的球中选出2个，不考虑顺序，记为C(d,2)
    # 10. 从N-1个球中选出两个，不考虑顺序，即N-1选2，记为C(N-1,2)
    # 11. 从d个相同的球中选出2个，不考虑顺序，记为C(d,2)
    # 12. 从N-1个球中选出两个，不考虑顺序，即N-1选2，记为C(N-1,2)
    # 13. 从d个相同的球中选出2个，不考虑顺
