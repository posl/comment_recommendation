Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    ans = N // (2 * D + 1)
    if N % (2 * D + 1) != 0:
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    print(int(N / (2 * D + 1)) + (1 if N % (2 * D + 1) else 0))

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    print((N + 2*D - 1) // (2*D + 1))

=======
Suggestion 5

def solve():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))
solve()

=======
Suggestion 6

def main():
    #write your code here
    N, D = map(int,input().split())
    if N % (2*D+1) == 0:
        print(N//(2*D+1))
    else:
        print(N//(2*D+1)+1)

=======
Suggestion 7

def main():
    N, D = map(int, input().split())
    print(int((N + 2 * D - 1) / (2 * D + 1)))

=======
Suggestion 8

def get_input():
    return map(int, raw_input().split())

=======
Suggestion 9

def read_int():
    return int(input())
