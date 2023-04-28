Synthesizing 10/10 solutions

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
    total = 0
    for i in range(1, N):
        total += i
        if total >= N:
            print(i)
            break

main()

=======
Suggestion 3

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        cnt += i
        if cnt >= N:
            print(i)
            break

=======
Suggestion 4

def main():
    N = int(input())
    #print(N)
    sum = 0
    for i in range(1, N+1):
        sum = sum + i
        if sum >= N:
            print(i)
            break

main()

=======
Suggestion 5

def main():
    N = int(input())
    print(int(((1+8*N)**0.5-1)/2))

=======
Suggestion 6

def main():
    N = int(input())
    print(N*(N+1)//2-N)

=======
Suggestion 7

def main():
    n = int(input())
    print(int((n * 2) ** 0.5))

=======
Suggestion 8

def main():
    N = int(input())
    print(int((2*N)**0.5))

=======
Suggestion 9

def main():
    N = int(input())
    print((N * 2) ** 0.5)

=======
Suggestion 10

def main():
    N = int(input())
    print((N**0.5-1)*2+1)
