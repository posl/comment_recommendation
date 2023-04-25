Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    if N % (2 * D + 1) == 0:
        print(N // (2 * D + 1))
    else:
        print(N // (2 * D + 1) + 1)

=======
Suggestion 2

def solve():
    N, D = map(int, input().split())
    ans = N // (D * 2 + 1)
    if N % (D * 2 + 1) != 0:
        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    print((N + D * 2) // (D * 2 + 1))

=======
Suggestion 5

def main():
    N, D = map(int, input().split())
    print((N - 1) // (2*D + 1) + 1)

=======
Suggestion 6

def main():
  n, d = map(int, input().split())
  print((n+2*d-1)//(2*d+1))

=======
Suggestion 7

def get_min_inspectors(N, D):
    # Write your code here
    return 0

=======
Suggestion 8

def main():
    # Write code here
    pass
