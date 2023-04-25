Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M == 0:
        print(1)
        return
    if M == N:
        print(0)
        return
    A.sort()
    A = [0] + A + [N+1]
    B = []
    for i in range(M+1):
        B.append(A[i+1]-A[i]-1)
    B.sort()
    B = B[::-1]
    k = B[0]
    ans = 0
    for b in B:
        ans += -(-b//k)
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        return
    if M == N:
        print(0)
        return
    if M == 1:
        print(min(A[0], N - A[0] + 1))
        return
    diff = []
    for i in range(M - 1):
        diff.append(A[i + 1] - A[i] - 1)
    diff.sort()
    ans = N
    for i in range(M - 1):
        ans = min(ans, diff[i] + 1)
    print(ans)

=======
Suggestion 3

def solve(n, m, a):
    if m == 0:
        return 1
    a.sort()
    b = [a[0] - 1]
    for i in range(1, m):
        b.append(a[i] - a[i - 1] - 1)
    b.append(n - a[m - 1])
    d = max(b)
    return (d + 1) // 2 + 1

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [A[0]-1]
    for i in range(M-1):
        B.append(A[i+1]-A[i]-1)
    B.append(N-A[-1])
    B = [b for b in B if b != 0]
    if len(B) == 0:
        print(0)
        return
    k = min(B)
    ans = 1
    for b in B:
        if b % k == 0:
            ans += b//k
        else:
            ans += b//k + 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [N + 1]
    B = [A[i + 1] - A[i] - 1 for i in range(M + 1)]
    if M == 0:
        print(1)
        return
    k = min([b for b in B if b > 0])
    for b in B:
        if b > 0:
            k = gcd(k, b)
    print((max(B) + k - 1) // k)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    if M == 0:
        print(1)
        return
    
    A.sort()
    A.append(N + 1)
    B = [A[0] - 1]
    for i in range(M):
        B.append(A[i + 1] - A[i] - 1)
    B.sort(reverse = True)
    
    ans = 0
    for i in range(M):
        if B[i] > 0:
            ans += B[i]
    
    print(ans + 1)

=======
Suggestion 7

def solve(n, m, a):
    if m == 0:
        return 1
    a.sort()
    a = [0] + a + [n + 1]
    b = [a[i + 1] - a[i] - 1 for i in range(m + 1)]
    b = list(filter(lambda x: x > 0, b))
    k = min(b)
    return sum([b[i] // k for i in range(len(b))]) + len(b)

=======
Suggestion 8

def get_input():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    return N, M, A

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(N+1)
    A.insert(0, 0)

    if M == 0:
        print(1)
        exit()

    # 空白の長さをリスト化
    S = []
    for i in range(M+1):
        if A[i+1] - A[i] - 1 != 0:
            S.append(A[i+1] - A[i] - 1)

    # 空白の長さの最大値を求める
    maxS = max(S)

    # 空白の長さが最大値の場合のスタンプの幅を求める
    K = []
    for i in range(M+1):
        if A[i+1] - A[i] - 1 == maxS:
            K.append(A[i+1] - A[i] - 1)
            break
        elif A[i+1] - A[i] - 1 == maxS - 1:
            K.append(A[i+1] - A[i] - 1)
        elif A[i+1] - A[i] - 1 == maxS - 2:
            K.append(A[i+1] - A[i] - 1)

    if len(K) == 1:
        print(maxS)
    else:
        print(maxS - 1)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(n + 1)
    m += 1
    if m == 1:
        print(1)
        return
    diff = []
    for i in range(1, m):
        if a[i] - a[i - 1] > 1:
            diff.append(a[i] - a[i - 1] - 1)
    if len(diff) == 0:
        print(0)
        return
    k = min(diff)
    ans = 0
    for d in diff:
        ans += (d + k - 1) // k
    print(ans)
