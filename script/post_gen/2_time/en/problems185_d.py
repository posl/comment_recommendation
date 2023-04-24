Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M == 0:
        print(1)
        return
    A.sort()
    A = [0] + A + [N + 1]
    D = [A[i + 1] - A[i] - 1 for i in range(M + 1)]
    D = [d for d in D if d != 0]
    K = max(D)
    print((sum(D) + K - 1) // K + 1)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [N + 1]
    B = []
    for i in range(M + 1):
        B.append(A[i + 1] - A[i] - 1)
    B = list(filter(lambda x: x > 0, B))
    if len(B) == 0:
        print(0)
        return
    k = min(B)
    for b in B:
        k = gcd(k, b)
    print((max(B) + k - 1) // k)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    if M == 0:
        print(1)
        return

    if N == M:
        print(0)
        return

    diff = []
    for i in range(M - 1):
        diff.append(A[i + 1] - A[i] - 1)

    diff.sort(reverse=True)

    if diff[0] == 0:
        print(1)
        return

    print(max(1, (diff[0] - 1) // (M - 1) + 1))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [A[0] - 1]
    for i in range(1, M):
        B.append(A[i] - A[i - 1] - 1)
    B.append(N - A[M - 1])
    if M == 0:
        print(1)
        return
    k = min(B)
    if k <= 0:
        print(M)
        return
    ans = M
    for b in B:
        ans += b // k
        if b % k == 0:
            ans -= 1
    print(ans)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a + [n + 1]
    a.sort()
    b = []
    for i in range(m + 1):
        b.append(a[i + 1] - a[i] - 1)
    b = [x for x in b if x > 0]
    k = min(b)
    ans = 0
    for x in b:
        ans += (x + k - 1) // k
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.insert(0, 0)
    A.append(N + 1)
    B = []
    for i in range(M + 1):
        if A[i + 1] - A[i] - 1 > 0:
            B.append(A[i + 1] - A[i] - 1)
    if len(B) == 0:
        print(0)
        return
    K = min(B)
    for i in range(len(B)):
        if B[i] % K == 0:
            B[i] = B[i] // K
        else:
            B[i] = B[i] // K + 1
    print(sum(B))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        return

    if N == M:
        print(0)
        return

    if M == 1:
        print(1)
        return

    if M == 2:
        print(2)
        return

    d = []
    for i in range(M-1):
        d.append(A[i+1] - A[i] - 1)

    d.sort(reverse=True)
    k = 1
    for i in range(M-2):
        k = max(k, d[i] + 1)
    print((k + 1) // 2)

main()

=======
Suggestion 8

def read_input():
    N, M = map(int, input().split())
    A = set(map(int, input().split()))
    return N, M, A

=======
Suggestion 9

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A.append(N+1)
    A.insert(0,0)
    B = []
    for i in range(1,M+2):
        if A[i]-A[i-1]-1 > 0:
            B.append(A[i]-A[i-1]-1)
    if len(B) == 0:
        print(0)
    else:
        K = min(B)
        for i in range(len(B)):
            if B[i] % K != 0:
                K = max(K,B[i]//2)
                break
        for i in range(len(B)):
            if B[i] % K != 0:
                K = B[i]
                break
        ans = 0
        for i in range(len(B)):
            ans += (B[i]-1)//K + 1
        print(ans)

=======
Suggestion 10

def get_num_of_stamps(num_of_squares, num_of_blue_squares, blue_squares):
    if num_of_blue_squares == 0:
        return 1
    if num_of_squares == num_of_blue_squares:
        return 0
    blue_squares.sort()
    max_distance = 0
    for i in range(num_of_blue_squares - 1):
        max_distance = max(max_distance, blue_squares[i + 1] - blue_squares[i])
    return (max_distance + 1) // 2 + 1

N, M = map(int, input().split())
A = list(map(int, input().split()))
print(get_num_of_stamps(N, M, A))
