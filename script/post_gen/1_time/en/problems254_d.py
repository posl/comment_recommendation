Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1, int(n ** 0.5) + 1):
        ans += n // i - i + 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i * j <= N:
                ans += 1
            else:
                break
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(i, N+1):
            if i * j > N:
                break
            if i == j:
                ans += 1
            else:
                ans += 2
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    count = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i * j == int(i * j ** 0.5) ** 2:
                count += 1
    print(count)

main()

=======
Suggestion 5

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        ans += n // i
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        ans += (n//i)**2
    print(ans)
main()

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += N // i
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, i+1):
            if i*j > N:
                break
            if i == j:
                ans += 1
            else:
                ans += 2
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        cnt += N//i
    print(cnt)
