Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    i = 1
    while i * i <= N:
        if N % i == 0:
            print(i)
            if i != N // i:
                print(N // i)
        i += 1

=======
Suggestion 2

def solve(n):
    ans = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n // i)
        i += 1
    ans.sort()
    return ans

=======
Suggestion 3

def problem180_c():
    pass

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    n = int(input())
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i)
            if i != n // i:
                print(n // i)
        i += 1

=======
Suggestion 6

def main():
    n = int(input())
    i = 1
    while i*i <= n:
        if n % i == 0:
            print(i)
            if i*i != n:
                print(n // i)
        i += 1
main()
