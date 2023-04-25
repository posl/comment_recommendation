Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    cnt = 0
    for i in range(1,N+1):
        if len(str(i)) % 2 == 1:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if len(str(i))%2 == 1:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    if n < 10:
        print(n)
    else:
        print(9 + (n - 9) // 10)

=======
Suggestion 4

def main():
    N = int(input())
    print(sum(1 for i in range(1,N+1) if len(str(i))%2 == 1))

=======
Suggestion 5

def main():
    N = int(input())
    print(N - 9 * (len(str(N)) - 1))

=======
Suggestion 6

def main():
    N = int(input())
    print((N + 1) // 2)

=======
Suggestion 7

def count_odd_digits(n):
    if n > 9:
        return 10 ** (len(str(n)) - 1) // 2 + count_odd_digits(n % (10 ** (len(str(n)) - 1)))
    else:
        return 1

=======
Suggestion 8

def odd_digits(N):
    return N - (N // 10)

N = int(input())
print(odd_digits(N))

=======
Suggestion 9

def main():
    N = int(input())
    print(int(N/10) + 1)
