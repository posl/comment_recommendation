Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [set(map(int, input().split()[1:])) for _ in range(N)]
    print(len(set.intersection(*A)))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, M + 1):
        if all(i in a for a in A):
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, M + 1):
        if all(i in A[j][1:] for j in range(N)):
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    foods = [0] * M
    for _ in range(N):
        for food in map(int, input().split()[1:]):
            foods[food - 1] += 1
    print(foods.count(N))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    food = [0] * M
    for i in range(N):
        A = list(map(int, input().split()))
        for j in range(A[0]):
            food[A[j+1]-1] += 1
    count = 0
    for i in range(M):
        if food[i] == N:
            count += 1
    print(count)

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    foods = [0] * M
    for i in range(N):
        K, *A = map(int, input().split())
        for a in A:
            foods[a - 1] += 1
    print(sum([1 for f in foods if f == N]))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(M):
        if all(i + 1 in a for a in A):
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    ans = 0
    for _ in range(n):
        k, *a = map(int, input().split())
        ans |= 1 << (k - 1)
    print(bin(ans).count("1"))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    foods = [0]*M
    for _ in range(N):
        foods += list(map(int, input().split()[1:]))
    print(foods.count(N))
