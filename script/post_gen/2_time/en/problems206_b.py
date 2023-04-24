Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        sum += i
        if sum >= n:
            print(i)
            break

=======
Suggestion 2

def main():
    N = int(input())
    sum = 0
    for i in range(1,N+1):
        sum += i
        if sum >= N:
            print(i)
            break

=======
Suggestion 3

def main():
    N = int(input())
    sum = 0
    for i in range(1,N+1):
        sum += i
        if sum >= N:
            print(i)
            break

main()

=======
Suggestion 4

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        sum = sum + i + 1
        if sum >= N:
            break
    print(i+1)

=======
Suggestion 5

def main():
    N = int(input())
    print(int((1 + 8 * N) ** 0.5 - 1) // 2 + 1)

=======
Suggestion 6

def main():
    n = int(input())
    print(int((1 + 8 * n) ** 0.5 - 1) // 2 + 1)

=======
Suggestion 7

def main():
    N = int(input())
    l = 0
    r = 10**9 + 1
    while r - l > 1:
        mid = (l + r) // 2
        if mid * (mid + 1) // 2 >= N:
            r = mid
        else:
            l = mid
    print(r)

=======
Suggestion 8

def main():
    N = int(input())
    print(N*(N+1)//2-N)

=======
Suggestion 9

def main():
    n = int(input())
    print((n * (n + 1)) // 2)

=======
Suggestion 10

def main():
    N = int(input())
    print(int((N*2)**0.5))
