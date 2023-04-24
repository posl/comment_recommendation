Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * N
    for i in range(N):
        if K >= N - i:
            ans[i] = a[i] + (K - (N - i)) // N
            K -= (K - (N - i)) // N * N
        else:
            ans[i] = a[i]
    for i in range(K):
        ans[i] += 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    C = [0] * N
    for i in range(N):
        C[i] = A[i] - (i + 1)
    #print(C)
    for i in range(N):
        if C[i] >= K:
            print(K + i)
            K = 0
            break
        else:
            K -= C[i]
    if K > 0:
        for i in range(N):
            print(A[i] + K // N + int(i < K % N))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    for i in range(N):
        if K >= N:
            ans[i] += 1
            K -= 1
        else:
            ans[A.index(A[i])] += K // N
            K %= N
    for i in range(N):
        print(ans[i])

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    if k <= n:
        print(k)
        for i in range(n - k):
            print(0)
        return

    b = [0] * n
    for i in range(n):
        b[i] = k // n
    for i in range(k % n):
        b[i] += 1

    for i in range(n):
        b[i] += (n - a[i]) // n

    for i in range(n):
        print(b[i])

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    ans = [0] * (N + 1)
    for i in range(N):
        ans[i + 1] = (A[i + 1] - A[i]) * (i + 1)
    for i in range(N):
        ans[i + 1] += ans[i]
    for i in range(N):
        if K <= ans[i + 1]:
            print(A[i] + (K - ans[i]) // (i + 1))
            break

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    cnt = [0] * N
    for i in range(N):
        cnt[i] = (A[i] - 1) // K

    ans = [0] * N
    for i in range(N):
        ans[i] = cnt[i] + 1

    for i in range(N):
        if i == 0:
            continue
        if cnt[i] == cnt[i - 1]:
            ans[i] = ans[i - 1]

    for i in range(N):
        print(ans[i])

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if K >= N:
        print(1)
        for i in range(N-1):
            print(1)
        return
    # まずはKを配る
    for i in range(K):
        print(a[i])
    # あまりを配る
    for i in range(K, N):
        print(a[K-1])

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    num = k // n
    mod = k % n
    for i in range(n):
        ans[i] += num
    for i in range(mod):
        ans[i] += 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    ans = [0] * N
    for i in range(N):
        ans[i] = K // N
        if i < K % N:
            ans[i] += 1
    #print(ans)
    for i in range(N):
        if a[i] <= K:
            print(ans[i])
        else:
            print(0)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 配列Aをソート
    A.sort()
    # 配列Bを作成
    B = [0 for _ in range(N)]
    for i in range(N):
        B[i] = A[i] - i - 1
    # print(B)
    # 配列Bの中でK以下の最大値を探す
    left = 0
    right = N - 1
    while right - left > 1:
        mid = (left + right) // 2
        if B[mid] <= K:
            left = mid
        else:
            right = mid
    # print(left, right)

    # K以下の最大値のインデックスを取得
    if B[right] <= K:
        index = right
    else:
        index = left
    # print(index)

    # お菓子の配り方
    if index == N - 1:
        # 全員に1個ずつ配る
        for i in range(N):
            print(1 + K // N)
    else:
        # K以下の最大値のインデックスの国民に1個ずつ配る
        for i in range(N):
            if i <= index:
                print(1)
            else:
                print(0)
        # K - B[index]個のお菓子を配る
        for i in range(K - B[index]):
            print(A[index] + i + 1)
