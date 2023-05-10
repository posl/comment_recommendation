Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    ans = []
    for i in range(q):
        ans.append(k[i] + i)
    count = 0
    for i in range(n):
        if count < q and a[i] == ans[count]:
            count += 1
    for i in range(q):
        ans[i] += count
    for i in range(q):
        print(ans[i])

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    ans = []
    # Aに含まれない数をKより大きい順に並べる
    B = [i for i in range(1, A[0])] + [i for i in range(A[-1]+1, 10**18+1)]
    # print(B)
    # Kより小さい数をAに追加し、Aをソートする
    A += B
    A.sort()
    # print(A)
    for k in K:
        ans.append(A[k-1])
    print(*ans, sep='\n')

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = []
    for i in range(Q):
        K.append(int(input()))

    # 各要素の差分を求める
    diff = []
    for i in range(N - 1):
        diff.append(A[i + 1] - A[i])
    # print(diff)

    # diff の累積和を求める
    cumsum = [diff[0]]
    for i in range(1, N - 1):
        cumsum.append(cumsum[i - 1] + diff[i])
    # print(cumsum)

    # 累積和の最大公約数を求める
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    ans = []
    for i in range(Q):
        # print("K[i] = ", K[i])
        # print("cumsum = ", cumsum)
        # print("A = ", A)
        # print("N = ", N)
        # print("A[N - 1] = ", A[N - 1])
        # print("A[N - 2] = ", A[N - 2])
        # print("cumsum[N - 2] = ", cumsum[N - 2])
        # print("cumsum[N - 3] = ", cumsum[N - 3])
        if K[i] <= A[0]:
            ans.append(K[i])
        elif K[i] > A[N - 1] - A[N - 2]:
            ans.append(A[N - 1] + K[i] - (A[N - 1] - A[N - 2]))
        else:
            left = 0
            right = N - 2
            while right - left > 1:
                mid = (right + left) // 2
                if K[i] <= cumsum[mid]:
                    right = mid
                else:
                    left = mid
            # print("left = ", left)
            # print("right = ", right)
            # print("cumsum[right] = ", cumsum[right])
            # print("cumsum[left] = ", cumsum[left])
            # print("A

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    #A = sorted(A)
    #print(A)
    #print(K)
    for k in K:
        cnt = 0
        for a in A:
            if a <= k:
                cnt += 1
            else:
                break
        print(k+cnt)

=======
Suggestion 5

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for i in range(q)]
    ans = []
    for i in range(n-1):
        ans.append(a[i+1]-a[i]-1)
    for i in range(q):
        if k[i] <= a[0]-1:
            print(k[i])
        elif k[i] >= a[n-1]+n-1:
            print(k[i]-(a[n-1]+n-1)+a[n-1])
        else:
            for j in range(n-1):
                if ans[j] >= k[i]:
                    print(a[j]+k[i])
                    break
                else:
                    k[i] -= ans[j]

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    ans = []
    for i in range(q):
        ans.append(k[i] + i)
    count = 0
    for i in range(q):
        for j in range(n):
            if ans[i] <= a[j]:
                count += 1
                break
    for i in range(q):
        print(ans[i] + count)

=======
Suggestion 7

def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    from bisect import bisect_left

    N, Q = map(int, readline().split())
    A = list(map(int, readline().split()))
    K = [int(readline()) for _ in range(Q)]

    for i in range(Q):
        k = K[i]
        idx = bisect_left(A, k)
        if idx == 0:
            print(k)
        else:
            print(k+idx)

=======
Suggestion 8

def problem205d():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    ans = []
    for i in range(q):
        tmp = k[i]
        ans.append(tmp)
        for j in range(n):
            if tmp >= a[j]:
                tmp += 1
        ans[i] = tmp
    for i in range(q):
        print(ans[i])

=======
Suggestion 9

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = []
    for i in range(q):
        k.append(int(input()))

    ans = []
    for i in range(q):
        ans.append(k[i] + i)

    for i in range(q):
        if ans[i] <= a[0]:
            ans[i] = ans[i] + n - 1
            continue
        if ans[i] >= a[n - 1]:
            ans[i] = ans[i] + n
            continue
        for j in range(n - 1):
            if a[j] < ans[i] and ans[i] <= a[j + 1]:
                ans[i] = ans[i] + j + 1
                break

    for i in range(q):
        print(ans[i])
