Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(n):
        a, b = map(int, input().split())
        ans += (b - a + 1) * (a + b) // 2
    print(ans % (10 ** 9 + 7))

=======
Suggestion 2

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        A, B = map(int, input().split())
        sum += (B - A + 1) * (A + B) // 2
    print(sum % (10 ** 9 + 7))

=======
Suggestion 3

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        A, B = map(int, input().split())
        sum += (B - A + 1) * (A + B) // 2
    print(sum % 1000000007)

=======
Suggestion 4

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
        ans %= 998244353

    print(ans)

=======
Suggestion 5

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
        ans += (B[i] - A[i] + 1) * (A[i] + B[i]) // 2

    print(ans % (10 ** 9 + 7))

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(N):
        a, b = map(int, input().split())
        ans += (b - a + 1) * (a + b) // 2

    print(ans % (10**9 + 7))

=======
Suggestion 7

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    print(sum((B[i]-A[i]+1)*(A[i]+B[i])//2 for i in range(N))%(10**9+7))

=======
Suggestion 8

def main():
    N = int(input())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        ans += ((B[i]-A[i]+1)*(A[i]+B[i]))//2
    print(ans%1000000007)

=======
Suggestion 9

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        ans += (AB[i][1] - AB[i][0] + 1) * (AB[i][0] + AB[i][1]) // 2
        ans %= 998244353
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    ans = 0
    for i in range(N):
        a, b = map(int, input().split())
        ans += (b-a+1)*(a+b)/2
    print(int(ans%1000000007))
