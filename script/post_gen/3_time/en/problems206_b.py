Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    sum = 0
    for i in range(1, N+1):
        sum += i
        if sum >= N:
            print(i)
            break

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i
        if ans >= N:
            print(i)
            break

=======
Suggestion 3

def main():
    N = int(input())
    i = 1
    while N > 0:
        N -= i
        i += 1
    print(i-1)

=======
Suggestion 4

def main():
    n = int(input())
    if n == 1:
        print(1)
    else:
        i = 1
        while True:
            if n <= (i*(i+1)/2):
                print(i)
                break
            else:
                i += 1

=======
Suggestion 5

def main():
    n = int(input())
    print(int((2 * n) ** 0.5))

=======
Suggestion 6

def main():
    N = int(input())
    if N <= 0:
        print(0)
    else:
        print(int((2*N)**0.5))

=======
Suggestion 7

def main():
    N = int(input())
    print(int((N*2)**0.5))

=======
Suggestion 8

def main():
    N = int(input())
    print(int(N * (N+1) / 2))

=======
Suggestion 9

def getN():
    return int(input())
