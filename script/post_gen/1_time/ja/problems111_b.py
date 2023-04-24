Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        print((N // 111 + 1) * 111)

=======
Suggestion 2

def main():
    n = int(input())
    if n % 111 == 0:
        print(n)
    else:
        print((n // 111 + 1) * 111)

=======
Suggestion 3

def main():
    n = input()
    if n[0] == n[1] and n[1] == n[2]:
        print(n)
    else:
        print(str(int(n[0])+1)*3)

=======
Suggestion 4

def main():
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        print(111 * (N // 111 + 1))

=======
Suggestion 5

def main():
    N = int(input())
    N = str(N)
    if N[0] == N[1] and N[1] == N[2]:
        print(N)
    else:
        if N[0] == N[1] and N[1] != N[2]:
            print(N[0]+N[1]+N[1])
        elif N[1] == N[2] and N[0] != N[1]:
            print(N[0]+N[1]+N[1])
        elif N[0] == N[2] and N[0] != N[1]:
            print(N[0]+N[1]+N[0])
        else:
            if N[0] > N[1] and N[0] > N[2]:
                print(N[0]+N[0]+N[0])
            elif N[1] > N[0] and N[1] > N[2]:
                print(N[1]+N[1]+N[1])
            elif N[2] > N[0] and N[2] > N[1]:
                print(N[2]+N[2]+N[2])
            else:
                print(N[0]+N[1]+N[2])

=======
Suggestion 6

def main():
    N = int(input())
    print((N + 111) // 111 * 111)

=======
Suggestion 7

def main():
    N = int(input())
    n = 1
    while True:
        if n > N:
            break
        n *= 10
    n //= 10
    ans = N // n * n + n - 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    print(n + 111 - n % 111)
