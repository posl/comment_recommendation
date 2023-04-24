Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n % 111 == 0:
        print(n)
    else:
        print((n // 111 + 1) * 111)

main()

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
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        print((N // 111 + 1) * 111)

=======
Suggestion 4

def main():
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        print(((N // 111) + 1) * 111)

=======
Suggestion 5

def main():
    n = int(input())
    n = str(n)
    if n[0] == n[1] and n[1] == n[2]:
        print(n)
    else:
        if n[0] == n[1]:
            if n[0] < n[2]:
                print(n[0] + n[1] + n[1])
            else:
                print(n[0] + n[0] + n[0])
        elif n[0] == n[2]:
            if n[0] < n[1]:
                print(n[0] + n[1] + n[0])
            else:
                print(n[0] + n[0] + n[0])
        else:
            if n[1] < n[2]:
                print(n[0] + n[1] + n[1])
            else:
                print(n[0] + n[0] + n[0])

=======
Suggestion 6

def main():
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        N = 111 * (int(N / 111) + 1)
        print(N)

=======
Suggestion 7

def main():
    #input
    n = int(input())
    #compute
    if n % 111 == 0:
        ans = n
    else:
        ans = int((n / 111 + 1) * 111)
    #output
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    print((n+111)//111*111)

main()

=======
Suggestion 9

def main():
    n = int(input())
    print((n+111)//111*111)
