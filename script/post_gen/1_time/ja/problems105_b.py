Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    for i in range(n // 4 + 1):
        if (n - 4 * i) % 7 == 0:
            print('Yes')
            return
    print('No')

=======
Suggestion 2

def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    N = int(input())
    for i in range(0, N+1, 4):
        for j in range(0, N+1, 7):
            if i+j == N:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 4

def main():
    n = int(input())
    for i in range((n//7)+1):
        for j in range((n//4)+1):
            if 7*i + 4*j == n:
                print("Yes")
                return
    print("No")
main()

=======
Suggestion 5

def main():
    n = int(input())
    for i in range(0, n+1, 4):
        if (n - i) % 7 == 0:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 6

def main():
    n = int(input())
    for i in range(0, n//4 + 1):
        if (n - 4 * i) % 7 == 0:
            print('Yes')
            return
    print('No')

=======
Suggestion 7

def main():
    n = int(input())
    for i in range(0, n+1, 4):
        if (n-i)%7 == 0:
            print('Yes')
            return
    print('No')

=======
Suggestion 8

def main():
    N = int(input())
    for i in range(N//4+1):
        if (N - i * 4) % 7 == 0:
            print("Yes")
            return
    print("No")

=======
Suggestion 9

def main():
    N = int(input())
    for i in range(N//4+1):
        if (N - 4 * i) % 7 == 0:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 10

def main():
    n = int(input())
    for i in range(0, n//4+1):
        if (n - 4*i)%7 == 0:
            print("Yes")
            return
    print("No")
