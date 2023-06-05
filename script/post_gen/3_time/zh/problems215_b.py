Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_max_k(n):
    k = 0
    while 2**k <= n:
        k += 1
    return k - 1

=======
Suggestion 2

def main():
    n = int(input())
    k = 0
    while 2**k <= n:
        k += 1
    print(k-1)

=======
Suggestion 3

def main():
    N = int(input())
    k = 0
    while True:
        if 2**k > N:
            break
        k += 1
    print(k-1)

=======
Suggestion 4

def main():
    n = int(input())
    k = 0
    while (2 ** k) <= n:
        k += 1
    print(k - 1)

=======
Suggestion 5

def main():
    N = int(input())
    k = 0
    while 2**k <= N:
        k += 1
    print(k-1)
main()

=======
Suggestion 6

def main():
    n = int(input())
    print(int(math.log2(n)))

=======
Suggestion 7

def find_max_k(n):
    k = 0
    while 2 ** k <= n:
        k += 1
    return k - 1

=======
Suggestion 8

def solve(n):
    k = 0
    while 2 ** k <= n:
        k += 1
    return k - 1

print(solve(int(input())))
