def main():
    Q = int(input())
    A = [-1] * 2 ** 20
    h = 0
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            while A[h % len(A)] != -1:
                h += 1
            A[h % len(A)] = x
        else:
            print(A[x % len(A)])

if __name__ == '__main__':
    main()