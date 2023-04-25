Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    print((B + A - 3) // (A - 1))

main()

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print((B + A - 3) // (A - 1))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print((b + a - 3) // (a - 1))

=======
Suggestion 4

def main():
    A, B = input().split()
    A = int(A)
    B = int(B)
    if B % A == 0:
        print(int(B/A))
    else:
        print(int(B/A)+1)

=======
Suggestion 5

def solve():
    A, B = map(int, input().split())
    ans = 0
    while B > 1:
        B -= A - 1
        ans += 1
    print(ans)

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    print((B + A - 1) // A)

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    if B <= A:
        print(1)
    else:
        print((B - 1) // (A - 1))

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    print(B // A + (1 if B % A != 0 else 0))

main()

=======
Suggestion 9

def main():
    A, B = map(int, input().split())
    print((B-1) // (A-1))

=======
Suggestion 10

def main():
    A, B = map(int, input().split())
    if B < A:
        print(1)
    else:
        print((B + A - 1) // A)
