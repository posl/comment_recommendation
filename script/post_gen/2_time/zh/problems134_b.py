Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def check_apple_tree(N, D):
    check = 0
    if N % (2 * D + 1) == 0:
        check = N // (2 * D + 1)
    else:
        check = N // (2 * D + 1) + 1
    return check

=======
Suggestion 2

def main():
    N,D = map(int, input().split())
    num = 2 * D + 1
    if N % num == 0:
        print(int(N / num))
    else:
        print(int(N / num) + 1)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    print((N + 2 * D) // (2 * D + 1))

=======
Suggestion 4

def main():
    N, D = map(int, input().split())
    if N % (2 * D + 1) == 0:
        print(N // (2 * D + 1))
    else:
        print(N // (2 * D + 1) + 1)

=======
Suggestion 5

def main():
    n,d = map(int,input().split())
    print(n//((2*d)+1)+1 if n%((2*d)+1)!=0 else n//((2*d)+1))

=======
Suggestion 6

def main():
    n, d = map(int, input().split())
    print((n + 2 * d) // (2 * d + 1))

=======
Suggestion 7

def main():
    N,D = map(int,input().split())
    print(N,D)
    if N%(2*D+1) == 0:
        print(N//(2*D+1))
    else:
        print(N//(2*D+1)+1)

=======
Suggestion 8

def main():
    N, D = map(int, input().split())
    count = 0
    for i in range(1, N+1):
        if i % (2*D+1) == 0:
            count += 1
    print(count)
