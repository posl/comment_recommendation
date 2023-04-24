Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    a, b, x = map(int, input().split())
    if x < a:
        print(0)
        return
    x -= a
    if x < b:
        print(0)
        return
    x -= b
    if x < b:
        print(0)
        return
    x //= b
    if x < 9:
        print(1)
        return
    x //= 9
    if x < 9:
        print(10)
        return
    x //= 9
    if x < 9:
        print(100)
        return
    x //= 9
    if x < 9:
        print(1000)
        return
    x //= 9
    if x < 9:
        print(10000)
        return
    x //= 9
    if x < 9:
        print(100000)
        return
    x //= 9
    if x < 9:
        print(1000000)
        return
    x //= 9
    if x < 9:
        print(10000000)
        return
    x //= 9
    if x < 9:
        print(100000000)
        return
    x //= 9
    if x < 9:
        print(1000000000)
        return
    x //= 9
    print(1000000000 + x)

main()

=======
Suggestion 2

def main():
    A, B, X = map(int, input().split())
    if X < A:
        print(0)
        return
    if A * 10**9 + B * 10 <= X:
        print(10**9)
        return
    N = 1
    while A * N + B * len(str(N)) <= X:
        N *= 10
    N //= 10
    while A * N + B * len(str(N)) <= X:
        N += 1
    print(N - 1)

=======
Suggestion 3

def main():
    A, B, X = map(int, input().split())
    if X >= A * 10**9 + B * 10:
        print(10**9)
        return
    if X < A + B:
        print(0)
        return
    if A > B:
        print(X // A)
        return
    if A <= B:
        print((X - B * 10) // (A - B))
        return

=======
Suggestion 4

def main():
    a, b, x = map(int, input().split())
    max_n = 10**9
    min_n = 0
    while max_n - min_n > 1:
        n = (max_n + min_n) // 2
        if a * n + b * len(str(n)) > x:
            max_n = n
        else:
            min_n = n
    print(min_n)

=======
Suggestion 5

def main():
    A, B, X = map(int, input().split())
    minN = 0
    maxN = 10**9
    while maxN - minN > 1:
        midN = (maxN + minN) // 2
        if A * midN + B * len(str(midN)) <= X:
            minN = midN
        else:
            maxN = midN
    print(minN)

=======
Suggestion 6

def main():
    A, B, X = map(int, input().split())
    N = 0
    if A * N + B * len(str(N)) <= X:
        N = X // A
        while A * N + B * len(str(N)) > X:
            N -= 1
    print(N)

main()

=======
Suggestion 7

def main():
    A, B, X = map(int, input().split())
    N = X // A
    if N > 10**9:
        N = 10**9
    while (A * N + B * len(str(N))) > X:
        N -= 1
    print(N)

=======
Suggestion 8

def count_digits(n):
    return len(str(n))

=======
Suggestion 9

def digits(x):
    return len(str(x))
