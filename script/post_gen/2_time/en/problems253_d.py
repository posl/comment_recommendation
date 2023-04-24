Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    print(N*(N+1)//2 - A*(N//A)*(N//A+1)//2 - B*(N//B)*(N//B+1)//2 + A*B*(N//(A*B))*(N//(A*B)+1)//2)

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    print(N * (N + 1) // 2 - A * (N // A) * (N // A + 1) // 2 - B * (N // B) * (N // B + 1) // 2 + A * B * (N // A // B) * (N // A // B + 1) // 2)

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    print(N * (N + 1) // 2 - A * (N // A) * (N // A + 1) // 2 - B * (N // B) * (N // B + 1) // 2 + A * B * (N // (A * B)) * (N // (A * B) + 1) // 2)

main()

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    print((N // A) * (A * (A + 1) // 2) + (N // B) * (B * (B + 1) // 2) - (N // (A * B)) * ((A * B) * ((A * B) + 1) // 2))

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    sum = 0
    for i in range(1, N+1):
        if i % A != 0 and i % B != 0:
            sum += i
    print(sum)

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    print(sum(range(1, N + 1)) - sum(range(A, N + 1, A)) - sum(range(B, N + 1, B)) + sum(range(A * B, N + 1, A * B)))

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    sum = 0
    for i in range(1, N+1):
        if (i % A != 0) and (i % B != 0):
            sum += i
    print(sum)

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    x = N // A
    y = N // B
    z = N // (A * B)
    print(N * (x + y) - A * (x * (x + 1) // 2) - B * (y * (y + 1) // 2) + A * B * (z * (z + 1) // 2))

=======
Suggestion 9

def main():
    N, A, B = map(int, input().split())
    lcm = A*B//math.gcd(A,B)
    ans = N//A + N//B - N//lcm
    print(ans)
