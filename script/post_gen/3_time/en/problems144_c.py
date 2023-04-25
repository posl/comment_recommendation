Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    N = int(input())
    i = 1
    while i * (i + 1) <= 2 * N:
        i += 1
    if i * (i - 1) // 2 == N:
        print(2 * i - 3)
    else:
        print(2 * i - 2)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if N % i == 0:
            ans = i + N // i - 2
            break
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if N % i == 0:
            ans = i
    print(N + ans - 2)

=======
Suggestion 5

def main():
    N = int(input())
    if N == 2:
        print(1)
        return
    for i in range(1, N):
        if i * i > N:
            print(i * 2 - 2)
            return
        if i * (i+1) > N:
            print(i * 2 - 1)
            return

=======
Suggestion 6

def main():
    N = int(input())
    i = 1
    while i*(i+1) <= N:
        i += 1
    print(i-1+N//i)

=======
Suggestion 7

def main():
    N = int(input())
    for i in range(1, 10**6):
        if i*(i+1) >= 2*N:
            print(i + (N - i*(i-1)//2 - 1)//i)
            break

=======
Suggestion 8

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
    #N = 1000000000000000000
    #

=======
Suggestion 9

def main():
    N = int(input())
    #print(N)
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            j = N//i
            #print(j, i)
    print(j+i-2)

=======
Suggestion 10

def main():
    N = int(input())
    # N = 10
    # N = 50
    # N = 10000000019
    # print(N)
    # N = 1000000000000000000
    # print(N)
    # N = 10000000000000000000
    # print(N)
    # N = 100000000000000000000
    # print(N)
    # N = 1000000000000000000000
    # print(N)
    # N = 10000000000000000000000
    # print(N)
    # N = 100000000000000000000000
    # print(N)
    # N = 1000000000000000000000000
    # print(N)
    # N = 10000000000000000000000000
    # print(N)
    # N = 100000000000000000000000000
    # print(N)
    # N = 1000000000000000000000000000
    # print(N)
    # N = 10000000000000000000000000000
    # print(N)
    # N = 100000000000000000000000000000
    # print(N)
    # N = 1000000000000000000000000000000
    # print(N)
    # N = 10000000000000000000000000000000
    # print(N)
    #
