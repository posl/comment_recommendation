Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = v[0]
    for i in range(1, n):
        ans = (ans + v[i]) / 2
    print(ans)

main()

=======
Suggestion 2

def main():
    N = int(input())
    V = list(map(int, input().split()))
    V.sort()
    ans = V[0]
    for i in range(1, N):
        ans = (ans + V[i]) / 2
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    v = list(map(int, input().split()))

    v.sort()
    ans = v[0]
    for i in range(1, N):
        ans = (ans + v[i]) / 2
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(N-1):
        v[i+1] = (v[i] + v[i+1]) / 2
    print(v[N-1])

=======
Suggestion 5

def solve():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = v[0]
    for i in range(1, n):
        ans = (ans + v[i])/2
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    v = list(map(int,input().split()))
    v.sort()
    ans = v[0]
    for i in range(1,N):
        ans = (ans + v[i]) / 2
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()

    for i in range(N-1):
        v[i+1] = (v[i]+v[i+1])/2

    print(v[-1])

=======
Suggestion 8

def main():
    n = int(input())
    v = sorted(list(map(int, input().split())))
    for i in range(n-1):
        v[i+1] = (v[i] + v[i+1]) / 2
    print(v[-1])

=======
Suggestion 9

def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

n = int(input())

=======
Suggestion 10

def get_max_value(n, v):
    v.sort()
    result = v[0]
    for i in range(1, n):
        result = (result + v[i]) / 2
    return result

n = int(input())
v = list(map(int, input().split()))
print(get_max_value(n, v))
