Synthesizing 9/10 solutions

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
        if N % i == 0:
            print(2 * i - 2)
        else:
            print(2 * i - 1)

=======
Suggestion 2

def main():
    N = int(input())
    i = 1
    while i * i < N:
        i += 1
    if i * i == N:
        print(i + i - 2)
    else:
        if N % i == 0:
            print(i + i - 1)
        else:
            print(i + i - 2)

=======
Suggestion 3

def main():
    N = int(input())
    ans = N-1
    for i in range(1, N):
        if N % i == 0:
            ans = min(ans, i+N//i-2)
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    x = 1
    y = 1
    for i in range(N-1):
        if x < y:
            x += 1
        else:
            y += 1
    print(x+y-2)
    return

=======
Suggestion 5

def main():
    n = int(input())
    ans = 0
    if n == 2:
        ans = 1
    else:
        i = 1
        while i*i <= n:
            if n % i == 0:
                ans = i + n//i - 2
            i += 1
    print(ans)

main()

=======
Suggestion 6

def main():
    N = int(input())
    #N = 10000000019
    #N = 50
    #N = 10
    #N = 1
    #N = 2
    #N = 3
    #N = 4
    #N = 5
    #N = 6
    #N = 7
    #N = 8
    #N = 9
    #N = 10
    #N = 11
    #N = 12
    #N = 13
    #N = 14
    #N = 15
    #N = 16
    #N = 17
    #N = 18
    #N = 19
    #N = 20
    #N = 21
    #N = 22
    #N = 23
    #N = 24
    #N = 25
    #N = 26
    #N = 27
    #N = 28
    #N = 29
    #N = 30
    #N = 31
    #N = 32
    #N = 33
    #N = 34
    #N = 35
    #N = 36
    #N = 37
    #N = 38
    #N = 39
    #N = 40
    #N = 41
    #N = 42
    #N = 43
    #N = 44
    #N = 45
    #N = 46
    #N = 47
    #N = 48
    #N = 49
    #N = 50

    # 1. Find the largest number that is a multiple of N
    # 2. Find the largest number that is a multiple of N
    # 3. Find the largest number that is a multiple of N
    # 4. Find the largest number that is a multiple of N
    # 5. Find the largest number that is a multiple of N
    # 6. Find the largest number that is a multiple of N
    # 7. Find the largest number that is a multiple of N
    # 8. Find

=======
Suggestion 7

def main():
    N = int(input())
    for i in range(1, N+1):
        if N <= i*(i+1):
            print(i-1 + N - i*(i+1))
            break

=======
Suggestion 8

def main():
    # read input
    N = int(input())
    # find the minimum number of moves
    if N % 2 == 0:
        print(N//2 - 1)
    else:
        print(N//2)

=======
Suggestion 9

def   main ( N ): 
    #N = int(input())
    max = 0
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            max = i
    print(N // max + max - 2)
