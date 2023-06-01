Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # print(n, k)
    # print(a)

    a.sort()
    # print(a)

    ans = k // n
    b = k % n
    # print(ans)
    # print(b)

    for i in range(n):
        if a[i] <= b:
            print(ans+1)
        else:
            print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = k // n
    B = sorted(A)
    for i in range(k % n):
        ans[B[i] - 1] += 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [k//n]*n
    k %= n
    for i in range(k):
        ans[a[i]-1] += 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 4

def prob208_c():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if k>=n:
        if k%n==0:
            print(k//n)
        else:
            print(k//n+1)
        return
    else:
        b = k
        for i in range(n):
            if a[i]<b:
                b = a[i]
        print(b)
        return

prob208_c()

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    k = K
    for i in range(N):
        if k >= N:
            A[i] += k // N
        else:
            A[i] += 0
        k = k - 1
    for i in range(N):
        print(A[i])

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(a[0] + K)
    #print(a)
    ans = [K//N for i in range(N)]
    #print(ans)
    tmp = K%N
    for i in range(tmp):
        ans[a[i]-1] += 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a_sorted = sorted(a)
    a_sorted.append(a_sorted[0]+k)
    for i in range(n):
        if a_sorted[i+1] == a_sorted[i]:
            print(k//n)
        else:
            print(k//n+1)

=======
Suggestion 9

def solve(n,k,a):
    # 二分探索
    def is_ok(arg):
        # 条件を満たすかどうか？問題ごとに定義
        # ngとokの中点midをargとして受け取る
        # ここで条件式を書く
        # return mid >= 0
        # ここで条件式を書く
        return sum(max(0, a_i - arg) for a_i in a) <= k

    # 二分探索
    def meguru_bisect(ng, ok):
        # okとngのどちらが大きいかわからないことを考慮
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    # 解の存在範囲を初期化
    ok = max(a)
    ng = 0
    # 二分探索
    ans = meguru_bisect(ng, ok)
    return ans

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(a[0] + K)
    b = [0] * N
    for i in range(N):
        b[i] = a[i + 1] - a[i]
    m = min(b)
    min_index = b.index(m)
    for i in range(N):
        if i == min_index:
            print(a[i] + K // N + 1)
        else:
            print(a[i] + K // N)
