Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    if N % (2*D+1) == 0:
        print(N//(2*D+1))
    else:
        print(N//(2*D+1)+1)

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    print((N + 2 * D - 1) // (2 * D + 1))

=======
Suggestion 4

def main():
    n, d = map(int, input().split())
    print((n + 2 * d) // (2 * d + 1))

=======
Suggestion 5

def main():
    N, D = map(int, input().split())
    print((N - 1) // (2 * D + 1) + 1)
    return

=======
Suggestion 6

def main():
    #入力
    N, D = map(int, input().split())
    #出力
    print((N + 2 * D) // (2 * D + 1))

=======
Suggestion 7

def main():
    n, d = map(int, input().split())
    ans = 0
    ans = int(n / (2 * d + 1))
    n = n % (2 * d + 1)
    if n > 0:
        ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, D = map(int, input().split())
    print(int(N/(2*D+1)) + 1)
