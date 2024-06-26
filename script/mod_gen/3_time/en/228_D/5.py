def main():
    N = 2**20
    q = int(input())
    A = [-1] * N
    for _ in range(q):
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