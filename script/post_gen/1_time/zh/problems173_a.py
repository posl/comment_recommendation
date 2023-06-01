Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n % 1000 == 0:
        print(0)
    else:
        print(1000 - n % 1000)

=======
Suggestion 2

def solution():
    N = int(input())
    print(1000 - N % 1000)

=======
Suggestion 3

def main():
    n = int(input())
    print(1000 - n % 1000)

=======
Suggestion 4

def main():
    N = int(input())
    print(1000 - N % 1000)

=======
Suggestion 5

def main():
    n = int(input())
    print(1000 - n % 1000 if n % 1000 != 0 else 0)

=======
Suggestion 6

def change(n):
    if n <= 1000:
        return 1000-n
    else:
        return change(n-1000)

print(change(int(input())))

=======
Suggestion 7

def main():
    n = int(input())
    print(1000 - n%1000)

main()
