Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n % 100 == 0:
        print(n // 100)
    else:
        print(n // 100 + 1)

=======
Suggestion 2

def main():
    n = int(input())
    print((n + 99) // 100)

=======
Suggestion 3

def main():
    N = int(input())
    if N % 100 == 0:
        print(int(N / 100))
    else:
        print(int(N / 100) + 1)

=======
Suggestion 4

def main():
    N = int(input())
    if N % 100 == 0:
        print(N // 100)
    else:
        print(N // 100 + 1)

=======
Suggestion 5

def main():
    n = int(input())
    ans = n // 100
    if n % 100 != 0:
        ans += 1
    print(ans)
