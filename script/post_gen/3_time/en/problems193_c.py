Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    print(N - len(set([a**b for a in range(2, int(N**0.5)+1) for b in range(2, int(N**0.5)+1)])))

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(2, int(N ** 0.5) + 1):
        j = 2
        while i ** j <= N:
            ans += 1
            j += 1
    print(N - ans)

main()

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(2, N+1):
        for j in range(2, N+1):
            if i**j > N:
                break
            ans += 1
    print(N - ans)
    return

main()

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(2, int(N**0.5)+1):
        for j in range(2, int(N**0.5)+1):
            if i**j <= N:
                ans += 1
            else:
                break
    print(N-ans)

=======
Suggestion 5

def main():
    N = int(input())
    print(N - 1 - int(N ** 0.5) - int(N ** 0.25) + int(N ** 0.5 * 0.5))

=======
Suggestion 6

def get_primes(n):
    # Sieve of Eratosthenes
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * 2, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]

=======
Suggestion 7

def main():
    N = int(input())
    k = int(N ** 0.5)
    ans = N - k - 1
    for i in range(2, k + 1):
        j = 2
        while i ** j <= N:
            ans -= 1
            j += 1
    print(ans)

=======
Suggestion 8

def read_int():
    return int(input())
