def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    rows = [i for i in range(1, H + 1)]
    cols = [i for i in range(1, W + 1)]
    for i in range(N):
        rows.remove(A[i])
        cols.remove(B[i])
    for i in range(N):
        print(rows[i], cols[i])

if __name__ == '__main__':
    main()