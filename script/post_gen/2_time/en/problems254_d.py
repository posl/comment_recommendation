Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i * j > N:
                break
            else:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i * j <= n and i * j == int(i * j) ** 2:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i * j <= N and i * j == int((i * j)**0.5)**2:
                count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i * j <= N and i * j == round(i * j ** 0.5) ** 2:
                count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i*j <= N and i == j:
                ans += 1
            elif i*j <= N and i != j:
                ans += 2
            else:
                break
    print(ans)
main()

=======
Suggestion 6

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i*j <= N:
                if i == j:
                    count += 1
                elif i*j == i*i or i*j == j*j:
                    count += 2
    print(count)

=======
Suggestion 7

def main():
    import math
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i*j <= N:
                if math.sqrt(i*j).is_integer():
                    ans += 1
            else:
                break
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i*j == int(i**0.5)**2 * int(j**0.5)**2:
                if i == j:
                    count += 1
                else:
                    count += 2
    print(count)

=======
Suggestion 9

def solve(n):
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i*j <= n and i*j == int(i**0.5)**2 * int(j**0.5)**2:
                count += 1
    return count

=======
Suggestion 10

def main():
    N = int(input())
    print(int(N**0.5)**2)
