Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 1:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 1:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    if N < 10:
        print(N)
    elif N < 100:
        print(9)
    elif N < 1000:
        print(9 + 1)
    elif N < 10000:
        print(9 + 2)
    elif N < 100000:
        print(9 + 3)
    else:
        print(9 + 4)

=======
Suggestion 4

def main():
    n = int(input())
    if n < 10:
        print(n)
    else:
        print(9 + (n - 9) // 10)

=======
Suggestion 5

def main():
    N = int(input())
    print(9*(len(str(N))-1)+N//(10**(len(str(N))-1)))

main()

=======
Suggestion 6

def main():
    N = int(input())
    print(N - 9 * len(str(N)) + 1)

=======
Suggestion 7

def main():
    N = int(input())
    print(N - 9 * len(str(N)))

=======
Suggestion 8

def main():
    N = int(input())
    print(N - int((N + 1) / 10))
