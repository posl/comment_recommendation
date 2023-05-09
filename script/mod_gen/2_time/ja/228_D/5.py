def main():
    Q = int(input())
    A = [-1] * 2 ** 20
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % 2 ** 20] != -1:
                h += 1
            A[h % 2 ** 20] = x
        if t == 2:
            print(A[x % 2 ** 20])

if __name__ == '__main__':
    main()