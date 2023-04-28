Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    diff = 0
    for i in range(n):
        diff += abs(a[i] - b[i])

    if diff <= k and (diff - k) % 2 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    maxA = max(A)
    maxB = max(B)
    if maxA > maxB:
        print('No')
        return

    A.sort()
    B.sort()
    A = A[::-1]
    B = B[::-1]

    for i in range(N):
        if A[i] > B[i]:
            print('No')
            return

    # 二分探索
    left = 0
    right = 10**18
    while left + 1 < right:
        mid = (left + right) // 2
        cnt = 0
        for i in range(N):
            cnt += bisect_right(B, mid + A[i])
        if cnt >= N:
            right = mid
        else:
            left = mid
    print('Yes')

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    if A[0] + K < B[0] or A[-1] - K > B[-1]:
        print('No')
        return

    for i in range(N):
        if A[i] + K < B[i]:
            print('No')
            return

    print('Yes')

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    left = 0
    right = 10**9 + 1
    while left < right:
        mid = (left + right) // 2
        is_ok = True
        for i in range(n):
            if a[i] > mid:
                if b[i] >= a[i] - mid:
                    continue
                else:
                    is_ok = False
                    break
            else:
                if b[i] >= a[i] - mid or b[i] <= a[i] + mid:
                    continue
                else:
                    is_ok = False
                    break
        if is_ok:
            right = mid
        else:
            left = mid + 1
    print("Yes" if left <= k else "No")

=======
Suggestion 5

def main():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A.sort()
    B.sort()
    B.reverse()
    
    #print(A)
    #print(B)
    
    if A[0] + K < B[0]:
        print("No")
        return
    
    if A[0] > B[0]:
        print("No")
        return
    
    for i in range(1, N):
        if A[i] > B[i]:
            print("No")
            return
        if A[i] + K < B[i]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # print(n, k)
    # print(a)
    # print(b)

    a.sort()
    b.sort()

    # print(a)
    # print(b)

    # for i in range(n):
    #     if abs(a[i] - b[i]) > k:
    #         print("No")
    #         return

    # print("Yes")

    # print("Yes" if all(abs(a[i] - b[i]) <= k for i in range(n)) else "No")

    print("Yes" if all(abs(a[i] - b[i]) <= k for i in range(n)) else "No")

=======
Suggestion 7

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    def check(x):
        cnt = 0
        for i in range(n):
            cnt += bisect.bisect_right(b, x - a[i])
        return cnt >= k

    ok = 0
    ng = 10 ** 18 + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid

    print(ok)

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    A.sort()
    B.sort()
    B.reverse()
    
    #print(A)
    #print(B)
    
    for i in range(N):
        if abs(A[i]-B[i]) > K:
            print("No")
            exit()
    
    print("Yes")
    
main()

=======
Suggestion 9

def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    A.reverse()
    B.reverse()
    #print(A)
    #print(B)
    #print(A[0],B[0])
    if A[0] < B[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    #A,Bの差の絶対値がK以下であることを確認する
    for i in range(N):
        if abs(A[i] - B[i]) > K:
            print("No")
            exit()
    print("Yes")
