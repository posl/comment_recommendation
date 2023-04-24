Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [set(map(int, input().split()[1:])) for _ in range(N)]
    print(len(set.intersection(*A)))

main()

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    foods = [0] * M
    for i in range(N):
        K, *A = map(int, input().split())
        for a in A:
            foods[a - 1] += 1
    print(sum([1 for f in foods if f == N]))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    foods = [0] * M
    for _ in range(N):
        for food in map(int, input().split()[1:]):
            foods[food - 1] += 1
    print(len([food for food in foods if food == N]))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [set(map(int, input().split()[1:])) for _ in range(N)]
    print(sum(all(i in a for a in A) for i in range(1, M+1)))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    ans = 0
    for i in range(N):
        K, *A = map(int, input().split())
        if i == 0:
            ans = set(A)
        else:
            ans = ans & set(A)
    print(len(ans))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    foods = [set() for _ in range(N)]
    for i in range(N):
        K, *A = map(int, input().split())
        foods[i] = set(A)
    ans = 0
    for i in range(1, M+1):
        if all(i in food for food in foods):
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    ans = 0
    for i in range(n):
        k, *a = map(int, input().split())
        for j in range(m):
            if j + 1 in a:
                ans += 1
                break
    print(m - ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    foods = set()
    for _ in range(N):
        foods = foods | set(map(int, input().split()[1:]))
    print(len(foods))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(set(map(int, input().split()[1:])))
    print(sum(1 for i in range(1, M + 1) if all(i in a for a in A)))
