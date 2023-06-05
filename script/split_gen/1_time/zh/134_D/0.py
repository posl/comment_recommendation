def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in reversed(range(1, N + 1)):
        s = sum(B[i::i]) % 2
        if s != A[i - 1]:
            B[i] = 1
    M = sum(B)
    print(M)
    if M > 0:
        print(' '.join(map(str, [i for i, b in enumerate(B) if b])))
solve()
