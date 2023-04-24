Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # input
    N, K = map(int, input().split())

    # compute
    ans = 0
    while N > 0:
        N //= K
        ans += 1

    # output
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    print(len(str(N)))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    i = 1
    while True:
        if K**i > N:
            print(i)
            return
        i += 1

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    print(len(str(N), K))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    print(len(str(N).encode('utf-8').hex())//2)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    print(len(str(n).encode("utf-8")) * 8 // math.log2(k))

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    print(len(str(n).replace("0", "")) + 1)
