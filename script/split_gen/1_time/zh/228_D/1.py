def main():
    import sys
    readline = sys.stdin.readline
    N = 2 ** 20
    A = [-1] * N
    Q = int(readline())
    for _ in range(Q):
        t, x = map(int, readline().split())
        if t == 1:
            while A[x % N] != -1:
                x += 1
            A[x % N] = x
        else:
            print(A[x % N])
