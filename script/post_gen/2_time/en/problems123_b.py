Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(10 * ((A + 9) // 10 + (B + 9) // 10 + (C + 9) // 10 + (D + 9) // 10 + (E + 9) // 10 - 5))

=======
Suggestion 2

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print((max(A, B, C, D, E) + 9) // 10 * 10)

=======
Suggestion 3

def main():
    A, B, C, D, E = map(int, input().split())
    print((A + 9) // 10 * 10 + (B + 9) // 10 * 10 + (C + 9) // 10 * 10 + (D + 9) // 10 * 10 + E)

=======
Suggestion 4

def main():
    A, B, C, D, E = (int(input()) for _ in range(5))
    print(10 * ((A + 9) // 10 + (B + 9) // 10 + (C + 9) // 10 + (D + 9) // 10 + (E + 9) // 10 - 4) + max(A % 10, B % 10, C % 10, D % 10, E % 10))

=======
Suggestion 5

def main():
    A, B, C, D, E = map(int, open(0).read().split())
    print(10 * ((A + 9) // 10 + (B + 9) // 10 + (C + 9) // 10 + (D + 9) // 10 + (E + 9) // 10) - max(A % 10, B % 10, C % 10, D % 10, E % 10))

=======
Suggestion 6

def main():
    A, B, C, D, E = map(int, [input() for _ in range(5)])
    print(10 * ((A + 9) // 10 + (B + 9) // 10 + (C + 9) // 10 + (D + 9) // 10 + (E + 9) // 10 - 5) + max(A % 10, B % 10, C % 10, D % 10, E % 10))

=======
Suggestion 7

def solve():
    A, B, C, D, E = map(int, input().split())
    print(10 * ((A + 9) // 10 + (B + 9) // 10 + (C + 9) // 10 + (D + 9) // 10 + (E + 9) // 10 - 5))

=======
Suggestion 8

def main():
    # input
    A, B, C, D, E = map(int, input().split())

    # compute
    ans = 0
    ans += A
    ans += B
    ans += C
    ans += D
    ans += E
    ans += 9

    # output
    print(ans)

=======
Suggestion 9

def main():
    A, B, C, D, E = map(int, input().split())
    print((A+B+C+D+E-1)//5+9)
