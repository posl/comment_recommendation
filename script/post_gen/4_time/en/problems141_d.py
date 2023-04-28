Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] // 2 ** min(m, i)
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] // 2**m
        if a[i] % 2**m != 0:
            m -= 1
        if m == -1:
            break
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    ans = 0
    for i in range(N):
        if M == 0:
            ans += A[i]
            continue
        if A[i] <= 2**M:
            ans += A[i]
        else:
            ans += A[i]//(2**M)
            M = 0
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for a in A:
        ans += a
        if ans % (2 ** M) == 0:
            ans //= 2 ** M
            M -= 1
        else:
            ans //= 2 ** (M - 1)
            M -= 2
    print(ans)
main()

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    tickets = [0] * 40
    for i in range(M):
        tickets[int(input())] += 1
    for i in range(39):
        tickets[i+1] += tickets[i] // 2
    ans = 0
    for i in range(N):
        ans += A[i] // (2 ** tickets[i])
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] < 2**m:
            ans += a[i]
        else:
            ans += a[i] // 2**m
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    tickets = [0] * (m + 1)
    for i in range(n):
        tickets[0] += a[i]
        for j in range(m):
            if tickets[j] < tickets[j + 1]:
                tickets[j + 1] = tickets[j]
            tickets[j] //= 2
    print(tickets[m])

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = sum(A)
    for i in range(N - 1):
        if A[i] >= M:
            break
        A[i + 1] = min(A[i + 1], A[i] * 2)
    print(ans - sum(A))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        a = A[i]
        if a <= 2 ** M:
            A[i] = 0
            M -= 1
        else:
            A[i] = a % (2 ** M)
    print(sum(A))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Aの最大値を求める
    max_A = max(A)
    
    # 2進数表記で1の数のリストを作成
    # 1の数が多い順に並べる
    # 2^0, 2^1, 2^2, ... となる
    # 1の数が多い順に並べることで、
    # 2^iの値の大きい順に並べることができる
    # 例えば、
    # 1の数が多い順に並べると、
    # 2^0, 2^1, 2^2, 2^3, 2^4, 2^5, 2^6, 2^7, 2^8, 2^9, 2^10, ...
    # となり、
    # 2^iの値の大きい順に並べることができる
    # 例えば、
    # 2^0, 2^2, 2^3, 2^1, 2^4, 2^5, 2^6, 2^7, 2^8, 2^9, 2^10, ...
    # となり、
    # 2^iの値の大きい順に並べることができる
    # 例えば、
    # 2^0, 2^2, 2^3, 2^1, 2^4, 2^5, 2^6, 2^7, 2^8, 2^9, 2^10, ...
    # となり、
    # 2^iの値の大きい順に並べることができる
    # 例えば、
    # 2^0,
