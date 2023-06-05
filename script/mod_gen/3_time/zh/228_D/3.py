def main():
    N = 1048576
    A = [-1] * N
    Q = int(input())
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
        else:
            print(A[x % N])

if __name__ == '__main__':
    main()