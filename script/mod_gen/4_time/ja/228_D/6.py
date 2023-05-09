def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 1048576
    N = 2 ** 20
    A = [-1] * N
    Q = int(readline())
    for _ in range(Q):
        t, x = map(int, readline().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])

if __name__ == '__main__':
    main()