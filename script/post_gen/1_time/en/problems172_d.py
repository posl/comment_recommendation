Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        ans += i * (N // i) * (N // i + 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    f = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            f[j] += 1
    ans = 0
    for i in range(1, N + 1):
        ans += i * f[i]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i * (N//i) * (N//i + 1) // 2
    print(ans)

main()

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for k in range(1, N+1):
        ans += k * (N//k) * ((N//k)+1) // 2
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        ans += i * (n//i) * ((n//i)+1) // 2
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        ans += i * (N//i) * ((N//i)+1) // 2
    print(ans)

=======
Suggestion 7

def solve(n):
    ans = 0
    for i in range(1, n+1):
        ans += i * (n//i) * (n//i+1) // 2
    return ans
