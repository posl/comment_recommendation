Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        ans += (A[i] + B[i]) * (B[i] - A[i] + 1) // 2
    print(ans % 1000000007)

=======
Suggestion 2

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        ans += (B[i] - A[i] + 1) * (B[i] + A[i]) // 2
    print(ans % 998244353)

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    ans = 0
    for i in range(n):
        ans += (b[i] - a[i] + 1) * (a[i] + b[i]) // 2
    print(ans % 998244353)

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        ans += (B[i]-A[i]+1)*(A[i]+B[i])//2
    print(ans%998244353)

=======
Suggestion 5

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    sum = 0
    for i in range(N):
        sum += (B[i] - A[i] + 1) * (A[i] + B[i]) // 2

    print(sum % 1000000007)

=======
Suggestion 6

def main():
    N = int(input())
    total = 0
    for i in range(N):
        A, B = map(int, input().split())
        total += (B - A + 1) * (A + B) // 2
    print(total % 1000000007)

main()

=======
Suggestion 7

def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    s = 0
    for i in range(n):
        s += (b[i] - a[i] + 1) * (b[i] + a[i]) // 2
    print(s % 1000000007)
    return

=======
Suggestion 8

def main():
    N = int(input())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    print(sum(B)-sum(A)+N)

=======
Suggestion 9

def main():
    n = int(input())
    ab = [0] * n
    for i in range(n):
        ab[i] = list(map(int, input().split()))
    ab.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n - 1):
        if ab[i][1] >= ab[i + 1][0]:
            ab[i + 1][0] = ab[i][0]
            ab[i + 1][1] = max(ab[i][1], ab[i + 1][1])
        else:
            ans += ab[i][1] - ab[i][0] + 1
    ans += ab[n - 1][1] - ab[n - 1][0] + 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for a, b in AB:
        ans += (b-a+1)*(a+b)//2
    print(ans%998244353)
