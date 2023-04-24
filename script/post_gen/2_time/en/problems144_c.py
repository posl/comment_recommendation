Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    i = 1
    while i * i < N:
        i += 1
    if i * i == N:
        print(2 * i - 2)
    else:
        if i * (i - 1) >= N:
            print(2 * i - 3)
        else:
            print(2 * i - 2)

=======
Suggestion 2

def main():
    N = int(input())
    i = 1
    while i * i < N:
        i += 1
    if i * i == N:
        print(2 * i - 2)
    elif N <= i * (i - 1) + 1:
        print(2 * i - 3)
    else:
        print(2 * i - 2)

main()

=======
Suggestion 3

def main():
    N = int(input())
    ans = N-1
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            ans = min(ans, N//i + i - 2)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    while N > 1:
        if N % 2 == 0:
            N = N // 2
            ans += 1
        else:
            N -= 1
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    if n == 2:
        print(2)
        return
    for i in range(1, n):
        if i * (i + 1) >= n:
            print(i + n // i - 2)
            return

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if N % i == 0:
            ans = i + (N // i) - 2
            break
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if i * i > N:
            break
        ans = i
    print(N - ans + ans - 1)

=======
Suggestion 8

def main():
    N = int(input())
    i = 1
    while i*(i+1) <= 2*N:
        i += 1
    print(2*N-i*(i-1))

=======
Suggestion 9

def main():
    N = int(input())
    # N = 10000000019
    # N = 10
    # N = 50
    # N = 10000000019
    # N = 10
    # N = 50
    # N = 10000000019
    # N = 10
    # N = 50

    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14
    # 2 4 6 8 10 12 14 16 18 20 22 24 26 28
    # 3 6 9 12 15 18 21 24 27 30 33 36 39 42
    # 4 8 12 16 20 24 28 32 36 40 44 48 52 56
    # 5 10 15 20 25 30 35 40 45 50 55 60 65 70
    # 6 12 18 24 30 36 42 48 54 60 66 72 78 84
    # 7 14 21 28 35 42 49 56 63 70 77 84 91 98
    # 8 16 24 32 40 48 56 64 72 80 88 96 104 112
    # 9 18 27 36 45 54 63 72 81 90 99 108 117 126
    # 10 20 30 40 50 60 70 80 90 100 110 120 130 140
    # 11 22 33 44 55 66 77 88 99 110 121 132 143 154
    # 12 24 36 48 60 72 84 96 108 120 132 144 156 168
    # 13 26 39 52 65 78 91 104 117 130 143 156 169 182
    # 14 28 42 56 70 84 98

=======
Suggestion 10

def main():
    N = int(input())
    print(N - 1)
