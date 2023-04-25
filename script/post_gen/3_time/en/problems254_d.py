Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(i, N+1):
            if i*j <= N:
                ans += 1
            else:
                break
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i * j > N:
                break
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    cnt = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i*j <= N:
                cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        ans += N // i
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, i+1):
            if i*j == int(i*j**0.5)**2:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    cnt = 0
    for i in range(1, int(n**0.5)+1):
        cnt += n // i - i + 1
    print(cnt)

=======
Suggestion 7

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i*j == int((i*j)**(1/2))**2:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    answer = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i * j == int(i * j ** 0.5) ** 2:
                answer += 1
    print(answer)
