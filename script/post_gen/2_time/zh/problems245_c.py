Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    #print(N, K, A, B)
    #print(len(A), len(B))
    #print(A[0], A[1])
    #print(B[0], B[1])

    for i in range(N):
        if abs(A[i] - B[i]) > K:
            print("No")
            return

    print("Yes")

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    
    for i in range(n):
        if abs(a[i] - b[i]) > k:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def readinput():
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    return n,k,a,b

=======
Suggestion 5

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_max = max(a)
    a_min = min(a)
    b_max = max(b)
    b_min = min(b)

    if a_max - a_min > k or b_max - b_min > k:
        print("No")
        return

    print("Yes")
    if a_max > b_max:
        for i in range(n):
            if a[i] > b[i]:
                print(b_max, end=" ")
            else:
                print(a[i], end=" ")
    else:
        for i in range(n):
            if a[i] < b[i]:
                print(a_max, end=" ")
            else:
                print(b[i], end=" ")

=======
Suggestion 6

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 二分探索
    def check(x):
        cnt = 0
        for i in range(N):
            cnt += abs(A[i] - x)
            cnt += abs(B[i] - x)
            cnt -= abs(A[i] - B[i])
        return cnt <= 2 * K

    # 二分探索
    ok = 0
    ng = 2 * 10 ** 9 + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print('Yes' if ok == 0 else 'No')

=======
Suggestion 7

def solve():
    pass

=======
Suggestion 8

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 二分法
    def check(x):
        cnt = 0
        for i in range(n):
            if a[i] > x:
                cnt += 1
            else:
                cnt -= 1
        for i in range(n):
            if b[i] > x:
                cnt += 1
            else:
                cnt -= 1
        return cnt >= 0

    left = -1
    right = 10 ** 9 + 1
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid
    if right == 10 ** 9 + 1:
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def check(a,b,k):
    # a,b,k = map(int, input().split())
    a = list(map(int, a.split()))
    b = list(map(int, b.split()))
    for i in range(len(a)):
        if abs(a[i]-b[i])>k:
            return "No"
    return "Yes"

a = "1 1 1000000000 1000000000"
b = "1 1000000000 1 1000000000"
k = 1000000000
print(check(a,b,k))

=======
Suggestion 10

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    m = 0
    for i in range(N):
        m = max(m, abs(A[i] - B[i]))
    if m <= K:
        print('Yes')
    else:
        print('No')

solve()
