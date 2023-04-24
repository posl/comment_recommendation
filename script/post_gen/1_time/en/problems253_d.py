Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    print(N*(N+1)//2 - A*(N//A)*(N//A+1)//2 - B*(N//B)*(N//B+1)//2 + A*B*(N//(A*B))*(N//(A*B)+1)//2)

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    print((N // A) * (A * (A - 1) // 2) + (N // B) * (B * (B - 1) // 2) - (N // (A * B)) * (A * B * (A * B - 1) // 2))

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    print(sum(range(1, N + 1)) - A * ((N // A) * ((N // A) + 1) // 2) - B * ((N // B) * ((N // B) + 1) // 2) + A * B * ((N // (A * B)) * ((N // (A * B)) + 1) // 2))

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    print(N*(N+1)//2 - (N//A+A*(N//A-1)*N//2//A) - (N//B+B*(N//B-1)*N//2//B) + (N//A//B+A*B*(N//A//B-1)*N//2//(A*B)))

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    ans = 0
    ans += N // A * (A + 1) * A // 2
    ans += N // B * (B + 1) * B // 2
    ans -= N // (A * B) * (A * B + 1) * (A * B) // 2
    print(ans)

=======
Suggestion 7

def solve(n, a, b):
    if a > b:
        a, b = b, a
    if b % a == 0:
        return (n // a) * (a + b)
    else:
        return (n // a) * (a + b) + (n // b) * b - (n // (a * b)) * b

n, a, b = map(int, input().split())
print(solve(n, a, b))

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    #print(N, A, B)
    S = 0
    for i in range(1, N+1):
        if i%A==0 or i%B==0:
            continue
        else:
            S += i
    print(S)

=======
Suggestion 9

def get_sum(n, a, b):
    # count the number of integers that are multiples of a or b
    cnt = n // a + n // b - n // lcm(a, b)
    # count the sum of integers that are multiples of a or b
    sum = (1 + n) * n // 2 - ((a + a * (cnt - 1)) * cnt // 2 + (b + b * (cnt - 1)) * cnt // 2 - (lcm(a, b) + lcm(a, b) * (cnt - 1)) * cnt // 2)
    return sum
