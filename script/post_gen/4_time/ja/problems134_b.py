Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, d = map(int, input().split())
    print((n + 2 * d) // (2 * d + 1))

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    print(N//(2*D+1) if N%(2*D+1)==0 else N//(2*D+1)+1)

=======
Suggestion 4

def main():
    n, d = map(int, input().split())
    print((n + (d * 2)) // ((d * 2) + 1))

=======
Suggestion 5

def main():
    N, D = map(int, input().split())
    print(N // (2 * D + 1) + min(1, N % (2 * D + 1)))

=======
Suggestion 6

def main():
    n, d = map(int, input().split())
    print(1 + (n - 1) // (d * 2 + 1))

=======
Suggestion 7

def main():
    N, D = map(int, input().split())
    print(int((N + (2 * D)) / ((2 * D) + 1)))

=======
Suggestion 8

def get_input_ints():
    return list(map(int, input().split()))

N, D = get_input_ints()
print((N + 2 * D) // (2 * D + 1))

=======
Suggestion 9

def main():
    n, d = map(int, input().split())
    print(1 + (n-1) // (2*d+1))

=======
Suggestion 10

def solve():
    N, D = map(int, input().split())
    #print(N, D)
    print((N+2*D)//(2*D+1))
